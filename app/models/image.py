from .db import db

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now(), server_onupdate=db.func.now())


    user = db.relationship("User", back_populates="images")
    recipe = db.relationship("Recipe", back_populates="images")


    def to_dict(self):
        return {
            'id': self.id,
            'image': self.image,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id
        }
