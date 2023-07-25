from app import db

class childrenscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    shirts = db.relationship('shirts_c', backref="childrenscollection", lazy="dynamic")
    dress = db.relationship('dress_c', backref="childrenscollection", lazy="dynamic")
    tshirts = db.relationship('tshirts_c', backref="childrenscollection", lazy="dynamic")
    shorts = db.relationship('shorts_c', backref="childrenscollection", lazy="dynamic")



class shirts_c(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection_id = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nullable=False)

class dress_c(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection_id = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nullable=False)

class tshirts_c(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection_id = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nullable=False)

class shorts_c(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    barcode_no = db.Column(db.String(20))
    image = db.Column(db.Text)
    image_name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    childrenscollection_id = db.Column(db.Integer, db.ForeignKey('childrenscollection.id'), nullable=False)

