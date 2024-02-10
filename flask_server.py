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


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)

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

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
    login_user(user)
    return jsonify({"message": "Logged in successfully", "user_id": user.user_id, "user_type": user.user_type})

@app.route("/getpatients", methods=["GET"])
@login_required
def get_patients():
    patients = User.query.filter_by(user_type=1).all()

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

@app.route("/transcribe", methods=["GET"])
@login_required
def transcribe():
    return jsonify({"data": upload_pipeline(request.json.get("imagebase64"))})

@app.route("/save", methods=["POST"])
@login_required
def save():
    data = request.json.data
    user_id = request.json.data.get("user_id")
    history_user_id = request.json.data.get("history_user_id")

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
            new_symptom = Symptoms(user_id=user_id, history_user_id=history_user_id, symptom=symptom['symptom'], symptom_date=datetime.strptime(symptom['symptom_date'], '%Y-%m-%d'))
            db.session.add(new_symptom)

    db.session.commit()

    return {"message": "Data saved successfully"}, 200

@app.route("/getentirehistory", methods=["GET"])
@login_required
def get_entire_history():
    user_id = request.json.get("user_id")
    notes = Notes.query.filter_by(user_id=user_id).all()
    medicine = Medicine.query.filter_by(user_id=user_id).all()
    Vitals = Vitals.query.filter_by(user_id=user_id).all()
    vaccine = Vaccine.query.filter_by(user_id=user_id).all()
    lab_result = LabResult.query.filter_by(user_id=user_id).all()
    surgeries = Surgeries.query.filter_by(user_id=user_id).all()
    emergencies = Emergencies.query.filter_by(user_id=user_id).all()
    diagnosis = Diagnosis.query.filter_by(user_id=user_id).all()
    symptoms = Symptoms.query.filter_by(user_id=user_id).all()

    return jsonify({
        "notes": [{"note": note.note, "note_date": note.note_date} for note in notes],
        "medicine": [{"med_name": med.med_name, "med_dosage": med.med_dosage, "med_frequency": med.med_frequency, "med_date": med.med_date} for med in medicine],
        "vitals": [{"vital_name": vital.vital_name, "vital_value": vital.vital_value, "vital_date": vital.vital_date} for vital in Vitals],
        "vaccine": [{"vac_name": vac.vac_name, "vac_date": vac.vac_date} for vac in vaccine],
        "lab_result": [{"lab_result": lab.lab_result, "lab_date": lab.lab_date} for lab in lab_result],
        "surgeries": [{"surgery": surgery.surgery, "surgery_date": surgery.surgery_date} for surgery in surgeries],
        "emergencies": [{"emergency_name": emergency.emergency_name, "emergency_date": emergency.emergency_date} for emergency in emergencies],
        "diagnosis": [{"diagnosis": diag.diagnosis, "diagnosis_date": diag.diag_date} for diag in diagnosis],
        "symptoms": [{"symptom": symptom.symptom, "symptom_date": symptom.symptom_date} for symptom in symptoms]
    })

@app.route("/convertNLPtoSQL", methods=["POST"])
@login_required
def convert_nlp_to_sql():
    return jsonify({"query": parse_query(request.json.get("text"))})

@app.route("/performquery", methods=["POST"])
@login_required
def perform_query():
    query = request.json.get("query")
    return jsonify({"result": db.engine.execute(query).fetchall()})

@app.route("/summarize", methods=["GET"])
@login_required
def summarize():
    pass

@app.route("/getprobable", methods=["GET"])
@login_required
def get_probable():
    pass

app.run(debug=True)