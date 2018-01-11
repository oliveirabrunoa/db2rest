from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Postagem(Base):
    __tablename__ = "post"

    id_postagem = Column('id', primary_key=True)
    titulo = Column('title')
    data_postagem = Column('date')
    hora_postagem = Column('time')

    categoria_id = Column('category', Integer, ForeignKey('category.id'))
    categoria = relationship("Categoria", backref="postagens",lazy='joined')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Categoria(Base):
    __tablename__ = "category"

    id_categoria = Column('id', primary_key=True)
    descricao = Column('name')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
