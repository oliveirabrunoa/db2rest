from Map2Rest.db import Base, db_session, engine, meta
from Map2Rest.render_template import render_to_template
import json, pdb, os, importlib
from sqlalchemy import inspect


class LoadModelClasses(object):

    def __init__(self, path_config_file):
        self.CONFIG_FILE = path_config_file #Path do json de configuração


    def open_config_file(self):
        data = []

        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE) as data_file:
                data = json.load(data_file)
        print('Lendo arquivo de configuração...')

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

    #Formata e checa as informações preenchidas sobre tabelas e atributos do arquivo de especificação.
    def check_model_attributes(self, model):

        if not self.check_table_exist(model.__db_table_name__):
            print('A __db_table_name__ informada para o modelo {0} não existe!'.format(model.__rst_model_name__))
            exit()

        for attributes_list in model.get_model_attributes():
            if not self.check_column_name(model.__db_table_name__, attributes_list.get('db_column_table')):
                print('A propriedade db_column_table ({0}) informado para o modelo {1} não existe na base de dados.'
                      .format(attributes_list.get('db_column_table'), model.__rst_model_name__))
                exit()

        return True

    #Geração do arquivo contendo os modelos.
    def generate_models(self):
        list_models = self.models_list()
        print('Gerando modelos...')
        for model in list_models:
            if self.check_model_attributes(model):
                setattr(model, 'attributes', model.get_model_attributes())
                print('O modelo {0} correspondente a tabela {1} foi criado com sucesso!'.format(model.__rst_model_name__, model.__db_table_name__))
            else:
                print('O __tablename__ informado para o modelo {0} não existe na base de dados.'.format(model.__modelname__))
                exit()
        return list_models


    def check_relationships(self):
        meta.reflect(bind=engine)
        for t in meta.sorted_tables:
            if t.name == 'post':
                mapper = inspect(t)
                fory = mapper.foreign_keys
                for o in fory:
                    print(o.name)


    def generate_file(self):
        list_models = self.generate_models()
        self.check_relationships()
        #render_to_template("Map2Rest/models.py", "model_template.py", list_models)
        #verificar modelos criados e ver se existe uma relação entre eles. Se existir,
        # segue o barco... se não existir, mostrar uma mensagem informando que não existe o relacionamento na database.


class ModelHelper(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_model_attributes(self):
        model_attrs = {}
        for attribute in self.__dict__.keys():
            if not attribute.startswith('__'):
                if attribute == 'attributes':
                    model_attrs = getattr(self,attribute)
                    return model_attrs

        return model_attrs

    def get_relationships(self):
        relationships_attr = getattr(self, 'relationships', None)
        if relationships_attr:
            return relationships_attr
        return False
