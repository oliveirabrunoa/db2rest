# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(BASE_DIR, 'templates')),
    trim_blocks=False)

def render_template(template, data):
    return TEMPLATE_ENVIRONMENT.get_template(template).render(data)

def render_to_template(file_name_arg, data):
    file_name = file_name_arg
    with open(file_name, 'w') as file:
        data_to_render = render_template('configuration_file.html', data)
        file.write(data_to_render)


if __name__ == "__main__":
    create_index_html()
