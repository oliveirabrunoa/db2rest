from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

{% for model in data %}
class {{model.__model_name__}}(Base):
    __tablename__ = "{{model.__table_name__}}"

    {% for attr in  model.attributes -%}
        {{attr.attribute_name}} = Column('{{attr.column_table}}'{{", primary_key=True" if attr.primary_key }})
    {% endfor %}

    {%- for relation in model.relationships -%}
    {% if relation.type == "one-to-many" %}
    {{relation.child_model_name}}_id = Column('{{relation.child_table_name}}', Integer, ForeignKey('{{relation.foreign_key}}'))
    {{relation.child_model_name}} = relationship("{{relation.child_model_name.capitalize()}}", backref="{{relation.backref}}",lazy='joined')
    {% endif %}
    {%- endfor %}


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

{% if True -%}
{% endif %}
{% endfor %}
