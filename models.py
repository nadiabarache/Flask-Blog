from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///dbMyBlog.db', echo=True)
Base = declarative_base()

class User(Base):
    """"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password



class Post(Base):
    """"""
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    description = Column(Text)
    body = Column(UnicodeText)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', backref=backref('posts'))

    def __init__(self, title, description, body, category_id):
        """"""
        self.title = title
        self.description = description
        self.body = body
        self.category_id = category_id

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Info(Base):
    """"""
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        """"""
        self.name = name


# create tables
Base.metadata.create_all(engine)
