from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo 

class FormCreateAccount(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()] )
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    password = PasswordField("Password: ", validators=[DataRequired(), Length(6,20)] )
    confirmation = PasswordField("Password Confirmation: ", validators=[DataRequired(), EqualTo('password')] )
    button_submit_create_account = SubmitField("Create Account")

class FromLogin(FlaskForm):
    email = StringField("E-mail: ", validators=[DataRequired(), Email()] )
    password = PasswordField("Password: ", validators=[DataRequired(), Length(6,20)] )
    button_submit_login = SubmitField("Login")

