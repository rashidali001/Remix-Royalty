from app import db


# Men's collection main schema
class menscollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    shirts = db.relationship("shirts", backref="menscollection", lazy="dynamic")
    tshirts = db.relationship("tshirts", backref="menscollection", lazy="dynamic")
    trousers = db.relationship("trousers", backref="menscollection", lazy="dynamic")
    jeans = db.relationship("jeans", backref="menscollection", lazy="dynamic")

    def __repr__(self):
        return f"<{self.name}>"

# Men's collection categories

class shirts(db.Model):
    __tablename__ = "shirts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100) , index=True)
    price = db.Column(db.Integer)
    size_string = db.Column(db.String(5), index=True, nullable=True)
    size_no = db.Column(db.Integer, index=True, nullable=True)
    image = db.Column(db.Text, nullable=False)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}"


class trousers(db.Model):
    __tablename__ = "trousers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size_string = db.Column(db.String(5), index=True, nullable=True)
    size_no = db.Column(db.Integer, index=True, nullable=True)
    image = db.Column(db.Text, nullable=False)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}>"

class tshirts(db.Model):
    __tablename__ = "tshirts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size_string = db.Column(db.String(5), index=True, nullable=True)
    size_no = db.Column(db.Integer, index=True, nullable=True)
    image = db.Column(db.Text, nullable=False)
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}>"

class jeans(db.Model):
    __tablename__ = "jeans"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    barcode_no = db.Column(db.String(100), index=True)
    price = db.Column(db.Integer)
    size_string = db.Column(db.String(5), index=True, nullable=True)
    size_no = db.Column(db.Integer, index=True, nullable=True)
    image = db.Column(db.Text, nullable=False, )
    image_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    menscollection_id = db.Column(db.Integer, db.ForeignKey('menscollection.id'), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}>"


