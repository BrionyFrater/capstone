from flask_wtf import FlaskForm
from wtforms import SelectField

class SearchForm(FlaskForm):
    select_field = SelectField('Search Signs')