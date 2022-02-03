from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##### Models #####


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, username, name):
        self.username = username
        self.name = name

# class Joke(db.Model):
#     def __init__(self):
#         pass
