from .db import db

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    instruction = db.Column(db.Text, nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now(), server_onupdate=db.func.now())


    user = db.relationship("User", back_populates="recipes")
    ingredient = db.relationship("Ingredient", back_populates="recipes")

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'instruction': self.instruction,
            'user_id': self.user_id,
            'ingredient_id': self.ingredient_id
        }
