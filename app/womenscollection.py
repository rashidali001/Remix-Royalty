from app import db
# from flask_login import UserMixin

class womenscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

