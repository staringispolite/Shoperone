#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Table, db.Column, Integer, String
#Base = declarative_base()

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
# import core

db = None

"""
  Setup the model the first time the app is run.
  params: app, the Flask app object
"""
def _init_model(app):
    print "\n\n\nINIT MODEL\n\n\n"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shoperone'
    global db
    db = SQLAlchemy(app)



