from flask_sqlalchemy import SQLAlchemy
from apps import app

db=SQLAlchemy(app)

class Goods(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gname=db.Column(db.String(80),unique=True)
    gprice=db.Column(db.Integer)
    gtype=db.Column(db.String(5))