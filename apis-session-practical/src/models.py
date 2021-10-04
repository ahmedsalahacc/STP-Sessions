from src.extensions import db
import datetime


# models


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False)
    task = db.Column(db.String, nullable=False)
    dateCreated = db.Column(db.DateTime(), nullable=False,
                            default=datetime.datetime.utcnow)

    @classmethod
    def __repr__(cls):
        return f"Todo <{cls.id} {cls.dateCreated}"

    @classmethod
    def insert(cls, task):
        todo = Todo(task=task)
        db.session.add(todo)
        db.session.commit()
        print("successfully inserted")

    @classmethod
    def update(cls, id, new_task):
        query = cls.query.filter_by(id=id).first()
        query.task = new_task
        query.dateCreated = datetime.datetime.utcnow()
        db.session.commit()
        print(f"Successfully updated {cls}")

    @classmethod
    def delete(cls, id):
        query = cls.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        print(f"Successfully deleted")

    @classmethod
    def get(cls, id):
        todo = cls.query.filter_by(id=id).first()
        return todo

    @classmethod
    def getAll(cls):
        todos = cls.query.order_by(cls.dateCreated.desc()).all()
        return todos
