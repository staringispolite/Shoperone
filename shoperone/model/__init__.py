from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from shoperone.model.core import *
import hashlib

db = SQLAlchemy()

"""
  Setup the model the first time the app is run.
  params: app, the Flask app object
"""
def _init_model(app_name):
    app = Flask(app_name)

    # Debug mode allows arbitrary execution of code. Never run as True on prod.
    app.debug = False

    # Set the secret key.  keep this really secret:
    app.secret_key = 'Gr8A9/4j3Je J~XMM!j}mnL]WX/,:JT'

    # Initialize the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shoperone'
    db.init_app(app)

    print "INIT MODEL"
    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), index=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    picture_url = db.Column(db.String(2000), nullable=False)
    bio = db.Column(db.String(2000), nullable=False)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    seller_id = db.Column(db.Integer, index=True, nullable=False)
    location = db.Column(db.Integer, nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    buyer_id = db.Column(db.Integer, index=True, nullable=False)
    listing_id = db.Column(db.Integer, nullable=False)
    poundpay_id = db.Column(db.String(34), nullable=False)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    transaction_id = db.Column(db.Integer, index=True, nullable=False)
    listing_id = db.Column(db.Integer, index=True, nullable=False)

