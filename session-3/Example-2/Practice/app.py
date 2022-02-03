from flask import jsonify, request
from extensions import app, db
from models import Student

# get students


@app.route('/', methods=['GET'])
def get_all_students():
    students = Student.query.all()

    res = []
    for student in students:
        res.append({
            'id': student.id,
            'name': student.name,
            'address': student.address,
            'gpa': student.gpa
        })

    return jsonify(res)

# create student


@app.route('/', methods=['POST'])
def create_student():
    name = request.form.get("name")
    address = request.form.get("address")
    gpa = request.form.get("gpa")

    student = Student(name, address, gpa)

    db.session.add(student)
    db.session.commit()
    return {"success": 200}
# update student


@app.route('/<int:id>', methods=['PUT'])
def update_student(id):
    name = request.form.get("name")
    address = request.form.get("address")
    gpa = request.form.get("gpa")

    student = Student.query.get(id)
    student.name = name
    student.address = address
    student.gpa = gpa

    db.session.commit()

    return {"success": 200}


# delete student


@app.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()

    return {"success": 200}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
