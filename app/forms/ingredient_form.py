from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class IngredientForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])
    recipe_id = IntegerField('recipe_id', validators=[DataRequired()])
