from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Call(Base):
    __tablename__ = 'calls'

    id = Column(String, primary_key=True)
    connectionChaiId = Column(String)
    callTimeStart = Column(Date)
    callTimeStop = Column(Date)
    taskId = Column(String)

    def __repr__(self):
        return (f"<Id: {self.id}, " +
                f"CallTimeStart: {self.callTimeStart}," +
                f"CallTimeStop: {self.callTimeStop}," +
                f"CallChainId: {self.connectionChaiId}," +
                f"TaskId: {self.taskId}>")