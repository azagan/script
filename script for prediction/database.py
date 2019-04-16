from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from call_model import Call


class DataBase:
    def __init__(self, db):
        engine = create_engine(db, echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getAll(self):
        return self.session.all()


class CallsDataBase(DataBase):
    def __init__(self, db):
        super(CallsDataBase, self).__init__(db)

    def getCountGroupByDay(self):
        return self.session.query(Call.callTimeStart, func.count(Call.callTimeStart)) \
            .group_by(func.strftime('%Y-%m-%d', Call.callTimeStart)) \
            .all()
