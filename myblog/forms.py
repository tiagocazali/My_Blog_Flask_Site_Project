from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from myblog.models import User

class FormCreateAccount(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()] )
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    password = PasswordField("Password: ", validators=[DataRequired(), Length(6,20)] )
    confirmation = PasswordField("Password Confirmation: ", validators=[DataRequired(), EqualTo('password')] )
    button_submit_create_account = SubmitField("Create Account")

    def validate_username(self, username):
        username_exist = User.query.filter_by(username=username.data).first()
        if username_exist:
            raise ValidationError("Username already exist in Database.Use another e-mail or Log in")
    
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
    button_save_changes = SubmitField("Save Changes")
