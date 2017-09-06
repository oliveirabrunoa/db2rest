from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String


class Postagem(Base):
    __tablename__ = "post"

    id_postagem = Column('post_id' , primary_key=True)
    titulo = Column('post_title' )
    data_postagem = Column('post_date' )
    hora_postagem = Column('post_time' )
    


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Categoria(Base):
    __tablename__ = "category"

    id_categoria = Column('category_id' , primary_key=True)
    descricao = Column('category_name' )
    


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

