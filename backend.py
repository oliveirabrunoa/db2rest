from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


db = "dsd"

engine = create_engine('sqlite:///test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

Base.metadata.create_all(bind=engine)

class BaseClass(Base):
    __tablename__ = 'course_type'
    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)

    def __init__(self, description=None):
        self.description = description

    def teste(self):
        return "teste"

    def __repr__(self):
        return self.description


# class CourseTypeNova(CourseType):
#     def __init__(self, description=None, attTeste=None):
#         CourseType.__init__(self, description)
#         self.attTeste = attTeste



# if __name__ == '__main__':
    # c = CourseTypeNova('admin','novo atributo')
    # print(c.attTeste)
    # db_session.add(c)
    # db_session.commit()

    # all = CourseTypeNova.query.all()
    # print(all[0].teste())

    # >>> User.query.all()
    # [<User u'admin'>]
    # >>> User.query.filter(User.name == 'admin').first()
