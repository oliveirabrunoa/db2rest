from MapToRest.db_config import Base
from sqlalchemy import Column, Integer, String


class {{model_name}}(Base):
    __tablename__ = "{{ table_name }}"
    __table_args__ = ({'autoload':True})

    {% for a in  attributes -%}
    {% for k,v in a.items() -%}
        {{k}} = Column('{{v}}')
    {% endfor -%}
    {% endfor %}

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


{% if True -%}

{% endif %}
