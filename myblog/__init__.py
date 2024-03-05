from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'cdcb1a8087026933fca6ceae9fa71136'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from myblog import routes
