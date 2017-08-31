from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "course_type"

    description_course_type = Column('description')
    id_course_type = Column('id', primary_key=True)
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class Category(Base):
    __tablename__ = "user_type"

    name_user_type = Column('name')
    id_user_type = Column('id', primary_key=True)
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

