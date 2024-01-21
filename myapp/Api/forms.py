from collections.abc import Mapping, Sequence
from typing import Any
from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, ValidationError
from myapp.Api.models import User
from myapp import bcrypt

class LoginForm(FlaskForm):
    username = StringField('username', name="username", validators=[DataRequired()], render_kw={"class": "form-control form-control-sm"})
    # email = StringField('email', name="email", validators=[DataRequired()],  render_kw={"class": "form-control form-control-sm"})
    password =  PasswordField('password', name="password", validators=[DataRequired()],  render_kw={"class": "form-control form-control-sm"})


    def validate_username(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            print("error2")
            raise ValidationError(f"{self.username.data} not exist..")
        




class SignUpForm(FlaskForm):
    username = StringField('username', name='username', validators=[DataRequired()], render_kw={"class": "form-control form-control-sm text-dark"})
    email = StringField('email', name='email', validators=[DataRequired()],  render_kw={"class": "form-control form-control-sm text-dark"})
    password =  PasswordField('password', validators=[DataRequired()],  render_kw={"class": "form-control form-control-sm text-dark"})

    def validate_email(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            print("error")
            raise ValidationError(f"{self.email.data} already exists. Please choose a different username.")
    
    def validate_username(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            print("error2")
            raise ValidationError(f"{self.username.data} already exists. Please choose a different username.")
        
