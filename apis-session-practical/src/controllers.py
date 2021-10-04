from flask import Blueprint, render_template, url_for, redirect, request
from src.models import Todo

import os


main = Blueprint('main', __name__, )
# print('template folder', main.template_folder)

# @TODO make an endpoint to display all todos
@main.route('/', methods=['GET'])
def getIndex():
    # extract the task from parameters
    tasks = Todo.getAll()

    return render_template('index.html', tasks=tasks)

# @TODO make save a todo to database
@main.route('/', methods=['POST'])
def postIndex():
    task = request.form.get('task')
    task = task.lstrip()
    print(task)
    Todo.insert(task)

    return redirect('/')


@main.route('/edit/<id>', methods=['GET'])
def getEdit(id):
    task = Todo.get(id)

    return render_template('edit.html', task=task)


@main.route('/edit/<id>', methods=['POST'])
def putEdit(id):
    task = request.form.get('task').rstrip().lstrip()

    Todo.update(id, task)

    return redirect('/')
# @TODO make an endpoint edit todo


@main.route('/delete/<id>', methods=['GET'])
def deleteTask(id):
    Todo.delete(id)

    return redirect('/')
# @TODO make an endpoint to delete todo
