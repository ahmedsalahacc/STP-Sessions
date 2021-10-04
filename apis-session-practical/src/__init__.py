from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.controllers import main
from src.extensions import db, cors
import os

# constants
INIT_DB = False


def create_app():
    '''
    create flask app
    '''
    # get the base directory
    basedir = os.getcwd()
    repo_path = os.path.abspath(os.path.dirname(__name__))
    template_dir = os.path.join(
        repo_path, 'views', 'html'
    )

    # init flask app
    app = Flask(__name__, template_folder=template_dir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/database.db'

    # manage extensions
    db.init_app(app)

    if INIT_DB:
        with app.app_context():
            db.create_all()

    cors.init_app(app)
    app.register_blueprint(main)

    return app


# create flask app
app = create_app()
