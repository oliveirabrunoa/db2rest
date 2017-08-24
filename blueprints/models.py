

class Post(object):
    __modelname__ = 'Post'

    __tablename__ = 'course_type'

    __attributes__ = [{"name":"id_course_type", "type": "Integer", "primary_key": True},
                     {"name":"description_course_type", "type":"String", "max_lenght": 50}]


class Category(object):
    __modelname__ = 'Category'

    __tablename__ = 'user_type'

    __attributes__ = [{"name":"id_user_type", "type": "Integer", "primary_key": True},
                     {"name":"name_user_type", "type":"String", "max_lenght": 20}]
