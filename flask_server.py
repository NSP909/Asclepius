from flask import Flask, redirect
from flask import request
from flask import jsonify
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()
connection_string = os.getenv("CONNECTION_STRING")

from upload_pipeline import upload_pipeline

from parse_query import parse_query
from predict_disease import predict_disease
from summary import summarize

from flask import current_app, g

from flask_cors import CORS

from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)

CORS(app)

class User(db.Model):
    __tablename__ = 'usertable'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    user_type = db.Column(db.SmallInteger, nullable=False)

class UserPwd(db.Model):
    __tablename__ = 'userpwd'
    pwd_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    pwd = db.Column(db.String(32), nullable=False)

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    info_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    fullname = db.Column(db.String(32), nullable=False)
    user_height = db.Column(db.Integer, nullable=False)
    user_weight = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(32), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    ethnicity = db.Column(db.String(32), nullable=False)
    sex = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.String(32), nullable=False)

class Notes(db.Model):
    __tablename__ = 'notes'
    note_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    note = db.Column(db.String(255), nullable=False)
    note_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Medicine(db.Model):
    __tablename__ = 'medicine'
    med_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    med_name = db.Column(db.String(32), nullable=False)
    med_dosage = db.Column(db.String(32), nullable=False)
    med_frequency = db.Column(db.String(32), nullable=False)
    med_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Vitals(db.Model):
    __tablename__ = 'vitals'
    vital_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    vital_name = db.Column(db.String(32), nullable=False)
    vital_value = db.Column(db.String(32), nullable=False)
    vital_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Vaccine(db.Model):
    __tablename__ = 'vaccine'
    vac_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    vac_name = db.Column(db.String(32), nullable=False)
    vac_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class LabResult(db.Model):
    __tablename__ = 'lab_result'
    lab_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    lab_result = db.Column(db.String(2048), nullable=False)
    lab_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Surgeries(db.Model):
    __tablename__ = 'surgeries'
    surgery_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    surgery = db.Column(db.String(255), nullable=False)
    surgery_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Emergencies(db.Model):
    __tablename__ = 'emergencies'
    emergency_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    emergency_name = db.Column(db.String(255), nullable=False)
    emergency_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Diagnosis(db.Model):
    __tablename__ = 'diagnosis'
    diag_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    diag_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

class Symptoms(db.Model):
    __tablename__ = 'symptoms'
    symptom_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usertable.user_id'), nullable=False)
    diag_id = db.Column(db.Integer, db.ForeignKey('diagnosis.diag_id'), nullable=False)
    symptom = db.Column(db.String(255), nullable=False)
    symptom_date = db.Column(db.Date, nullable=False)
    history_user_id = db.Column(db.Integer, nullable=False)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "Invalid username or password"}), 400
    user_pwd = UserPwd.query.filter_by(user_id=user.user_id).first()
    if user_pwd is None or user_pwd.pwd != password:
        return jsonify({"message": "Invalid username or password"}), 400
    return jsonify({"message": "Logged in successfully", "user_id": user.user_id, "user_type": user.user_type})

@app.route("/getpatients", methods=["GET"])
def get_patients():
    patients = User.query.filter_by(user_type=1).all()
    print(patients)
    print(patients[0].user_id)
    for patient in patients:
        patient_info = UserInfo.query.filter_by(user_id=patient.user_id).first()
        patient.fullname = patient_info.fullname
        patient.date_of_birth = patient_info.date_of_birth
        patient.user_height = patient_info.user_height
        patient.user_weight = patient_info.user_weight
        patient.race = patient_info.race
        patient.ethnicity = patient_info.ethnicity
        patient.sex = patient_info.sex
        patient.gender = patient_info.gender

    return jsonify([{
        "user_id": patient.user_id, 
        "username": patient.username,
        "fullname": patient.fullname,
        "date_of_birth": patient.date_of_birth,
        "user_height": patient.user_height,
        "user_weight": patient.user_weight,
        "race": patient.race,
        "ethnicity": patient.ethnicity,
        "sex": patient.sex,
        "gender": patient.gender
    } for patient in patients])

