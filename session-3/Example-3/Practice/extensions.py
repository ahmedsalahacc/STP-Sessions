from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# intiialize app, db -> app db


def create_flask_app():
    app = Flask(__name__)
    CORS(app)
    # @TODO SQL ALchemy init SQLALCHEMY_DATABASE_URI and SQLALCHEMY_TRACK_MODIFICATIONS

    db = SQLAlchemy(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app, db


app, db = create_flask_app()
