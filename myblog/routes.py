from flask import render_template, redirect, url_for, flash, request
from myblog import app
from myblog.forms import FormCreateAccount, FormLogin

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
        flash(f"Login successful! - Wellcome {form_login.email.data}", "alert-success")
        return redirect(url_for("home"))

    if form_createAccount.validate_on_submit() and "button_submit_create_account" in request.form:
        flash(f"New account created! - Wellcome {form_createAccount.email.data}", "alert-success") 
        return redirect(url_for("home"))

    return render_template("login.html", form_createAccount=form_createAccount, form_login=form_login)

