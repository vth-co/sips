from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, NumberRange
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    rating = IntegerField('rating', validators=[DataRequired("Rating: Please give a rating from 1 to 5"), NumberRange(
        min=1, max=5, message='Number must be between 1 and 5')])
    review = StringField('review', validators=[DataRequired("Please provide a message for your review.")])
    user_id = IntegerField("user_id", validators=[DataRequired()])
    recipe_id = IntegerField("recipe_id", validators=[DataRequired()])
