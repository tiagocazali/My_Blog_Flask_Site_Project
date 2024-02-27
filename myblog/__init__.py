from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'cdcb1a8087026933fca6ceae9fa71136'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

database = SQLAlchemy(app)

with app.app_context():
    database.create_all()

from myblog import routes
