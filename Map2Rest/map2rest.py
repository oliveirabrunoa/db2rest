from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
import json, pdb, os, importlib
from sqlalchemy import inspect

class LoadModelClasses(object):

    def __init__(self, loader_models):
        self.LOADER_MODEL_CLASSES = loader_models

    #Realiza o importe dos módulos a partir da lista informada no momento da criação do objeto LoadModelClasses
    def import_modules(self):
        model_list = []

        for model in self.LOADER_MODEL_CLASSES:
            module_name, class_name = model.rsplit('.', maxsplit=1)
            m = importlib.import_module(module_name)
            cls = getattr(m, class_name)
            model_list.append(cls)

        return model_list

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
    def get_model_attributes(self, model):
        model_attributes = []

        for attribute in model.__dict__.keys():
            if not attribute.startswith('__'):

                model_attrs = getattr(model.__dict__.get(attribute), '__dict__')
                if self.check_column_name(model.__tablename__, model_attrs.get('column_table')):
                    attributes = model_attrs
                    attributes['attribute_name'] = attribute
                    model_attributes.append(attributes)
                else:
                    print('A propriedade column_table ({0}) informado para o atributo {1}, modelo {2}, não existe na base de dados.'.
                          format(model_attrs.get('column_table'),attribute, model.__modelname__))
                    exit()
        return model_attributes


    #Geração do arquivo contendo os modelos.
    def generate_models(self):
        modules = self.import_modules()
        list_models = []
        for model in modules:
            dict_model = {}

            if self.check_table_exist(model.__tablename__):
                dict_model['model_name'] = model.__modelname__
                dict_model['table_name'] = model.__tablename__
                dict_model['attributes'] = self.get_model_attributes(model)

                list_models.append(dict_model)
            else:
                print('O __tablename__ informado para o modelo {0} não existe na base de dados.'.format(model.__modelname__))
        render_to_template("Map2Rest/models.py", "model_template.py", list_models)

    #Pendente: Criação de função para identificar relações, chaves e atributos compostos de acordo com valores informados!
