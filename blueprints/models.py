from Map2Rest.fields import Field

class Post(object):
    __modelname__ = 'Post'

    __tablename__ = 'course_type'

    #Attributes
    id_course_type = Field(type='Integer', primary_key=True, column_table='id')
    description_course_type = Field(type='String', max_lenght=50)


    # __attributes__ = [{"name":"id_course_type", "type": "Integer", "primary_key": True},
    #                  {"name":"description_course_type", "type":"String", "max_lenght": 50}]



class Category(object):
    __modelname__ = 'Category'

    __tablename__ = 'user_type'

    #Attributes
    id_user_type = Field(type='Integer', primary_key=True, column_table='id')
    name_user_type = Field(type='String', max_lenght=50)

    # __attributes__ = [{"name":"id_user_type", "type": "Integer", "primary_key": True},
    #                  {"name":"name_user_type", "type":"String", "max_lenght": 20}]
