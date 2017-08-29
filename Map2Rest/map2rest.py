from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
import json, pdb, os, importlib


class LoadModelClasses(object):

    def __init__(self, loader_models):
        self.LOADER_MODEL_CLASSES = loader_models


    def import_modules(self):
        model_list = []
        for model in self.LOADER_MODEL_CLASSES:
            module_name, class_name = model.rsplit('.', maxsplit=1)
            m = importlib.import_module(module_name)
            cls = getattr(m, class_name)
            model_list.append(cls)

        return model_list

    def table_names(self):
        for table in meta.sorted_tables:
            print(table)

    def generate_new_models(self):
        data_config = self.open_config_file()

        if not data_config:
            print("Necessário configurar o arquivo model.json!")
            exit()

        list_models=[]
        for model in data_config:
            dict_model = {
                "model_name": model.get('model_name'),
                "table_name": model.get('table_name'),
                "attributes": [model.get('attributes')]
                }
            list_models.append(dict_model)
        render_to_template("Map2Rest/models.py", "model_template.py", list_models)
