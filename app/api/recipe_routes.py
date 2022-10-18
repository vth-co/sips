from crypt import methods
from flask import Blueprint, json, jsonify, redirect, request
from flask_login import login_required
from app.models import db, Recipe, Ingredient, Review, User, Category
from app.forms import RecipeForm

recipe_routes = Blueprint('recipes', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages

@recipe_routes.route('/')
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify(
        [recipe.to_dict() for recipe in recipes]
    )

@recipe_routes.route('/recipe/<int:id>', methods=["POST"])
@login_required
