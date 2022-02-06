from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##### Models #####


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, username, name):
        self.username = username
        self.name = name

    def insert(self, name, username, password):
        pass

    def update(self, id, name, username, password):
        pass

    def getUser(self, id):
        pass

    def getAllUsers(self):
        pass


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    joke = db.Column(db.String(256), unique=True, nullable=False)
    #  datetime = None

    def __init__(self, joke):
        self.joke = joke

    def insert(self, joke):
        pass

    def update(self, id, joke):
        pass

    def getRandomJoke(self):
        pass
