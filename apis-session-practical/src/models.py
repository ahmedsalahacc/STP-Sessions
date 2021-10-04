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
        '''
        class method that inserts task to database
        ----------
        args:
            task - string
        '''
        try:
            todo = Todo(task=task)
            db.session.add(todo)
            db.session.commit()
            print("successfully inserted item into database")
        except:
            print("Error occured while inserting to database")

    @classmethod
    def update(cls, id, new_task):
        '''
        class method that updates a specific record in the database
        ----------
        args:
            id - int
            task - string
        '''
        try:
            query = cls.query.filter_by(id=id).first()
            query.task = new_task
            query.dateCreated = datetime.datetime.utcnow()
            db.session.commit()
            print(f"Successfully updated database")
        except:
            print("Error occured while updating database")

    @classmethod
    def delete(cls, id):
        '''
        class method that deletes a specific record in the database
        ----------
        args:
            id - int
        '''
        try:
            query = cls.query.filter_by(id=id).first()
            db.session.delete(query)
            db.session.commit()
            print(f"Successfully deleted item from database")
        except:
            print("Error occured while deleting from database")

    @classmethod
    def get(cls, id):
        '''
        class method that gets a specific record from database
        ----------
        args:
            id - int
        '''
        try:
            todo = cls.query.filter_by(id=id).first()
            print("Success retreiving data from database")
        except:
            print("Error occured while retrieving from database")
        return todo

    @classmethod
    def getAll(cls):
        '''
        class method that gets all records in database and sort them
        by date in descending order
        ----------
        '''
        try:
            todos = cls.query.order_by(cls.dateCreated.desc()).all()
            print("Success retreiving data from database")
        except:
            print("Error occured while retrieving from database")
        return todos
