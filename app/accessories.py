from app import db

class accessories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    watches = db. relationship("watches", backref="accessories", lazy="dynamic")
    perfumes = db. relationship("perfumes", backref="accessories", lazy="dynamic")
    shoes = db. relationship("shoes", backref="accessories", lazy="dynamic")



class watches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    accessories = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)


class perfumes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    accessories = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)

class shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    accessories = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)
