from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String

{% for model in data %}
class {{model.model_name}}(Base):
    __tablename__ = "{{model.table_name}}"

    {% for attr in  model.attributes -%}
        {{attr.attribute_name}} = Column('{{attr.column_table}}' {{", primary_key=True" if attr.primary_key }})
    {% endfor %}

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
{% if True -%}
{% endif %}
{% endfor %}
