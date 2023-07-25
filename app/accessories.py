from app import db

class accessories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    watches = db. relationship("watches_a", backref="accessories", lazy="dynamic")
    perfumes = db. relationship("perfumes_a", backref="accessories", lazy="dynamic")
    shoes = db. relationship("shoes_a", backref="accessories", lazy="dynamic")



class watches_a(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    accessories_id = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)


class perfumes_a(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    accessories_id = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)

class shoes_a(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    barcode_no = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(10))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    accessories_id = db.Column(db.Integer, db.ForeignKey('accessories.id'), nullable=False)
