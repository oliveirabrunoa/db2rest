from Map2Rest.db_config import Base, db_session, engine, meta
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

    def generate_base_file(self):
        models_list = self.import_modules()
        data_to_render = []

        for model in models_list:
            model_data = {"model_name": model.__modelname__, "table_name": model.__tablename__}
            attributes = []
            for attribute in model.__attributes__:
                attributes.append(attribute)
            model_data['attributes']= attributes
            data_to_render.append(model_data)
        render_to_template("Map2Rest/model.json", "configuration_file.html",data_to_render)


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
        render_to_template("Map2Rest/db_model.py", "template_model.py", list_models)


    def open_config_file(self):
        mode_json_path = 'Map2Rest/model.json'
        data = []
        if os.path.exists(mode_json_path):
            with open('Map2Rest/model.json') as data_file:
                data = json.load(data_file)
            return data
        return data
