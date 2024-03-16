from flask import render_template, redirect, url_for, flash, request,abort
from myblog import app, database, bcrypt
from myblog.forms import FormCreateAccount, FormLogin, FormEditProfile, FormCreatePost
from myblog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required
from PIL import Image
import secrets
import os


@app.route("/")
def home():
    all_posts = Post.query.order_by(Post.id.desc())
    return render_template("home.html", all_posts=all_posts)


@app.route("/users")
@login_required
def users():
    all_users = User.query.all()
    return render_template("users.html", users_list=all_users)


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
            flash("Login Error! - Incorrect e-mail or password", "alert-danger")            


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
    photo_profile = url_for("static", filename=f"photos_profile/{current_user.photo_profile}") 
    return render_template("/profile.html", photo_profile=photo_profile)


@app.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    form_edit_profile = FormEditProfile()

    photo_profile = url_for("static", filename=f"photos_profile/{current_user.photo_profile}")
    
    if form_edit_profile.validate_on_submit():
        current_user.email = form_edit_profile.email.data
        current_user.username = form_edit_profile.username.data
        if form_edit_profile.photo_profile.data: 
            new_photo = save_photo(form_edit_profile.photo_profile.data)
            current_user.photo_profile = new_photo
        current_user.courses = update_courses_list(form_edit_profile)
        database.session.commit()
        flash("updated Successfully", "alert-success")
        return redirect(url_for("profile"))
    else:
        # Automatic fill the form with users data
        form_edit_profile.username.data = current_user.username
        form_edit_profile.email.data = current_user.email
        # fill the users courses
        for course in current_user.courses.split(';'):
            for field in form_edit_profile:
                if course in field.label.text:
                    field.data = True
    
    return render_template("edit_profile.html", photo_profile=photo_profile, form_edit_profile=form_edit_profile)


def save_photo(photo):
    code = secrets.token_hex(8)
    name, extension = os.path.splitext(photo.filename)
    photo_name = name + code + extension
    local_path = os.path.join(app.root_path, 'static/photos_profile', photo_name)
    size = (200, 200)
    new_photo = Image.open(photo)
    new_photo.thumbnail(size)
    new_photo.save(local_path)
    return photo_name


def update_courses_list(form):
    courses_list = []
    for field in form:
        if "course_" in field.name:
            if field.data:
                courses_list.append(field.label.text)
    
    if not courses_list:
        return "none"
    
    return ';'.join(courses_list)


@app.route("/post/create", methods=["GET", "POST"])
@login_required
def create_post():

    form_create_post = FormCreatePost()

    if form_create_post.validate_on_submit():
        with app.app_context():
            post = Post(title=form_create_post.title.data, body=form_create_post.body.data, author=current_user )
            database.session.add(post)
            database.session.commit()
            flash("Post Created!", "alert-success")
            return redirect( url_for('home') )

    return render_template("create_post.html", form_create_post=form_create_post)


@app.route("/post/<post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):

    post = Post.query.get(post_id)

    if current_user == post.author:
        form = FormCreatePost()
        
        if request.method == "GET":
            form.title.data = post.title
            form.body.data = post.body
        
        elif form.validate_on_submit():
            post.title = form.title.data
            post.body = form.body.data
            database.session.commit()
            flash("Post modified successfully", "alert-success")

    else:
        form = None

    return render_template("post.html", post=post, form_create_post=form)


@app.route("/post/<post_id>/delete", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    
    post = Post.query.get(post_id)

    if current_user == post.author:
        database.session.delete(post)
        database.session.commit()
        flash("Post deleted!", "alert-danger")
        return redirect( url_for("home"))
    else:
        abort(403)