import importlib
from MapToRest.db_config import Base, db_session, engine, meta
from MapToRest.render_template import render_to_template
from MapToRest.script import LoadModelClasses
import json



if __name__ == '__main__':
    LOADER_MODEL_CLASSES = ['cruds.crud_course_type.models.CourseType']
    l = LoadModelClasses(LOADER_MODEL_CLASSES)
    l.generate_base_file()
    l.generate_new_models()




#ACESSAR A LISTA DE MODELS
#FAZER IMPORT E LEITURA DE ATRIBUTOS
#LER SCHEMA DO BANCO
