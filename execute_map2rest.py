import importlib
from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
from Map2Rest.map2rest import LoadModelClasses
import json


if __name__ == '__main__':
    CONFIG_FILE = 'Map2Rest/to_generate_models.json'
    load_models = LoadModelClasses(CONFIG_FILE)
    load_models.generate_file()
