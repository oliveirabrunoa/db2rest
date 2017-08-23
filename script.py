import importlib
from MapToRest.db_config import Base, db_session, engine, meta

LOADER_MODEL_CLASSES = 'cruds.crud_course_type.models.CourseType'

class LoadModelClasses:

    def import_modules(self):
        module_name, class_name = LOADER_MODEL_CLASSES.rsplit('.', maxsplit=1)
        m = importlib.import_module(module_name)
        cls = getattr(m, class_name)

        for field in cls.__attributes__:
            print(field)

        return cls.__attributes__[0].get('name')

    def table_names(self):
        for t in meta.sorted_tables:
            print(t)


if __name__ == '__main__':
    l = LoadModelClasses()
    l.teste()



#ACESSAR A LISTA DE MODELS
#FAZER IMPORT E LEITURA DE ATRIBUTOS
#LER SCHEMA DO BANCO
