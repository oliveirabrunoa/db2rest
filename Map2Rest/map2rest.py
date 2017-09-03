from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
import json, pdb, os, importlib
from sqlalchemy import inspect


class LoadModelClasses(object):

    def __init__(self, loader_models):
        self.LOADER_MODEL_CLASSES = loader_models #Path do json de configuração

    def open_config_file(self):
        mode_json_path = 'Map2Rest/to_generate_models.json'
        data = []
        if os.path.exists(mode_json_path):
            with open(mode_json_path) as data_file:
                data = json.load(data_file)
        return data

    def models_list(self):
        models_json = self.open_config_file()
        models_list = []

        for model_json in models_json:
            model = ModelHelper(**model_json)
            models_list.append(model)

        return models_list



    #Verifica se o nome da tabela informado existe na base de dados.
    def check_table_exist(self, table_name):
        table_names = meta.sorted_tables

        if table_name in str(table_names):
            return True
        return False

    #Verifica se o nome da coluna informada existe na base de dados.
    def check_column_name(self,table_name, column_name):
        insp = inspect(engine)

        for collumn in insp.get_columns(table_name):
            if collumn.get('name') == column_name:
                return True
        return False

    #Formata e checa as informações preenchidas nos módulos.
    def check_model_attributes(self, model):

        if not self.check_table_exist(model.__table_name__):
            print('A __table_name__ informada para o modelo {0} não existe!'.format(model.__model_name__))
            exit()

        for attribute in model.get_model_attributes():
            for key in attribute.keys():
                attr = attribute[key].get('column_table')
                if not self.check_column_name(model.__table_name__, attribute[key].get('column_table')):
                    print('A propriedade column_table ({0}) informado para o atributo {1}, modelo {2}, não existe na base de dados.'.
                          format( attribute[key].get('column_table'),key, model.__model_name__ ))
                    exit()
        return True

    #Geração do arquivo contendo os modelos.
    def generate_models(self):
        list_models = self.models_list()

        for model in list_models:
            print(model)
            #if self.check_model_attributes(model):
        #
        #         dict_model = {}
        #
        #         dict_model['model_name'] = model.__model_name__
        #         dict_model['table_name'] = model.__table_name__
        #         dict_model['attributes'] = model.get_model_attributes()
        #
        #         list_models.append(dict_model)
        #     else:
        #         print('O __tablename__ informado para o modelo {0} não existe na base de dados.'.format(model.__modelname__))
        # render_to_template("Map2Rest/models.py", "model_template.py", list_models)

    #Pendente: Criação de função para identificar relações, chaves e atributos compostos de acordo com valores informados!


class ModelHelper(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_model_attributes(self):
        model_attributes = []

        for attribute in self.__dict__.keys():
            model_attrs = getattr(self, 'attributes')
            if not attribute.startswith('__'):
                model_attributes.append(model_attrs)

        return model_attributes
