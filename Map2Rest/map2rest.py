from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
import json, pdb, os, importlib
from sqlalchemy import inspect

class LoadModelClasses(object):

    def __init__(self, loader_models):
        self.LOADER_MODEL_CLASSES = loader_models

    #Verifica se o nome da tabela informado existe na base de dados.
    def check_table_exist(self, table_name):
        table_names = meta.sorted_tables
        if table_name in str(table_names):
            return True
        return False

    #Verifica se o nome da coluna informada existe na base de dados.
    def check_column_name(self,table_name, column_name):
        insp = inspect(engine)
        for f in insp.get_columns(table_name):
            if f.get('name') == 'column_name':
                return True
        return False

    #Realiza o importe dos módulos a partir da lista informada no momento da criação do objeto LoadModelClasses
    def import_modules(self):
        model_list = []
        for model in self.LOADER_MODEL_CLASSES:
            module_name, class_name = model.rsplit('.', maxsplit=1)
            m = importlib.import_module(module_name)
            cls = getattr(m, class_name)
            model_list.append(cls)

        return model_list

    #Formata e checa as informações preenchidas nos módulos.
    def prepare_models(self):
        list_models = self.import_modules()

        for model in data_config:
            dict_model = model.__dict__
            for d in dict_model.keys():
                if not d.startswith('__'):
                    dict__ = getattr(dict_model.get(d), '__dict__')
                    print(dict_model.get('__tablename__'))
                    print(dict__)

    #Geração do arquivo contendo os modelos.
    def generate_models(self):

        #     dict_model = {
        #         "model_name": model.get('model_name'),
        #         "table_name": model.get('table_name'),
        #         "attributes": [model.get('attributes')]
        #         }
        #     list_models.append(dict_model)
        # render_to_template("Map2Rest/models.py", "model_template.py", list_models)

    #Pendente: Criação de função para identificar relações, chaves e atributos compostos de acordo com valores informados!
