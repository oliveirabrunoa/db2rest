from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#Obtem a URL do Banco de Dados a partir da variável de ambiente DATABASE_URL
engine = create_engine(os.environ['DATABASE_URL'], convert_unicode=True)

#Criação de uma fábrica de sessões de acesso ao Banco de dados, realizando
#bind com a engine criada. Cada sessão do banco tem um escopo único.
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

#A criação do objeto MetaData, que realiza bind com a engine, fornce um objeto
# que permite consultar informações sobre a base de dados, nomes das tabelas,
#nomes dos atributos e tipos definidos.
meta = MetaData()
meta.reflect(bind=engine)

#declarative_base é uma class fornecida pelo SQLAlchemy que permite criar modelos de dados
# que são interpretados pelo framework. Isto é, permite criar uma classe que será a representação
# de uma tabela no banco de dados em linguagem Python.
Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.bind = engine
