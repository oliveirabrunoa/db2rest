from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String

#Models que serão gerados dinamicamente

class BaseClass(Base):
    __tablename__ = 'course_type'
    __table_args__ = ({'autoload':True})

    #rename atributtes
    description_ = Column('description')

    def __init__(self, id, description, *args):
        self.id = id
        self.description_ = description
