from flask import Flask
from flask_cors import CORS

from services.models import db

##### CONSTANTS #####
PORT = 5000
DB_FILENAME = 'dbfile.db'
INIT_DB = True  # to create db file


def create_app():
    '''
    Creates a flask app

    Returns
    -------
    (app, db): tuple
        has the app object and the db object
    '''
    # create flask app
    app = Flask(__name__)

    # create database extension
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_FILENAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # create flask cors extension
    CORS(app)

    return app, db


# create flask app
app, db = create_app()

# create db file on demand
if INIT_DB:
    db.create_all(app=app)

##### ROUTES #####

# -- display pages


@app.route('/')
def index():
    '''
    route to the index page (/)
    '''
    return "hello"

# -- User routes


@app.route('/users/register')
def reg_page():
    pass


@app.route('/users', methods=['POST'])
def add_user():
    pass


@app.route('/users', methods=['GET'])
def get_users():
    pass


@app.route('/users', methods=['DELETE'])
def delete_users():
    pass


@app.route('/users', methods=['DELETE'])
def update_users():
    pass

# -- Jokes routes


@app.route('/jokes', method=['GET'])
def pick_joke():
    pass


@app.route('/jokes', method=['POST'])
def add_joke():
    pass


@app.route('/jokes', method=['DELETE'])
def delete_joke():
    pass


@app.route('/jokes', method=['PUT'])
def update_joke():
    pass


##### BONUS SECTION #####
# @TODO get the jokes associated with a specific user
'''
    NOTE Advanced topic ⚠: Databases
    ----
    It will require you to dig a little deeper in database so search
    for the following
    * Database referrentials
    * Foreign keys in flask sqlalchemy
'''

# @TODO allow jokes review from a specific user authority
'''
    NOTE Advanced topic ⚠: Software Engineering
    ----
    Requires you to add a state section to the joke and track its state ,
    if the state of the joke is new then it must be in the review list that will
    appear in the admin's page to allow the jokes to be listed if not abusive
'''

# @TODO add like and dislike button to the joke
'''
    NOTE Advanced topic ⚠: Software Engineering - UI
    ----
    Allow anyone to like/dislike the joke and if the joke's like-dislikes ratio hit a 
    predetermined threshold then ban it from being displayed (needs you to add
    a state column to the joke db model and check the likes-dislikes ratio on each
    new dislike)
'''

#### RUN FLASK APP#####
if __name__ == "__main__":
    app.run(debug=True, port=PORT)
