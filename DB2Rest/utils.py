from sqlalchemy import inspect
from DB2Rest.db import Base, db_session, engine, meta
import ast

def get_table_derived_attributes(**kwargs):
    table_name = kwargs.get('table_name')
    for table in meta.sorted_tables:
        if table.name==table_name:
            mapper_table = inspect(table)
            for column in mapper_table.c:
                if str(column.name) == kwargs.get('clause_where_attribute'):
                    result_query = (db_session.query(mapper_table).filter(column==kwargs.get('clause_where_value')))
                    if kwargs.get('many') is True:
                        return str(result_query.all())
                    return str(result_query.first())
