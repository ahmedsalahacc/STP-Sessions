from extensions import db


# table student


class Student(db.Model):
    # @TODO
    # students ID primary key and unique
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # students name NOT NULL
    name = db.Column(db.String(200), nullable=False)
    # students address NOT NULL
    address = db.Column(db.String(200), nullable=False)
    # students gpa  NULL
    gpa = db.Column(db.Float, nullable=True)

    def __init__(self, name, address, gpa=None):
        self.name = name
        self.address = address
        self.gpa = gpa


if __name__ == "__main__":
    db.create_all()
