from flask import Blueprint, render_template, url_for, redirect, request
from src.models import Todo

#-- init --#
main = Blueprint('main', __name__, )

#-- endpoints --#

# @TODO make an endpoint to display all todos
@main.route('/home', methods=['GET'])
def getIndex():
    try:
        pass
        # retrieve all items from database

    except:
        return 500

    return render_template('index.html', tasks=None)

# @TODO make save a todo to database
@main.route('/', methods=['POST'])
def postIndex():
    try:
        pass
        # get the task from request form dict
        # insert item to database

    except:
        return 500

    return redirect('/')

# @TODO make endpoint to get single item
@main.route('/edit/<id>', methods=['GET'])
def getEdit(id):
    try:
        pass
        # get item from database by id

    except:
        return 500

    return render_template('edit.html', task=None)


# @TODO make an endpoint edit todo
@main.route('/edit/<id>', methods=['POST'])
def putEdit(id):
    try:
        pass
        # get the new task from request form dict

        # update database of specific record

    except:
        return 500

    return redirect('/')


# @TODO make an endpoint to delete todo
@main.route('/delete/<id>', methods=['GET'])
def deleteTask(id):
    try:
        pass
        # delete specific record by id

    except:
        return 500

    return redirect('/')


@main.errorhandler(500)
def handle_500(err):
    return {
        'err', err
    }, 500
