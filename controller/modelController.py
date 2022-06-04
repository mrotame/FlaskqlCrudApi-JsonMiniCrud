from sqlalchemy import false
from sql.Sqldb import session

class ModelController():
    table = None
    session = session
    def __init__(self, table):
        self.table = table

    def createOne(self, data):
        newRow = self.table(**data)
        session.add(newRow)
        session.commit()

    def readOne(self, conditions):
        return session.query(self.table).filter_by(**conditions).first()

    def readMany(self,conditions):
        return session.query(self.table).filter_by(**conditions)

    def updateOne(self, conditions, newInfo):
        row = self.readOne(conditions)
        if (row is None):
            return False
        for key, value in newInfo.items():
            setattr(row,key,value)
        session.commit()
        return True

    def delete(self, conditions):
        rowToDelete = self.readOne(conditions)
        if (rowToDelete is None):
            return False
        session.delete(rowToDelete)
        session.commit()
        return True

