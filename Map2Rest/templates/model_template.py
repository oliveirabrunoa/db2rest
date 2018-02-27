from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

{% for model in data %}
class {{model.__rst_model_name__}}(Base):
    __tablename__ = "{{model.__db_table_name__}}"

    {% for attr in  model.attributes -%}
        {{attr.rst_attribute_name}} = Column('{{attr.db_column_table}}'{{", primary_key=True" if attr.db_primary_key }})
    {% endfor %}
    ##Relationships##
    {%- for relation in model.relationship_atributes -%}
    {% if relation.atribute_field == "Column" %}
    {{relation.relation_atribute_name}} = {{relation.atribute_field}}({{relation.atribute_field_name}},{{relation.atribute_field_type}},ForeignKey({{relation.atribute_field_fk}}))
    {%- else %}
    {{relation.relation_atribute_name}} = {{relation.atribute_field}}({{relation.atribute_field_name}}{% if relation.atribute_field_backref is defined %} ,backref={{relation.atribute_field_backref}} {% endif %},lazy='joined')
    {% endif %}
    {%- endfor %}


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

{% if True -%}
{% endif %}
{% endfor %}
