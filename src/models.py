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
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique= True)
    follower = relationship("Follower")
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    
class Comment(Base):
    __tablename__="comment"
    id = Column(Integer,primary_key=True)
    text = Column(String(250), nullable=False)
    user_id=Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__='follower'
    id = Column(Integer, primary_key=True)
    follower = relationship(User)
    following_id = Column(Integer, ForeignKey('user.id'))
    following = relationship (User)
    user_id = Column(Integer, ForeignKey('user.id'))


render_er(Base, 'diagram.png')