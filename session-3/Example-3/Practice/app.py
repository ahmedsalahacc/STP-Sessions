from flask import request
from extensions import app, db
from models import Student

# get students


@app.route('/', methods=['GET'])
def get_all_students():
    # @TODO get all students
    students = Student.query.all()
    res = []

    for student in students:
        res.append(
            {'id': student.id,
             'name': student.name,
             'address': student.address,
             'gpa': student.gpa})

    return {
        'status': 200,
        'message': 'success',
        'content':  res
    }

# create student


@app.route('/', methods=['POST'])
def create_student():
    # @TODO
    # get student name
    name = request.form.get('name')
    address = request.form.get('address')
    gpa = request.form.get('gpa')

    # get student address
    # get student gpa

    # @TODO add student to database
    student = Student(name=name, address=address, gpa=gpa)

    db.session.add(student)
    db.session.commit()

    return {
        'status': 200,
        'message': 'ok'
    }
# update student


@app.route('/<int:id>', methods=['PUT'])
def update_student(id):
    name = request.form.get('name')
    address = request.form.get('address')
    gpa = request.form.get('gpa')

    # @TODO edit student's data
    student = Student.query.get(id)

    student.name = name
    student.address = address
    student.gpa = gpa

    db.session.commit()

    return {
        'status': 200,
        'message': 'ok'
    }


@app.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    # @TODO delete student's info

    student = Student.query.get(id)

    db.session.delete(student)
    db.session.commit()

    return {
        'status': 200,
        'message': 'ok balala'
    }


if __name__ == "__main__":
    app.run(port=5000, debug=True)
