from extensions import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(500), nullable=False)
    gpa = db.Column(db.Float, nullable=False)

    def __init__(self, name, address, gpa):
        self.name = name
        self.address = address
        self.gpa = gpa


# run to create db file
if __name__ == "__main__":
    # MUST BE AFTER THE CLASSES
    db.create_all()