@app.route("/transcribe", methods=["POST"])
def transcribe():
    return jsonify({"data": str(upload_pipeline(request.json.get("imagebase64")))})

@app.route("/save", methods=["POST"])
def save():
    data = request.json['data']
    username = data.get("username")
    user_id = User.query.filter_by(username=username).first().user_id
    history_user_id = data.get("history_user_id")

    # if any kind of field is None then replace with the string "None" and if any date is None replace with the current date
    for note in data['notes']:
        if note['note'] is None:
            note['note'] = "None"
        if note['note_date'] is None:
            note['note_date'] = datetime.now().date()

    for med in data['medicine']:
        if med['med_name'] is None:
            med['med_name'] = "None"
        if med['med_dosage'] is None:
            med['med_dosage'] = "None"
        if med['med_frequency'] is None:
            med['med_frequency'] = "None"
        if med['med_date'] is None:
            med['med_date'] = datetime.now().date()

    for vital in data['vitals']:
        if vital['vital_name'] is None:
            vital['vital_name'] = "None"
        if vital['vital_value'] is None:
            vital['vital_value'] = "None"
        if vital['vital_date'] is None:
            vital['vital_date'] = datetime.now().date()

    for vac in data['vaccine']:
        if vac['vac_name'] is None:
            vac['vac_name'] = "None"
        if vac['vac_date'] is None:
            vac['vac_date'] = datetime.now().date()

    for lab in data['lab_result']:
        if lab['lab_result'] is None:
            lab['lab_result'] = "None"
        if lab['lab_date'] is None:
            lab['lab_date'] = datetime.now().date()

    for surgery in data['surgeries']:
        if surgery['surgery'] is None:
            surgery['surgery'] = "None"
        if surgery['surgery_date'] is None:
            surgery['surgery_date'] = datetime.now().date()

    for emergency in data['emergencies']:
        if emergency['emergency_name'] is None:
            emergency['emergency_name'] = "None"
        if emergency['emergency_date'] is None:
            emergency['emergency_date'] = datetime.now().date()

    for diag in data['diagnosis']:
        if diag['diagnosis'] is None:
            diag['diagnosis'] = "None"
        if diag['diag_date'] is None:
            diag['diag_date'] = datetime.now().date()

    for symptom in data['symptoms']:
        if symptom['symptom'] is None:
            symptom['symptom'] = "None"
        if symptom['diag_id'] is None:
            symptom['diag_id'] = "None"
        if symptom['symptom_date'] is None:
            symptom['symptom_date'] = datetime.now().date()

    if data['notes']:
        for note in data['notes']:
            new_note = Notes(user_id=user_id, history_user_id=history_user_id, note=note['note'], note_date=datetime.strptime(note['note_date'], '%Y-%m-%d'))
            db.session.add(new_note)

    if data['medicine']:
        for medicine in data['medicine']:
            new_medicine = Medicine(user_id=user_id, history_user_id=history_user_id, med_name=medicine['med_name'], med_dosage=medicine['med_dosage'], med_frequency=medicine['med_frequency'], med_date=datetime.strptime(medicine['med_date'], '%Y-%m-%d'))
            db.session.add(new_medicine)

    if data['vaccine']:
        for vaccine in data['vaccine']:
            new_vaccine = Vaccine(user_id=user_id, history_user_id=history_user_id, vac_name=vaccine['vac_name'], vac_date=datetime.strptime(vaccine['vac_date'], '%Y-%m-%d'))
            db.session.add(new_vaccine)

    if data['lab_result']:
        for lab_result in data['lab_result']:
            new_lab_result = LabResult(user_id=user_id, history_user_id=history_user_id, lab_result=lab_result['lab_result'], lab_date=datetime.strptime(lab_result['lab_date'], '%Y-%m-%d'))
            db.session.add(new_lab_result)

    if data['surgeries']:
        for surgery in data['surgeries']:
            new_surgery = Surgeries(user_id=user_id, history_user_id=history_user_id, surgery=surgery['surgery'], surgery_date=datetime.strptime(surgery['surgery_date'], '%Y-%m-%d'))
            db.session.add(new_surgery)

    if data['diagnosis']:
        for diagnosis in data['diagnosis']:
            new_diagnosis = Diagnosis(user_id=user_id, history_user_id=history_user_id, diagnosis=diagnosis['diagnosis'], diag_date=datetime.strptime(diagnosis['diag_date'], '%Y-%m-%d'))
            db.session.add(new_diagnosis)

    if data['symptoms']:
        for symptom in data['symptoms']:
            new_symptom = Symptoms(user_id=user_id, history_user_id=history_user_id, diag_id=symptom['diag_id'], symptom=symptom['symptom'], symptom_date=datetime.strptime(symptom['symptom_date'], '%Y-%m-%d'))
            db.session.add(new_symptom)

    db.session.commit()

    return {"message": "Data saved successfully"}, 200

