import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(
    os.path.join(project_dir, database_filename))

db = SQLAlchemy()

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'tours')
DB_PATH = 'postgresql://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)


def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Tours(db.Model):
    __tablename__ = 'tours'
    title = db.Column(db.String(120))
    start_date = db.Column(db.String(120))
    end_date = db.Column(db.String(120))
    description = db.Column(db.String(1240))
    days = db.Column(db.Integer)
    nights = db.Column(db.Integer)
    max_people = db.Column(db.Integer)
    inbound = db.Column(db.String(30))
    outbound = db.Column(db.String(30))
    min_age = db.Column(db.Integer)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.get_title()


class Booking(db.Model):
    booking_date = db.Column(db.String(120))
    price = db.Column(db.Integer)
    # user =
    # tour =

    def __str__(self):
        return self.price


class Yachts(db.Model):
    __tablename__ = 'yachts'


class User(db.Model):
    __tablename__ = 'users'
    # username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12))
    dob = db.Column(db.String(10))
    address = db.Column(db.String(120))

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name.strip()

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.get_full_name()
