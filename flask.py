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
    pass

@app.route("/save", methods=["POST"])
@login_required
def save():
    pass

@app.route("/getentirehistory", methods=["GET"])
@login_required
def get_entire_history():
    pass

@app.route("/convertNLPtoSQL", methods=["POST"])
@login_required
def convert_nlp_to_sql():
    pass

@app.route("/performquery", methods=["POST"])
@login_required
def perform_query():
    pass

@app.route("/summarize", methods=["GET"])
@login_required
def summarize():
    pass

@app.route("/getprobable", methods=["GET"])
@login_required
def get_probable():
    pass

app.run(debug=True)

def get_all_data(user_id):
    assert type(user_id) == str
    user_id = request.json.get(user_id)
    lst = []
    lst.append(Notes.query.filter_by(user_id=user_id).all())
    lst.append(Medicine.query.filter_by(user_id=user_id).all())
    lst.append(Vitals.query.filter_by(user_id=user_id).all())
    lst.append(Vaccine.query.filter_by(user_id=user_id).all())
    lst.append(LabResult.query.filter_by(user_id=user_id).all())
    lst.append(Surgeries.query.filter_by(user_id=user_id).all())
    lst.append(Emergencies.query.filter_by(user_id=user_id).all())
    lst.append(Diagnosis.query.filter_by(user_id=user_id).all())
    lst.append(Symptoms.query.filter_by(user_id=user_id).all())
    
    print(lst)
    return lst