from app import db
# from flask_login import UserMixin

class womenscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    blouse = db.relationship("blouse_w", backref="womenscollection", lazy="dynamic")
    dress = db.relationship("dress_w", backref="womenscollection", lazy="dynamic")
    trouser = db.relationship("trouser_w", backref="womenscollection", lazy="dynamic")
    jeans = db.relationship("jeans_w", backref="womenscollection", lazy="dynamic")


class blouse_w(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection_id = db.Column(db.Integer, db.ForeignKey("womenscollection.id"), nullable=False)

class dress_w(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection_id = db.Column(db.Integer, db.ForeignKey("womenscollection.id"), nullable=False)

class trouser_w(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection_id = db.Column(db.Integer, db.ForeignKey('womenscollection.id'), nullable=False)


class jeans_w(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection_id = db.Column(db.Integer, db.ForeignKey('womenscollection.id'), nullable=False)


