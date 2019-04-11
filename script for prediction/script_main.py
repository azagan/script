from peewee import *
from datetime import *
import pandas
from call_model import Call

db = SqliteDatabase('calls.sqlite3')

db.connect()

callsMonth = Call.select(fn.Count(Call.id).alias('quantity')).group_by(fn.strftime('%Y-%m', Call.calltimestart))
for call in callsMonth:
    print(call.quantity)


print('type of callsMonth : ', type(callsMonth))
print(callsMonth)
