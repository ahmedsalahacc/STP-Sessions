from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# intiialize app, db -> app db


def create_flask_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db22.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    return app, db


app, db = create_flask_app()
