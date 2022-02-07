from flask import Flask, render_template, redirect, url_for, session, request
from flask_cors import CORS

from datetime import timedelta

from services.models import db, User, Joke

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
    app.secret_key = 'asdfads234egrg'
    app.permanent_session_lifetime = timedelta(minutes=5)

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

# @TODO


@app.route('/')
def index():
    '''
    route to the index page (/)
    '''
    joke = session.get('joke_content')
    return render_template('index.html', joke=joke)


@app.route('/genjoke')
def getRandomJoke():
    '''
    route to the index page (/)
    '''
    joke = Joke.getRandomJoke()
    content = joke.joke
    session['joke_content'] = content
    return redirect('/')

# -- User routes


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


@app.route('/users/register')
def get_reg_page():
    '''
    Method: GET
    Route: /users/register
    -----------
    renders the registration page
    '''
    return render_template('registration.html')


@app.route('/users/register', methods=['POST'])
def post_reg_page():
    '''
    Method: POST
    Route: /users/register
    -----------
    Posts the data to register the user
    '''
    # retrieve input
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')

    # input to database
    print(name, username, password)
    try:
        User.insert(name=name, username=username, password=password)
    except:
        return redirect('/users/register')

    # clear current session
    session.clear()

    # redirect to index page
    return redirect('/')


@app.route('/users/login', methods=['GET'])
def login_get():
    '''
    Method: GET
    Route: /users/login
    -----------
    renders the login page
    '''
    return render_template("signin.html")


@app.route('/users/login', methods=['POST'])
def login_post():
    '''
    Method: POST
    Route: /users/login
    -----------
    Authenticates the user allow passage if registered
    '''
    username = request.form.get('username')
    password = request.form.get('password')

    # validate
    query = User.getByUsername(username)
    if query == None or query.password != password:
        # @TODO return a proper failure message
        return redirect('/users/login')

    # save session
    print("LOGIN success")
    session.permanent = True
    session['username'] = username
    # redirect to my jokes
    return redirect('/user/jokes')


@app.route('/user/jokes', methods=['GET'])
def get_users():
    '''
    Method: GET
    Route: /user/jokes
    -----------
    Gets the jokes associated with the user
    '''
    # return render_template('userjokes.html')
    if "username" in session:
        username = session['username']
        # get jokes associated with username
        jokes = User.getUserJokes(username)
        # render the jokes page
        return render_template('userjokes.html', jokes=jokes)
    else:
        # user is not logged in --> redirect to login page
        return redirect('/users/login')

# -- Jokes routes


@app.route('/jokes', methods=['POST'])
def add_joke():
    '''
    Method: POST
    Route: /jokes
    -----------
    Adds a the joke to the database
    '''
    # check if user in session
    if "username" in session:
        username = session['username']
        joke = request.form.get('joke')

        # get user id
        id = User.getUserId(username)

        # insert joke
        Joke.insert(joke, id)
        return redirect('/user/jokes')
    else:
        # user is not logged in --> redirect to login page
        return redirect('/users/login')


@app.route('/jokes/<id>/edit', methods=['GET'])
def get_joke(id):
    '''
    Method: GET
    Route: /jokes/<id>
    -----------
    View the joke edit page
    '''
    joke = Joke.get(id).joke
    return render_template('editjoke.html', id=id, joke=joke)


@app.route('/jokes/<id>/edit', methods=['POST'])
def update_joke(id):
    '''
    Method: GET
    Route: /jokes/<id>
    -----------
    Updates the database record of the joke with the new records
    '''
    if "username" in session:
        updatedJoke = request.form.get('joke')
        Joke.update(id, updatedJoke)
        return redirect('/user/jokes')
    else:
        # user is not logged in --> redirect to login page
        return redirect('/users/login')


@app.route('/jokes/<id>/delete', methods=['GET'])
def delete_joke(id):
    '''
    Method: GET
    Route: /jokes/<id>
    -----------
    Updates the database record of the joke with the new records
    '''
    if "username" in session:
        username = session['username']
        # delete joke from database
        Joke.delete(id)
        return redirect('/user/jokes')

    else:
        # user is not logged in --> redirect to login page
        return redirect('/users/login')

#####################
#### Assignments ####
#####################


# @TODO Assignment
'''
    NOTE Advanced topic ⚠: Databases
    ----
    It will require you to dig a little deeper in database so, search
    for the following
    * Database referrentials
    * Foreign keys in flask sqlalchemy
'''
# --- Users can delete their account
# @app.route('/users/<id>', methods=['DELETE'])
# def delete_users(id):
#     pass

# --- Users can update their account
# @app.route('/users/<id>', methods=['PUT'])
# def update_users(id):
#     pass

# --- Use sessions to prompt user incase if Unauthorized
# --- Use sessions to prompt user incase if Registering with existing username

#########################
##### BONUS SECTION #####
#########################

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
