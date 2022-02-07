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
        '''
        inserts user to the database

        Parameters:
        -----------
        name: string
        username: string
        password: string
        '''
        user = User(name=name, username=username, password=password)

        # add to db and commit
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update(self, id, name, username, password):
        '''
        updates user record with id=id with the new record

        Parameters
        ----------
        id: int
        name: string
        username: string
        password: string
        '''
        query = self.query.filter_by(id=id).first()

        # update values
        query.name = name
        query.username = username
        query.password = password

        # commit changes to db
        db.session.commit()

    @classmethod
    def getUser(self, id):
        '''
        gets the user by id

        Parameters:
        -----------
        id: int

        Returns:
        -------
        query: user object
        '''
        query = self.query.filter_by(id=id).first()
        return query

    @classmethod
    def getByUsername(self, username):
        '''
        gets user by username

        Parameters:
        -----------
        username: string

        Returns:
        --------
        query: user object
        '''
        query = self.query.filter_by(username=username).first()
        return query

    @classmethod
    def getUserJokes(self, username):
        '''
        gets jokes associated with username

        Parameters:
        ----------
        username: string

        Returns:
        --------
        jokes: list of joke objects
        '''
        query = self.query.filter_by(username=username).first()
        jokes = query.jokes

        return jokes

    @classmethod
    def getUserId(self, username):
        '''
        get id associated with the given username
        '''
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
        '''
        insert joke into db

        Parameters:
        -----------
        joke: string
        user_id: int
        '''
        joke = Joke(joke=joke, user_id=user_id)

        # add to db and commit
        db.session.add(joke)
        db.session.commit()

    @classmethod
    def update(self, id, joke):
        '''
        updates existing joke record

        Parameters:
        -----------
        id: int
        joke: string
        '''
        query = self.query.get(id)

        # update values in query
        query.joke = joke
        query.date_created = datetime.utcnow()

        # commit the updates
        db.session.commit()

    @classmethod
    def getRandomJoke(self):
        '''
        gets a random joke from the database

        Returns
        -------
        joke: string
        '''
        # get all jokes
        query = self.query.all()
        sz = len(query)

        # get random idx
        idx = random.randint(0, sz-1)
        return query[idx]

    @classmethod
    def delete(self, id):
        '''
        deletes joke with id=id from the database

        Parameters:
        ----------
        id: integer
        '''
        query = self.query.get(id)
        db.session.delete(query)
        db.session.commit()

    @classmethod
    def get(self, id):
        '''
        gets joke with id=id

        Parameters:
        -----------
        id: Integer
        '''
        query = self.query.get(id)

        return query
