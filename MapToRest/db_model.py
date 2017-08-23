from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String


class CourseTypeBase(Base):
    __tablename__ = "course_type"
    
    id = Column('id', primary_key=True)
    description = Column('description')


    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class UserTypeBase(Base):
    __tablename__ = "user_type"

    name = Column('description')
    id = Column('id', primary_key=True)


    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
