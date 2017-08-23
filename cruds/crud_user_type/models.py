

class UserType:

    __modelname__ = 'UserType'

    __tablename__ = 'user_type'

    __attributes__ = [{"name":"id_user_type", "type": "Integer", "primary_key": True},
                     {"name":"name_user_type", "type":"String", "max_lenght": 20}]
