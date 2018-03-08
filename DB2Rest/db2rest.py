from DB2Rest.db import Base, db_session, engine, meta
from DB2Rest.render_template import render_to_template
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

    def get_table(self, table_name):

        for table in meta.sorted_tables:
            if table.name==table_name:
                return table

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
        print("Gerando modelos...")
        for model in list_models:
            if self.check_model_attributes(model):
                setattr(model, 'attributes', model.get_model_attributes())
                print('Modelo->Tabela: {0} >>>> {1}'.format(model.__rst_model_name__, model.__db_table_name__))
            else:
                print('O __tablename__ informado para o modelo {0} não existe na base de dados.'.format(model.__modelname__))
                exit()
        return list_models


    def check_relationships(self, model):

        if not model.get_relationships():
            return False

        result_list = []
        for relationship in model.get_relationships():
            table_name = relationship.get('db_table_name')#Obtém o nome da tabela com o qual tem relacionamento
            if not relationship.get('type') == "M2M":
                if not self.check_table_exist(table_name): #verifica se a tabela de fato existe na base
                    result_list.append({'status': 'A tabela {0} não existe na Base de Dados. Verifique os relacionamentos para o modelo no JSON de configuração e tente novamente.'
                                   .format(table_name)})
                    return False

                mapper_table = inspect(self.get_table(table_name))
                for pk in mapper_table.primary_key:
                    if not str(pk.name) == (relationship.get('db_foreign_key').split(".")[1]):
                        result_list.append({'relationships': 'Relacionamento entre {0} e {1} através da foreign_key {2} NÃO encontrado!'
                                       .format(model.__db_table_name__,relationship.get('db_table_name'),relationship.get('db_foreign_key'))})

            return result_list


    def relationship_atributes_attrs(self, model, relation_list):
        if not getattr(model, 'relationship_atributes', None):
            setattr(model, 'relationship_atributes', relation_list)
            return model
        else:
            setattr(model, 'relationship_atributes', getattr(model, 'relationship_atributes') + relation_list)
            return model

    def generate_relationships(self,list_models):
        print('Verificando relacionamentos....')
        for model in list_models:
            if not model.get_relationships():
                #print('O modelo {0} não possui relacionamentos definidos no arquivo de configuração.'.format(model.__rst_model_name__))
                continue

            for relation in model.get_relationships():
                if relation.get('type') == 'M2O':
                    relation_M2O = [
                             {
                             'relation_atribute_name': '{0}_id'.format(relation.get('rst_model_name')),
                             'atribute_field': 'Column','atribute_field_name': "'{0}'".format(relation.get('db_table_name')),
                             'atribute_field_type': 'Integer','atribute_field_fk': "'{0}'".format(relation.get('db_foreign_key'))
                             },
                             {
                             'relation_atribute_name': relation.get('rst_model_name'),'atribute_field': 'relationship',
                             'atribute_field_name': "'{0}'".format(relation.get('rst_model_name').capitalize()),
                             'atribute_field_backref': "'{0}'".format(relation.get('rst_backref')),
                             'atribute_field_lazy':"'joined'"
                             }]
                    self.relationship_atributes_attrs(model,relation_M2O)

                if relation.get('type') == 'O2M':
                    relation_O2M = [
                             {
                             'relation_atribute_name': '{0}_id'.format(relation.get('rst_model_target').lower()),
                             'atribute_field': 'Column','atribute_field_name': "'{0}'".format(relation.get('db_column_fk')),
                             'atribute_field_type': 'Integer','atribute_field_fk': "'{0}'".format(relation.get('db_foreign_key'))
                             }]

                    self.relationship_atributes_attrs(model,relation_O2M)

                    relation_O2M_target = [
                               {
                               'relation_atribute_name': relation.get('rst_model_name'),'atribute_field': 'relationship',
                               'atribute_field_name': "'{0}'".format(relation.get('rst_model_name').capitalize())
                               }]
                    target = self.get_model_by_name(list_models,relation.get('rst_model_target'))
                    self.relationship_atributes_attrs(target,relation_O2M_target)

                if relation.get('type') == 'O2O':
                    relation_O2O = [
                             {
                              'relation_atribute_name': '{0}_id'.format(relation.get('rst_model_name')),
                              'atribute_field': 'Column','atribute_field_name': "'{0}'".format(relation.get('db_column_fk')),
                              'atribute_field_type': 'Integer','atribute_field_fk': "'{0}'".format(relation.get('db_foreign_key'))
                             },
                             {
                             'relation_atribute_name': relation.get('rst_model_name'),'atribute_field': 'relationship',
                             'atribute_field_name': "'{0}'".format(relation.get('rst_model_name').capitalize()),
                             'atribute_field_back_populates': "'{0}'".format(relation.get('rst_back_populates'))
                             }]
                    self.relationship_atributes_attrs(model,relation_O2O)

                    relation_O2O_target = [
                               {
                               'relation_atribute_name': relation.get('rst_model_target_name'),'atribute_field': 'relationship',
                               'atribute_field_name': "'{0}'".format(model.__rst_model_name__),
                               'atribute_uselist': "'False'", 'atribute_field_back_populates': "'{0}'".format(relation.get('rst_model_name'))
                               }]
                    target = self.get_model_by_name(list_models,relation.get('rst_model_target'))
                    self.relationship_atributes_attrs(target,relation_O2O_target)

                if relation.get('type') == 'M2M':
                    relation_M2M = [
                             {
                              'relation_atribute_name': '{0}_id'.format(relation.get('db_association_fk_a').split('.')[0]),
                              'atribute_field': 'Column','atribute_field_type': 'Integer', 'atribute_pk':True,
                              'atribute_field_fk': "'{0}'".format(relation.get('db_association_fk_a'))
                             },
                             {
                             'relation_atribute_name': relation.get('rst_association_atribute_a'),'atribute_field': 'relationship',
                             'atribute_field_name': "'{0}'".format(relation.get('rst_association_a')),
                             'atribute_field_back_populates': "'{0}'".format(relation.get('rst_back_populates_a'))
                             },
                             {
                             'relation_atribute_name': '{0}_id'.format(relation.get('db_association_fk_b').split('.')[0]),
                             'atribute_field': 'Column','atribute_field_type': 'Integer','atribute_pk':True,
                             'atribute_field_fk': "'{0}'".format(relation.get('db_association_fk_b'))
                             },
                             {
                             'relation_atribute_name': relation.get('rst_association_atribute_b'),'atribute_field': 'relationship',
                             'atribute_field_name': "'{0}'".format(relation.get('rst_association_b')),
                             'atribute_field_back_populates': "'{0}'".format(relation.get('rst_back_populates_b'))
                             }]
                    self.relationship_atributes_attrs(model,relation_M2M)

                    relation_M2M_target_A = [
                               {
                               'relation_atribute_name': relation.get('rst_back_populates_a'),'atribute_field': 'relationship',
                               'atribute_field_name': "'{0}'".format(model.__rst_model_name__),
                               'atribute_field_back_populates': "'{0}'".format(relation.get('rst_association_atribute_a'))
                               }]
                    target_a = self.get_model_by_name(list_models,relation.get('rst_association_a'))
                    self.relationship_atributes_attrs(target_a,relation_M2M_target_A)

                    relation_M2M_target_B = [
                               {
                               'relation_atribute_name': relation.get('rst_back_populates_b'),'atribute_field': 'relationship',
                               'atribute_field_name': "'{0}'".format(model.__rst_model_name__),
                               'atribute_field_back_populates': "'{0}'".format(relation.get('rst_association_atribute_b'))
                               }]
                    target_b = self.get_model_by_name(list_models,relation.get('rst_association_b'))
                    self.relationship_atributes_attrs(target_b,relation_M2M_target_B)

        render_to_template("DB2Rest/models.py", "model_template.py",list_models)


    def get_model_by_name(self, list_models, model_name):

        for model in list_models:
            if model.__rst_model_name__ == model_name:
                return model


    def generate_file(self):
       list_models = self.generate_models()
       relations=[]
       for model in list_models:
           relations.append(self.check_relationships(model))
       self.generate_relationships(list_models)
       [print(r) for r in relations if r]
       print('Arquivo models.py gerado com sucesso! Realize o import deste arquivo para uso dos serviços!')

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
