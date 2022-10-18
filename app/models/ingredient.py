from unicodedata import name
from .db import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    amount = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now(), server_onupdate=db.func.now())


    recipe = db.relationship("Recipe", back_populates="ingredients")

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'recipe_id': self.recipe_id
        }
