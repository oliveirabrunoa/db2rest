from Map2Rest.db import Base
from sqlalchemy import Column, Integer, String

{% for model in data %}
class {{model.model_name}}(Base):
    __tablename__ = "{{model.table_name}}"

    {% for a in  model.attributes -%}
    {% for k,v in a.items() -%}
        {{k}} = Column('{{v}}'{{', primary_key=True' if 'id' in k }})
    {% endfor -%}
    {% endfor %}

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
{% if True -%}
{% endif %}
{% endfor %}
