from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

{% for model in data %}
class {{model.__rst_model_name__}}(Base):
    __tablename__ = "{{model.__db_table_name__}}"

    {% for attr in  model.attributes -%}
        {{attr.rst_attribute_name}} = Column('{{attr.db_column_table}}'{{", primary_key=True" if attr.db_primary_key }})
    {% endfor %}


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

{% if True -%}
{% endif %}
{% endfor %}
