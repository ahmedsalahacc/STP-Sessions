from flask import Flask, render_template, redirect, url_for
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
    return render_template('index.html')

# -- User routes


@app.route('/users/register')
def reg_page():
    return render_template('registration.html')


@app.route('/users', methods=['POST'])
def add_user():
    pass


@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users.html')


@app.route('/users', methods=['DELETE'])
def delete_users():
    pass


@app.route('/users', methods=['PUT'])
def update_users():
    pass

# -- Jokes routes


@app.route('/jokes/add', methods=['GET'])
def add_jokes_page():
    return render_template('addJokeForm.html')


@app.route('/jokes', methods=['POST'])
def add_joke():
    pass


#### Assignments ####
# @TODO Assignment
'''
    NOTE Advanced topic ⚠: Databases
    ----
    It will require you to dig a little deeper in database so, search
    for the following
    * Database referrentials
    * Foreign keys in flask sqlalchemy
'''
# @app.route('/<userid>/jokes', methods=['GET'])
# def get_user_jokes():
#     pass

# @app.route('/<userid>/jokes', methods=['DELETE'])
# def delete_joke():
#     pass

# @app.route('/<userid>/jokes', methods=['PUT'])
# def update_joke():
#     pass


##### BONUS SECTION #####

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
