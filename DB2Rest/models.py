from DB2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Postagem(Base):
    __tablename__ = "post"

    id_postagem = Column('id',Integer,primary_key=True)
    titulo = Column('title')
    data_postagem = Column('date')
    hora_postagem = Column('time')

    ##Relationships##
    categoria_id = Column('category',Integer,ForeignKey('category.id'))
    categoria = relationship('Categoria',back_populates='postagens',lazy='joined')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Categoria(Base):
    __tablename__ = "category"

    id_categoria = Column('id',Integer,primary_key=True)
    descricao = Column('name')

    ##Relationships##
    postagens = relationship('Postagem',back_populates='categoria')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Livro(Base):
    __tablename__ = "books"

    id = Column('id',Integer,primary_key=True)
    titulo = Column('title')
    autor = Column('author')
    publicacao = Column('published_date')
    isbn = Column('isbn')

    ##Relationships##
    revisao = relationship('Revisao',back_populates='livro')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Revisao(Base):
    __tablename__ = "reviews"

    id = Column('id',Integer,primary_key=True)
    revisor_name = Column('reviewer_name')
    conteudo = Column('content')
    pontuacao = Column('rating')
    publicacao = Column('published_date')

    ##Relationships##
    livro_id = Column('book_id',Integer,ForeignKey('books.id'))
    livro = relationship('Livro',back_populates='revisao',lazy='joined')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Usuario(Base):
    __tablename__ = "users"

    id_usuario = Column('id',Integer,primary_key=True)
    nome = Column('name')

    ##Relationships##
    endereco = relationship('Endereco',back_populates='usuario',uselist=False)



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class Endereco(Base):
    __tablename__ = "addresses"

    id_endereco = Column('id',Integer,primary_key=True)
    rua = Column('street')
    cidade = Column('city')
    estado = Column('state')

    ##Relationships##
    usuario_id = Column('user_id',Integer,ForeignKey('users.id'))
    usuario = relationship('Usuario',back_populates='endereco')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class EntryModel(Base):
    __tablename__ = "entry"

    id_entry = Column('id',Integer,primary_key=True)
    titulo = Column('title')
    conteudo = Column('content_entry')

    ##Relationships##
    tags = relationship('EntryTag',back_populates='entry')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class TagModel(Base):
    __tablename__ = "tag"

    id_tag = Column('id',Integer,primary_key=True)
    nome = Column('name')

    ##Relationships##
    entries = relationship('EntryTag',back_populates='tag')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class EntryTag(Base):
    __tablename__ = "entrytag"

    id_entrytag = Column('id',Integer,primary_key=True)

    ##Relationships##
    entry_id = Column(Integer,ForeignKey('entry.id'),primary_key=True)
    entry = relationship('EntryModel',back_populates='tags')

    tag_id = Column(Integer,ForeignKey('tag.id'),primary_key=True)
    tag = relationship('TagModel',back_populates='entries')



    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
