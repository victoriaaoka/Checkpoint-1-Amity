from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Person(Base):
    __tablename__ = "People"
    id = Column(Integer, autoincrement=True)
    person_id = Column(String, primary_key= True)
    person_name = Column(String)
    person_type = Column(String)
    wants_accommodation = Column(String)
    room_allocated = Column(String)


class Room(Base):
    __tablename__ = "Rooms"
    id = Column(Integer, primary_key= True, autoincrement=True)
    room_name = Column(String)
    room_type = Column(String)
    occupants = Column(String)


engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)