from app import app
from flask import redirect, render_template, jsonify, request
from app.mens_collection import menscollection


# GETTING MEN'S COLLECTION RELATIONSHIPS

@app.route("/get_men_relationships", methods=["POST"])
def get_men_relationships():
    mens_collection = menscollection.query.first()

    relationships=[]

    for relationship in mens_collection.__mapper__.relationships:
        relationships.append(relationship.key)
    
    return jsonify(relationships)
