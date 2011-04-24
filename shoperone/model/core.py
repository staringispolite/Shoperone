import hashlib
from shoperone.model import db

class User(db.Model):
    __tablename__ = 'user'

    def __init__(self, first_name, last_name, email, password, 
                 picture_url = None, bio = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = hashlib.sha256(password).hexdigest()
        self.picture_url = picture_url
        self.bio = bio

    def __repr__(self):
        return "<User %s>" % self.email

    id = db.Column('id', Integer, primary_key=True, nullable=False)
    first_name = db.Column('first_name', String(255), nullable=False)
    last_name = db.Column('last_name', String(255), nullable=False)
    email = db.Column('email', String(255), key=True, nullable=False)
    password_hash = db.Column('password_hash', String(64), nullable=False)
    picture_url = db.Column('picture_url', String(2000), nullable=False)
    bio = db.Column('bio', String(2000), nullable=False)


class Listing(db.Model):
    __tablename__= 'listing'

    id = db.Column('id', Integer, primary_key=True, nullable=False)
    seller_id = db.Column('seller_id', Integer, key=True, nullable=False)
    location = db.Column('location', Integer, nullable=False)


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column('id', Integer, primary_key=True, nullable=False)
    buyer_id = db.Column('buyer_id', Integer, key=True, nullable=False)
    listing_id = db.Column('listing_id', Integer, nullable=False)
    poundpay_id = db.Column('poundpay_id', String(34), nullable=False)


class Request(db.Model):
    __tablename__ = 'request'

    id = db.Column('id', Integer, primary_key=True, nullable=False)
    transaction_id = db.Column('transaction_id', Integer, key=True, nullable=False)
    listing_id = db.Column('listing_id', Integer, key=True, nullable=False)
