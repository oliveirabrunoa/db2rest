from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "course_type"

    id_course_type = Column('id' , primary_key=True)
    description_course_type = Column('description' )
    

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Category(Base):
    __tablename__ = "user_type"

    id_user_type = Column('id' , primary_key=True)
    name_user_type = Column('name' )
    

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

