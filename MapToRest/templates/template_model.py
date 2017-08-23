from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String

{% for model in data %}
class {{model.model_name}}(Base):
    __tablename__ = "{{model.table_name}}"
    __table_args__ = ({'autoload':True})

    {% for a in  model.attributes -%}
    {% for k,v in a.items() -%}
        {{k}} = Column('{{v}}'{{', primary_key=True' if k=='id' }})
    {% endfor -%}
    {% endfor %}

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
{% if True -%}
{% endif %}
{% endfor %}
