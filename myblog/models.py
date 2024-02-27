from myblog import database
from datetime import datetime

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    photo_profile = database.Column(database.String, default="default.jpg")
    courses = database.Column(database.String, nullable=False, default="No Courses")
    posts = database.relationship("Post", backref="autor", lazy=True)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_ID = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    create_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

