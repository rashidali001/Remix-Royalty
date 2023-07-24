from app import db

class childrenscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    shirts = db.relationship('shirts', backref="childrenscollection", lazy="dynamic")
    dress = db.relationship('dress', backref="childrenscollection", lazy="dynamic")
    tshirts = db.relationship('tshirts', backref="childrenscollection", lazy="dynamic")
    shorts = db.relationship('shorts', backref="childrenscollection", lazy="dynamic")



class shirts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nulable=False)

class dress(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nulable=False)

class tshirts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nulable=False)

class shorts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nulable=False)

