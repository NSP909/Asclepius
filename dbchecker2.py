import psycopg2
from psycopg2 import OperationalError
import os

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://<db-user>:<db-password>@<unix-socket-path>/<db-name>'
db = SQLAlchemy(app)


unix_socket = '/cloudsql/favorable-mix-413908:us-central1:hacklytics'

conn = psycopg2.connect(database="postgres", user="postgres", password="hacklytics", host=unix_socket)
