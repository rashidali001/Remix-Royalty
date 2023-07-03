from app import db


# Men's collection main schema
class menscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    shirts = db.relationship("shirts", backref="menscollection", lazy="dynamic")
    tshirts = db.relationship("tshirts", backref="menscollection", lazy="dynamic")
    trousers = db.relationship("trousers", backref="menscollection", lazy="dynamic")
    jeans = db.relationship("jeans", backref="menscollection", lazy="dynamic")

# Men's collection categories

class shirts(db.Model):
    __tablename__ = "shirts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100) , index=True)
    price = db.Column(db.Integer)
    size = db.Column(db.String(5), index=True)
    image = db.Column(db.Text, nullable=False, unique=True)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__():
        return f"<{shirts.__tablename__}"


class trousers(db.Model):
    __tablename__ = "trousers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size = db.Column(db.String(5), index=True)
    image = db.Column(db.Text, nullable=False, unique=True)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__():
        return f"<{trousers.__tablename__}>"

class tshirts(db.Model):
    __tablename__ = "tshirts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size = db.Column(db.String(5), index=True)
    image = db.Column(db.Text, nullable=False, unique=True)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__():
        return f"<{tshirts.__tablename__}>"

class jeans(db.Model):
    __tablename__ = "jeans"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size = db.Column(db.String(5), index=True)
    image = db.Column(db.Text, nullable=False, unique=True)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__():
        return f"<{jeans.__tablename__}>"