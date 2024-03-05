from myblog import database, app
from myblog.models import User, Post

with app.app_context():
    database.drop_all()
    database.create_all()
