from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime # small letters only

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    email = Column(String(50), unique=True)
    password = Column(String(64))
    created_at = Column(DateTime, default=datetime.now)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    message = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    oath = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    message_id = Column(Integer, ForeignKey("messages.id"))
    created_at = Column(DateTime, default=datetime.now)

# utility function
def get_db():
    engine = create_engine("sqlite:///example.db")
    return sessionmaker(bind=engine)()

def add_to_db(obj):
    db = get_db()
    db.add(obj)
    db.commit()
    db.close()

# 👇 double underscore h niche likha sab jagah pe 
if __name__ == "__main__":
    engine = create_engine("sqlite:///example.db")
    Base.metadata.create_all(engine)