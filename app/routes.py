from app import app, login, db
from app.models import User
from werkzeug.urls import url_parse
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required



@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        return render_template("register.html", email=email)
    return render_template("index.html")


@app.route("/admin", methods=["POST","GET"])
def admin():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("admin.html", title="admin")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/user")
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return redirect("/login")

        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("user")            
        return redirect(next_page)
    

    return render_template("login.html", title="login")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.json

        name = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Creating new user into the database
        user = User()
        user.username = name
        user.email = email
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        # logging the user in
        login_user(user)
        return jsonify(redirect=url_for("user"))
        

    return render_template("register.html", title="register")

'''
checking if email already exists
'''

@app.route("/check_email", methods=["POST"])
def check_email():
    email = request.form.get("email")
    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({'message':'success'}), 200
    
    if user is not None:
        return jsonify({"message":"error"}), 500


@app.route("/user")
@login_required
def user():
    if not current_user.is_authenticated:
        return redirect("/login")
    
    print(current_user.email)
    return render_template("user.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")




