from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String


class CourseType(Base):
    __tablename__ = "course_type"

    description_course_type = Column('column on database')
    id_course_type = Column('column on database', primary_key=True)
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class UserType(Base):
    __tablename__ = "user_type"

    name_user_type = Column('column on database')
    id_user_type = Column('column on database', primary_key=True)
    

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

