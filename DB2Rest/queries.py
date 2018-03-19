from sqlalchemy import inspect
from DB2Rest.db import Base, db_session, engine, meta


def get_table_derived_attributes(**kwargs):
    table_name = kwargs.get('table_name')
    for table in meta.sorted_tables:
        if table.name==table_name:
            if check_column(table, kwargs.get('column_name')):
                column_required = get_column(table, kwargs.get('column_name'))
                clause_where_attr = get_column(table, kwargs.get('clause_where_attribute'))
                clause_where_value = kwargs.get('clause_where_value')
                query_result = db_session.query(column_required).filter(clause_where_attr==clause_where_value)

                if kwargs.get('many') is True:
                    results = query_result.all()
                    result_formated = []
                    [result_formated.append(result[0]) for result in results]
                    return result_formated
                else:
                    results = query_result.first()
                    return results[0]


def check_column(table, column_name):
    for column in table.c:
        if str(column.name) == column_name:
            return True
    return False

def get_column(table, column_name):
    for column in table.c:
        if str(column.name) == column_name:
            return column
