from flask import Flask, render_template, url_for
from forms import FormLogin, FormCreateAccount

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cdcb1a8087026933fca6ceae9fa71136'

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
    return render_template("login.html", form_createAccount=form_createAccount, form_login=form_login)



if __name__ == "__main__":
    app.run(debug=True)