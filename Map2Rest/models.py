from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Postagem(Base):
    __tablename__ = "post"

    id_postagem = Column('id', primary_key=True)
    titulo = Column('title')
    data_postagem = Column('date')
    hora_postagem = Column('time')

    ##Relationships##
    categoria_id = Column('category',Integer,ForeignKey('category.id'))
    categoria = relationship('Categoria',lazy='joined')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Categoria(Base):
    __tablename__ = "category"

    id_categoria = Column('id', primary_key=True)
    descricao = Column('name')

    ##Relationships##


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Livro(Base):
    __tablename__ = "books"

    id = Column('id', primary_key=True)
    titulo = Column('title')
    autor = Column('author')
    publicacao = Column('published_date')
    isbn = Column('isbn')

    ##Relationships##
    revisao = relationship('Revisao',lazy='joined')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Revisao(Base):
    __tablename__ = "reviews"

    id = Column('id', primary_key=True)
    revisor_name = Column('reviewer_name')
    conteudo = Column('content')
    pontuacao = Column('rating')
    publicacao = Column('published_date')

    ##Relationships##
    livro_id = Column('book_id',Integer,ForeignKey('books.id'))


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
