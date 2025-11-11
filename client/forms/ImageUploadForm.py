from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



class ImageUploadForm(FlaskForm):
    image = FileField('Upload Dish Image', validators=[
        FileRequired(),
        FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')
    ])
    submit = SubmitField('Analyze')