from extensions import db


# table student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(240), nullable=False)
    gpa = db.Column(db.Float, nullable=True)

    def __init__(self, name, address, gpa=None):
        self.name = name
        self.address = address
        self.gpa = gpa


if __name__ == "__main__":
    db.create_all()
