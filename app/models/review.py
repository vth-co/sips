from logging.handlers import RotatingFileHandler
from .db import db

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now(), server_onupdate=db.func.now())


    user = db.relationship("User", back_populates="reviews")
    recipe = db.relationship("Recipe", back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'review': self.review,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id
        }
