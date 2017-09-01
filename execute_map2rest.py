import importlib
from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
from Map2Rest.map2rest import LoadModelClasses
import json


if __name__ == '__main__':
    LOADER_MODEL_CLASSES = ['blueprints.models.Post', 'blueprints.models.Category']
    l = LoadModelClasses(LOADER_MODEL_CLASSES)
    #l.generate_base_file()
    #l.generate_models()
    #l.config()
    #l.table_names()
    #l.check_table_exist('course_type')
    l.generate_models()
    #l.check_column_name('user_type', 'id')
