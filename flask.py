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


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:hacklytics@35.232.153.130:5432/postgres"
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