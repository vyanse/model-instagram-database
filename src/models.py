import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(15), unique=True)
    password = Column(String(20), unique=True)
    email = Column(String(250), unique=True)
    followers = relationship("Follower")
    comments = relationship("Comment")
    posts = relationship("Post")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    comments = relationship("comment")
    medias = relationship("media")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=False)
    user_id= Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))

class Media(Base):
    __tablename__ = "media"
    id=Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    url = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = "follower"
    id=Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user_from_id = Column(Integer, ForeignKey("user.id"), nullable=True)



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e