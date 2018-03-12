from DB2Rest.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, back_populates

{% for model in data %}
class {{model.__rst_model_name__}}(Base):
    __tablename__ = "{{model.__db_table_name__}}"

    {% for attr in  model.attributes -%}
        {{attr.rst_attribute_name}} = Column('{{attr.db_column_table}}'{% if attr.db_primary_key is defined %},Integer,primary_key={{attr.db_primary_key}}{% endif %})
    {% endfor %}
    ##Relationships##
    {%- for relation in model.relationship_atributes -%}
    {% if relation.atribute_field == "Column" %}
    {{relation.relation_atribute_name}} = {{relation.atribute_field}}({% if relation.atribute_field_name is defined %}{{relation.atribute_field_name}},{% endif %}{{relation.atribute_field_type}},ForeignKey({{relation.atribute_field_fk}}){% if relation.atribute_pk is defined %},primary_key={{relation.atribute_pk}}{% endif %})
    {%- else %}
    {{relation.relation_atribute_name}} = {{relation.atribute_field}}({{relation.atribute_field_name}}{% if relation.atribute_field_backref is defined %},back_populates={{relation.atribute_field_backref}}{% endif %}{% if relation.atribute_field_back_populates is defined %},back_populates={{relation.atribute_field_back_populates}}{% endif %}{% if relation.atribute_field_lazy is defined %},lazy={{relation.atribute_field_lazy}}{% endif %}{% if relation.atribute_uselist is defined %},uselist={{relation.atribute_uselist}}{% endif %})
    {% endif %}
    {%- endfor %}


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

{% if True -%}
{% endif %}
{% endfor %}
