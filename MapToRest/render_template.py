# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(BASE_DIR, 'templates')),
    trim_blocks=False)

def render_template(template, data):
    return TEMPLATE_ENVIRONMENT.get_template(template).render(dict(data=data))

def render_to_template(file_name_arg, template_name, data_to_render):
    file_name = file_name_arg
    with open(file_name, 'a+') as file:
        template_render = render_template(template_name, data_to_render)
        file.write(template_render)
