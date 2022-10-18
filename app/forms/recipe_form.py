from tkinter.tix import Select
from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    instruction = StringField("instruction", validators=[DataRequired()])
    category = SelectField("category", choices=["Coffee", "Tea", "Alcohol", "Non-Alc"], validators=[DataRequired()])
