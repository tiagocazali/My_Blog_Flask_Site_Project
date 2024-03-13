from myblog import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    photo_profile = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='author', lazy=True)  
    courses = database.Column(database.String, nullable=False, default='None')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    create_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    user_ID = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)