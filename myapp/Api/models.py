from flask_login import UserMixin
from myapp import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model, UserMixin):

    # __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    created_at  = db.Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username

    

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self._authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



class Images(db.Model):

    # __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    imagename = db.Column(db.String(100))
    image = db.Column(db.LargeBinary)
    created_at  = db.Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.imagename

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return '<User %r>' % self.name