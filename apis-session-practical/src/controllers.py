from flask import Blueprint, render_template, url_for, redirect, request
from src.models import Todo

#-- init --#
main = Blueprint('main', __name__, )

#-- endpoints --#

# @TODO make an endpoint to display all todos
@main.route('/', methods=['GET'])
def getIndex():
    try:
        # retrieve all items from database
        tasks = Todo.getAll()
    except:
        return 500

    return render_template('index.html', tasks=tasks)

# @TODO make save a todo to database
@main.route('/', methods=['POST'])
def postIndex():
    try:
        # get the task from request form dict
        task = request.form.get('task')
        # insert item to database
        Todo.insert(task)
    except:
        return 500

    return redirect('/')

# @TODO make endpoint to get single item
@main.route('/edit/<id>', methods=['GET'])
def getEdit(id):
    try:
        # get item from database by id
        task = Todo.get(id)
    except:
        return 500

    return render_template('edit.html', task=task)


# @TODO make an endpoint edit todo
@main.route('/edit/<id>', methods=['POST'])
def putEdit(id):
    try:
        # get the new task from request form dict
        task = request.form.get('task')
        # update database of specific record
        Todo.update(id, task)
    except:
        return 500

    return redirect('/')


# @TODO make an endpoint to delete todo
@main.route('/delete/<id>', methods=['GET'])
def deleteTask(id):
    try:
        # delete specific record by id
        Todo.delete(id)
    except:
        return 500

    return redirect('/')
