from flask import render_template, redirect, url_for, flash, request
from myblog import app, database
from myblog.forms import FormCreateAccount, FormLogin
from myblog.models import User

users_list = ["Tiago", "Robert", "Ana", "Vanessa", "Marcus", "Andi"]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/users")
def users():
    return render_template("users.html", users_list=users_list)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_createAccount = FormCreateAccount()
    form_login = FormLogin()

    if form_login.validate_on_submit() and "button_submit_login" in request.form:
        flash(f"Login successful! - Welcome {form_login.email.data}", "alert-success")
        return redirect(url_for("home"))

    if form_createAccount.validate_on_submit() and "button_submit_create_account" in request.form:
        with app.app_context():
            user = User(username=form_createAccount.username.data, email=form_createAccount.email.data, password=form_createAccount.password.data)
            database.session.add(user)
            database.session.commit()
            flash(f"New account created! - Welcome {form_createAccount.email.data}", "alert-success") 
            return redirect(url_for("home"))

    return render_template("login.html", form_createAccount=form_createAccount, form_login=form_login)

