from sqlalchemy import create_engine
engine = create_engine("sqlite://")

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, Date

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)

Base.metadata.create_all(engine)

message = Message(message="This is my first ORM object")

# for save the object you need to create a session object

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(message)
session.commit()

query = session.query(Message)
instance = query.first()
print(instance.message)

# The session object is similar that context at .Net architecture

# you can define a transaction
with engine.connect() as conn:
    trans = conn.begin()
    try:        
        conn.execute("Select * from messages")
        trans.commit()
    except:
        trans.rollback()
        raise

from datetime import date

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    birthday = Column(Date)

Base.metadata.create_all(engine)

user_one = User(name="Richard",birthday=date(1995, 3, 3))
user_two = User(name="Carol",birthday=date(1992, 2, 3))
user_tree = User(name="Henrry",birthday=date(1983, 6, 12))

session.add(user_one)
session.add(user_two)
session.add(user_tree)
session.commit()

# filter users use the word filter
user_older = session.query(User).filter(User.birthday < date(1984,1,1))

# to retrive all the item in a list use all()
reslist = user_older.all()
# to retrive the count use count()
count = user_older.count()
# to retrive the first element use first()
first = user_older.order_by(User.birthday).first()
# to retrive one file use one()
one_file = session.query(User).filter(User.name == 'Richard').one()
# if the filed dont retrive a value use one_or_one()
one_file_none = session.query(User).filter(User.name=="Joseph").one_or_none()





