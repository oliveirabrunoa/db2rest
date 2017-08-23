from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(os.environ['DATABASE_URL'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
meta = MetaData()
meta.reflect(bind=engine)

Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.bind = engine
