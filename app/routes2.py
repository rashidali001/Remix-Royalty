from app import app
from flask import redirect, render_template, jsonify, request
from app.mens_collection import menscollection, tshirts, trousers, jeans, shirts


# GETTING MEN'S COLLECTION RELATIONSHIPS

@app.route("/get_men_relationships", methods=["POST"])
def get_men_relationships():
    mens_collection = menscollection.query.first()

    relationships=[]

    for relationship in mens_collection.__mapper__.relationships:
        relationships.append(relationship.key)
    
    return jsonify(relationships)


@app.route("/field_names", methods=["POST"])
def field_names():
    models = {
        "tshirts":tshirts,
        "shirts":shirts,
        "jeans":jeans,
        "trousers":trousers        
    }
    tables_names = ["name", "barcode_no","price","quantity"]
    data = request.get_json()
    name = data["name"].lower()

    for model in models:
        if model == name:
            # RETURNS A COLUMN OBJECT IN models[name].__table__.columns where it has a name property for the name of the table
            user_fields = [model.name for model in models[name].__table__.columns if model.name in tables_names]
       

    print(user_fields)
   # user_fields = [fields.name for fields in name.__table__.columns if fields.name in tables_names]

    return jsonify(user_fields), 200



