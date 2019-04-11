from peewee import *

database = SqliteDatabase('calls.sqlite3', **{})

class UnknownField(object):
    def __initt__(selfself, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Call(BaseModel):
    callresult = IntegerField(column_name='CallResult', null=True)
    calltimestart = DateTimeField(column_name='CallTimeStart', null=True)
    calltimestop = DateTimeField(column_name='CallTimeStop', null=True)
    connectionchainid = TextField(column_name='ConnectionChainId', null=True)
    id = TextField(column_name='Id', null=True)
    taskid = TextField(column_name='TaskId', null=True)

    class Meta:
        table_name = 'calls'
        primary_key = False

    def to_dict(self):
        return {
            'id' : self.id,
            'calltimestart' : self.calltimestart,
            'calltimestop' : self.calltimestop,
            'callresult' : self.callresult,
            'connectionchainid' : self.connectionchainid,
            'taskid' : self.taskid
        }