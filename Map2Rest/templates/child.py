{% extends "model_template.py" %}

{% block relationships %}
{% for model in data %}
{{model}}
{% endfor %}
{% endblock %}
