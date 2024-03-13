from tkinter.font import BOLD
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from myblog.models import User
from flask_login import current_user

class FormCreateAccount(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()] )
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    password = PasswordField("Password: ", validators=[DataRequired(), Length(6,20)] )
    confirmation = PasswordField("Password Confirmation: ", validators=[DataRequired(), EqualTo('password')] )
    button_submit_create_account = SubmitField("Create Account")

    def validate_username(self, username):
        username_exist = User.query.filter_by(username=username.data).first()
        if username_exist:
            raise ValidationError("Username already exist in Database.Use another Username or Log in")
    
    def validate_email(self, email):
        email_exist = User.query.filter_by(email=email.data).first()
        if email_exist:
            raise ValidationError("E-mail already exist in Database. Use another e-mail or Log in")


class FormLogin(FlaskForm):
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    password = PasswordField("Password: ", validators=[DataRequired(), Length(6,20)] )
    remember_me = BooleanField("Remember Password")
    button_submit_login = SubmitField("Login")


class FormEditProfile(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()] )
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    photo_profile = FileField("Update Photo Profile", validators=[FileAllowed(["jpg", "png", "jpeg"])] )
    button_save_changes = SubmitField("Save Changes")

    course_webdesigner = BooleanField("Web Designer - Programming")
    course_sql = BooleanField("SQL - Data base")
    course_python = BooleanField("Python - Programming")
    course_javascript = BooleanField("JavaScript - Programming")
    course_powerpoint = BooleanField("PowerPoint - Office")
    course_excel = BooleanField("Excel - Office")
    course_git = BooleanField("Git and GitHub")
   
    def validate_email(self, email):
        if current_user.email != email.data:
            email_exist = User.query.filter_by(email=email.data).first()
            if email_exist:
                raise ValidationError("E-mail already exist in Database. Use another e-mail")
            
    def validate_username(self, username):
        if current_user.username != username.data:
            username_exist = User.query.filter_by(username=username.data).first()
            if username_exist:
                raise ValidationError("Username already exist in Database.Use another Username")


class FormCreatePost(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired(), Length(2,150)] )
    body = TextAreaField("Your post here:")
    button_create_post = SubmitField("Create Post")