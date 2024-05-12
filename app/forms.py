from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class SearchForm(FlaskForm):
    select_field = SelectField('Search Signs')

class UploadForm(FlaskForm):
    video = FileField(validators=[FileRequired(), FileAllowed(['mp4'], 'Only .mp4 files')])