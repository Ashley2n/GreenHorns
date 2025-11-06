from wsgiref.validate import validator

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Optional


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter a username")])
    email = StringField('Email', validators=[Email(message='Invalid email'), Optional()] )
    password = StringField('Password', validators=[DataRequired(message="Please enter a password")])
    submit = SubmitField('Register')