from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(72), index=True)
    email = db.Column(db.String(72), index=True, unique=True)
    password_hash = db.Column(db.String(72))


    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)
    
    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)
    
    def __repr__ (self):
        return f"<user.{self.username}>"
    
