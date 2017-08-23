from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


db = "teste"

engine = create_engine('sqlite:///test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.bind = engine
# Base.metadata.create_all(bind=engine)

class BaseClass(Base):
    __tablename__ = 'course_type'
    # __table_args__ = ({'autoload':True})
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, id, description, *args):
        self.id = id
        self.description = description
