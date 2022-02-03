from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_flask_app():
    '''
    Creates flask app and db
    '''
    # initialize flask
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize db
    db = SQLAlchemy(app)

    return app, db


# initialize flask app and db
app, db = create_flask_app()
