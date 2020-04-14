from sqlalchemy import create_engine

engine = create_engine('sqlite://')

from sqlalchemy import Column, Integer, Text, MetaData, Table

metadata = MetaData()
m = Table(
    'messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('message', Text),
)

m.create(bind=engine)

insert_message = m.insert().values(message='Welcome to SQLAlchemy!')
engine.execute(insert_message)

insert_message2 = m.insert().values(message='In this Tutotial you learn to use SQLAlchemy!')
engine.execute(insert_message2)

from sqlalchemy import select

stmt = select([m.c.message])
message, = engine.execute(stmt).fetchone()
print(message)

stmt = select([m.c.message])
message2 = engine.execute(stmt).fetchall()
for m in message2:
    print(message2)






