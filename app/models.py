from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    inventory = db.relationship('Inventory', backref='owner', lazy=True)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
