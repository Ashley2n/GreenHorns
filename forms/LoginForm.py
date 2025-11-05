from flask_wtf import FlaskForm
from pyexpat.errors import messages
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(messages="Please enter a username")])
    password = StringField('Password', validators=[DataRequired(messages="Please enter a password")])
    submit = SubmitField('Submit')