from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String


class CourseType(Base):
    __tablename__ = "course_type"

    id_course_type = Column('id', primary_key=True)
    description_course_type = Column('description')
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class UserType(Base):
    __tablename__ = "user_type"

    name_user_type = Column('name')
    id_user_type = Column('id', primary_key=True)
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

