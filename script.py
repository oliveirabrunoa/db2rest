import importlib
from MapToRest.db_config import Base, db_session, engine, meta
from MapToRest.render_template import render_to_template

LOADER_MODEL_CLASSES = 'cruds.crud_course_type.models.CourseType'

class LoadModelClasses:

    def import_modules(self):
        module_name, class_name = LOADER_MODEL_CLASSES.rsplit('.', maxsplit=1)
        m = importlib.import_module(module_name)
        cls = getattr(m, class_name)
        #
        # for field in cls.__attributes__:
        #     print(field)

        return cls

    def table_names(self):
        for t in meta.sorted_tables:
            print(t)

    def generate_base_file(self):

        attributes_class = self.import_modules()
        a = attributes_class.__attributes__[0]
        print(a.get('name'))
        data = {
                "model_name": attributes_class.__modelname__,
                "table_name": "substituir pelo nome da tabela",
                "model_att_id": a.get('name'),
                "column_table_id": "nome coluna banco",
                "model_att_description": a.get('type'),
                "column_table_description": "nome colua banco"

                
                }

        render_to_template("seraaaa.json", data)


        # data = {
        #     'class_name': "class_name",
        #     'table_name':"table_name"
        # }




if __name__ == '__main__':
    l = LoadModelClasses()
    l.generate_base_file()



#ACESSAR A LISTA DE MODELS
#FAZER IMPORT E LEITURA DE ATRIBUTOS
#LER SCHEMA DO BANCO
