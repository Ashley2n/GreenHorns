from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(messages="Please enter a username")])
    password = StringField('Password', validators=[DataRequired(messages="Please enter a password")])
    submit = SubmitField('Register')