from flask import jsonify, request
from extensions import app, db
from models import Student

# controllers


@app.route("/", methods=['GET'])
def index():
    students = Student.query.all()
    res = []

    for student in students:
        res.append(
            {'id': student.id,
             'name': student.name,
             'address': student.address,
             'gpa': student.gpa})

    return jsonify(res)


@app.route('/student', methods=['POST'])
def add_student():
    name = request.form.get("name")
    address = request.form.get('address')
    gpa = request.form.get("gpa")

    student = Student(name, address, gpa)
    db.session.add(student)
    db.session.commit()
    return jsonify({'status': 200}), 200


@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    # retrieve edits
    new_name = request.form.get("name")
    new_address = request.form.get('address')
    new_gpa = request.form.get("gpa")

    # retrieve student
    student = Student.query.get(id)

    # apply edits
    student.name = new_name
    student.address = new_address
    student.gpa = new_gpa

    # commit changes
    db.session.commit()

    return jsonify({'status': 200}), 200


@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()

    return jsonify({'status': 200}), 200


# flask app running
if __name__ == "__main__":
    app.run(debug=True, port=5000)
