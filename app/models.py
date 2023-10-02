from . import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.String(32), nullable=False, unique=False)
    title = db.Column(db.String(60))
    material_type = db.Column(db.String(60))