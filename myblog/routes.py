from flask import render_template, redirect, url_for, flash, request
from myblog import app, database, bcrypt
from myblog.forms import FormCreateAccount, FormLogin
from myblog.models import User
from flask_login import login_user, logout_user, current_user, login_required

users_list = ["Tiago", "Robert", "Ana", "Vanessa", "Marcus", "Andi"]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/users")
@login_required
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
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.remember_me.data)
            flash(f"Login successful! - Welcome {form_login.email.data}", "alert-success")
            parameter_next = request.args.get('next')
            if parameter_next:
                return redirect(parameter_next)
            else:
                return redirect(url_for("home"))
        else:
            flash(f"Login Error! - Incorrect e-mail or password", "alert-danger")            


    if form_createAccount.validate_on_submit() and "button_submit_create_account" in request.form:
        with app.app_context():
            crypt_password = bcrypt.generate_password_hash(form_createAccount.password.data)
            user = User(username=form_createAccount.username.data, email=form_createAccount.email.data, password=crypt_password)
            database.session.add(user)
            database.session.commit()
            flash(f"New account created! - Welcome {form_createAccount.email.data}", "alert-success") 
            return redirect(url_for("home"))

    return render_template("login.html", form_createAccount=form_createAccount, form_login=form_login)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Logout done!", "alert-success")
    return redirect( url_for("home"))


@app.route("/profile")
@login_required
def profile():
    return render_template("/profile.html")


@app.route("/post/create")
@login_required
def create_post():
    return render_template("create_post.html")