from app import app, db
from flask import redirect, render_template, jsonify, request
from werkzeug.utils import secure_filename
from app.mens_collection import menscollection, tshirts, trousers, jeans, shirts
from app.womenscollection import womenscollection, blouse_w, dress_w, trouser_w, jeans_w
from app.childrenscollection import childrenscollection, shirts_c, dress_c, tshirts_c, shorts_c
from app.accessories import accessories, watches_a, perfumes_a, shoes_a


DB_collection = {
    "menscollection" : menscollection,
    "womenscollection" : womenscollection,
    "childrenscollection" : childrenscollection,
    "accessories" : accessories
}

models = {
        "tshirts":tshirts,      # men's collection
        "shirts":shirts,
        "jeans":jeans,
        "trousers":trousers,
        "blouse_w":blouse_w,    # womens's collection
        "dress_w":dress_w ,
        "trouser_w": trouser_w,
        "jeans_w" : jeans_w,
        "watches_a" : watches_a,    # accessories
        "perfumes_a" : perfumes_a,
        "shoes_a" : shoes_a,
        "shirts_c" : shirts_c,  #children's collection
        "dress_c" : dress_c,
        "tshirts_c" : tshirts_c,
        "short_c" : shorts_c

}


# GETTING MEN'S COLLECTION RELATIONSHIPS

@app.route("/get_relationships", methods=["POST"])
def get_relationships():
    data = request.get_json()
    collection_name = data["collection_name"]

    for key in DB_collection:
        if key == collection_name:
            collection = DB_collection[key].query.first()

    # list to store all the string values of the relationships the model has
    # placed in the category section in the site
    relationships=[]

    for relationship in collection.__mapper__.relationships:
        relationships.append(relationship.key)
    
    return jsonify(relationships)


# GETTING FIELD NAMES 

@app.route("/field_names", methods=["POST"])
def field_names():
    
    tables_names = ["name", "barcode_no","price","quantity"]
    data = request.get_json() # Gets data from ajax in json format
    name = data["name"].lower()

    for model in models:
        if model == name:
            # List comprehension 
            # RETURNS A COLUMN OBJECT IN models[name].__table__.columns where it has a name property for the name of the table
            user_fields = [model.name for model in models[name].__table__.columns if model.name in tables_names]
       

   # user_fields = [fields.name for fields in name.__table__.columns if fields.name in tables_names]

    return jsonify(user_fields), 200


# ADDING COLLECTION

@app.route("/add_collection", methods=["POST"])
def add_collection():
    category = request.form.get("category")
    collection = request.form.get("db_collection")

    # OBTAINING THE IMAGE
    pic = request.files["image"]

    for key_db in DB_collection:
        if key_db == collection:
            for key in models:                 
                if key == category:
                    db_collection_obj = DB_collection[key_db]().query.first()
                    object = models[key]()
                    object.name = request.form.get("name_of_product")
                    object.barcode_no = request.form.get("barcode")
                    object.price = request.form.get("price")
                    object.size_string = request.form.get("size")
                    object.size_no = request.form.get("size_no")
                    object.description = request.form.get("description")
                    object.quantity = request.form.get("quantity")
                    object.image = pic.read()
                    object.image_name = secure_filename(pic.filename)
                    object.mimetype = pic.mimetype
                    object.menscollection_id = db_collection_obj.id

                    db.session.add(object)
                    db.session.commit()
    
    return "success", 200





