from dbconfig import Base
from sqlalchemy import Column, Integer, String

#Models que serão gerados dinamicamente

class BaseClass(Base):
    __tablename__ = 'course_type'
    # __table_args__ = ({'autoload':True})
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, id, description, *args):
        self.id = id
        self.description = description
