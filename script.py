import importlib
from MapToRest.db_config import Base, db_session, engine, meta
from MapToRest.render_template import render_to_template

LOADER_MODEL_CLASSES = ['cruds.crud_course_type.models.CourseType']

class LoadModelClasses:

    def import_modules(self):
        model_list = []
        for model in LOADER_MODEL_CLASSES:
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

        for att_classs in models_list:
            data = {"model_name": att_classs.__modelname__, "table_name": "table name on database"}
            attributes = []
            for attribute in att_classs.__attributes__:
                attributes.append(attribute.get('name'))
            data['attributes']= attributes
            data_to_render.append(data)
        render_to_template("seraaaa.json", data)


if __name__ == '__main__':
    l = LoadModelClasses()
    l.generate_base_file()



#ACESSAR A LISTA DE MODELS
#FAZER IMPORT E LEITURA DE ATRIBUTOS
#LER SCHEMA DO BANCO