@app.route("/getentirehistory", methods=["POST"])
def get_entire_history():
    user_id = request.json.get("user_id")
    notes = Notes.query.filter_by(user_id=user_id).all()
    medicine = Medicine.query.filter_by(user_id=user_id).all()
    vitals = Vitals.query.filter_by(user_id=user_id).all()
    vaccine = Vaccine.query.filter_by(user_id=user_id).all()
    lab_result = LabResult.query.filter_by(user_id=user_id).all()
    surgeries = Surgeries.query.filter_by(user_id=user_id).all()
    emergencies = Emergencies.query.filter_by(user_id=user_id).all()
    diagnosis = Diagnosis.query.filter_by(user_id=user_id).all()
    symptoms = Symptoms.query.filter_by(user_id=user_id).all()

    return jsonify({
        "notes": [{"note": note.note, "note_date": note.note_date} for note in notes],
        "medicine": [{"med_name": med.med_name, "med_dosage": med.med_dosage, "med_frequency": med.med_frequency, "med_date": med.med_date} for med in medicine if medicine is not None],
        "vitals": [{"vital_name": vital.vital_name, "vital_value": vital.vital_value, "vital_date": vital.vital_date} for vital in vitals if vitals is not None],
        "vaccine": [{"vac_name": vac.vac_name, "vac_date": vac.vac_date} for vac in vaccine if vaccine is not None],
        "lab_result": [{"lab_result": lab.lab_result, "lab_date": lab.lab_date} for lab in lab_result if lab_result is not None],
        "surgeries": [{"surgery": surgery.surgery, "surgery_date": surgery.surgery_date} for surgery in surgeries if surgeries is not None],
        "emergencies": [{"emergency_name": emergency.emergency_name, "emergency_date": emergency.emergency_date} for emergency in emergencies if emergencies is not None],
        "diagnosis": [{"diagnosis": diag.diagnosis, "diagnosis_date": diag.diag_date} for diag in diagnosis if diagnosis is not None],
        "symptoms": [{"diag_id": symptom.diag_id, "symptom": symptom.symptom, "symptom_date": symptom.symptom_date} for symptom in symptoms if symptoms is not None]
    })

@app.route("/convertNLPtoSQL", methods=["POST"])
def convert_nlp_to_sql():
    query = parse_query(request.json.get("text"))
    query = query[query.index("SELECT"):query.index(";")+1]
    return jsonify({"query": query})

@app.route("/performquery", methods=["POST"])
def perform_query():
    query = request.json.get("query")
    print(f"Executing query: {query}")
    with db.engine.connect() as connection:
        result = connection.execute(text(query))
    return jsonify({"result": [dict(row._asdict()) for row in result]})

@app.route("/summarise", methods=["POST"])
def summarise():
    data = request.json.get("data")
    print(data)
    data_string = str(data)
    summary = summarize(data_string)
    return jsonify({"summary": summary})

@app.route("/getprobable", methods=["POST"])
def get_probable():
    data = request.json.get("data")
    data_string = str(data)
    print(data_string)
    prediction = predict_disease(data_string)
    return jsonify({"prediction": prediction})

app.run(debug=True)