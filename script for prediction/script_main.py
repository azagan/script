from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from call_model import Call

engine = create_engine('sqlite:///calls.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

calls = session.query(func.count(Call.callTimeStart), Call.callTimeStart)\
    .group_by(func.strftime('%Y-%m-%d', Call.callTimeStart))\
    .all()

for call in calls:
    print(call)