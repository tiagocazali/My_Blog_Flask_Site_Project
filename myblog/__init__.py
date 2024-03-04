from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'cdcb1a8087026933fca6ceae9fa71136'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///teste.db"

database = SQLAlchemy(app)


from myblog import routes
