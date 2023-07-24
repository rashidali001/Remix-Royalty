from app import db
# from flask_login import UserMixin

class womenscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    blouse = db.relationship("blouse", backref="womescollection", lazy="dynamic")
    dress = db.relationship("dress", backref="womescollection", lazy="dynamic")
    trouser = db.relationship("trouser", backref="womescollection", lazy="dynamic")
    jeans = db.relationship("jeans", backref="womescollection", lazy="dynamic")


class blouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection = db.Column(db.Integer, db.ForeignKey("womenscollection.id"), nullable=False)

class dress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection = db.Column(db.Integer, db.ForeignKey("womenscollection.id"), nullable=False)

class trouser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection = db.Column(db.Integer, db.ForeignKey('womenscollection.id'), nullable=False)


class jeans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.column(db.Text)
    mimetype = db.Column(db.Text)
    womenscollection = db.Column(db.Integer, db.ForeignKey('womenscollection.id'), nullable=False)


