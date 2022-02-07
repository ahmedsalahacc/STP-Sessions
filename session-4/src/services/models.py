from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import random


##### Init class #####
db = SQLAlchemy()


##### Models #####


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    jokes = db.relationship('Joke', backref='author', lazy=True)

    def __init__(self, username, name, password):
        self.username = username
        self.password = password
        self.name = name

    def __repr__(self):
        return f"<User({self.id}, #{self.username}, {self.name}> "

    @classmethod
    def insert(self, name, username, password):
        user = User(name=name, username=username, password=password)

        # add to db and commit
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update(self, id, name, username, password):
        query = self.query.filter_by(id=id).first()

        # update values
        query.name = name
        query.username = username
        query.password = password

        # commit changes to db
        db.session.commit()

    @classmethod
    def getUser(self, id):
        query = self.query.filter_by(id=id).first()
        return query

    @classmethod
    def getByUsername(self, username):
        query = self.query.filter_by(username=username).first()
        return query

    @classmethod
    def getUserJokes(self, username):
        query = self.query.filter_by(username=username).first()
        jokes = query.jokes

        return jokes

    @classmethod
    def getUserId(self, username):
        id = self.query.filter_by(username=username).first().id
        return id


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    joke = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, joke, user_id):
        self.joke = joke
        self.user_id = user_id

    def __repr__(self):
        return f"<User({self.user}, {self.joke[:20]}...> "

    @classmethod
    def insert(self, joke, user_id):
        joke = Joke(joke=joke, user_id=user_id)

        # add to db and commit
        db.session.add(joke)
        db.session.commit()

    @classmethod
    def update(self, id, joke):
        query = self.query.get(id)

        # update values in query
        query.joke = joke
        query.date_created = datetime.utcnow()

        # commit the updates
        db.session.commit()

    @classmethod
    def getRandomJoke(self):
        # get all jokes
        query = self.query.all()
        sz = len(query)

        # get random idx
        idx = random.randint(0, sz-1)
        return query[idx]

    @classmethod
    def delete(self, id):
        query = self.query.get(id)
        db.session.delete(query)
        db.session.commit()

    @classmethod
    def get(self, id):
        query = self.query.get(id)

        return query
