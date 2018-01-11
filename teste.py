from Map2Rest.db import Base, engine, meta
from Map2Rest.models import Postagem, Categoria
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy import inspect
from sqlalchemy.engine import reflection


def get_relationships():
    '''
    meta.reflect(bind=engine)
    for t in meta.sorted_tables:
        #print('table nome',t.name)
        inss = inspect(t)
        print(type(inss))

    #insp = reflection.Inspector.from_engine(engine)
    #print(insp.get_foreign_keys('post'))
'''
    a = Postagem.__mapper__.relationships
    for i in a:
        if i.mapper.class_
        print(i.mapper.class_ )



    #mapper = inspect(Postagem).mapper
    #thing_relations = inspect(Postagem).relationships
    #print(thing_relations.keys().value)
    #a = insp.relationships
    #print(insp.relationships)

    #for i in a:
        #print(i)

    #for rel in mapper.relationships:
    #    print(rel)
    #for i in insp.relationships:
    #    print(i)

    ##########
'''
    for rel in mapper.relationships:
        key = rel.key
        print('relationship', key, 'to', getattr(Postagem, key))
        for lcl in rel.local_columns:
            local_key = mapper.get_property_by_column(lcl).key
            print(local_key, getattr(Postagem, local_key))

'''

if __name__ == '__main__':
    get_relationships()
