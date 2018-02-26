from Map2Rest.db import Base, meta
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

#Many-to-one
class Postagem(Base):
    __tablename__ = "post"

    id_postagem = Column('id', primary_key=True)
    titulo = Column('title')
    data_postagem = Column('date')
    hora_postagem = Column('time')

    ##Relationships##
    categoria_id = Column('category',Integer,ForeignKey('category.id'))
    categoria = relationship('Categoria',backref='postagens',lazy='joined')



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

#One-to-Many
class BookModel(Base):
    __tablename__ = 'books'
    id = Column('id', primary_key=True)
    titulo = Column('title')
    autor = Column('author')
    publicacao = Column('published_date')
    isbn = Column('isbn')

    revisor = relationship("ReviewsModel")

class ReviewsModel(Base):
    __tablename__ = 'reviews'
    id = Column('id', primary_key=True)
    revisor_name = Column('reviewer_name')
    conteudo = Column('content')
    pontuacao = Column('rating')
    publicacao = Column('published_date')

    livro_id = Column('book_id',Integer,ForeignKey('books.id'))


#One-to-one
class UsersModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name =Column('name')

    endereco = relationship("AddressesModel", uselist=False, back_populates="usuario")

class AddressesModel(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    rua = Column('street')
    cidade = Column('city')
    estado = Column('state')

    usuario_id = Column('user_id',Integer, ForeignKey('users.id'))
    usuario = relationship("UsersModel", back_populates="endereco")

#Many-to-Many
class Association(Base):
    __tablename__ = 'entrytag'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('entry.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)
    tag = relationship("TagModel", back_populates="entries")
    entry = relationship("EntryModel", back_populates="tags")


class EntryModel(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    titulo = Column('title')
    conteudo_post = Column('content_entry')
    tags = relationship("Association", back_populates="entry")

class TagModel(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    nome = Column('name')
    entries = relationship("Association", back_populates="tag")
