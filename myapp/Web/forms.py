from collections.abc import Mapping, Sequence
from typing import Any
from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators, FileField
from wtforms.validators import DataRequired, ValidationError
from myapp.Api.models import User
from myapp import bcrypt

class ImageStorageForm(FlaskForm):
    imagename = StringField('imagename', name="imagename", validators=[DataRequired()], render_kw={"class": "form-control form-control-sm"})
    image =  FileField('image', name="image", validators=[DataRequired()],  render_kw={"class": "form-control form-control-sm"})

