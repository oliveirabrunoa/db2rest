

class UserType:

    __modelname__ = 'UserType'

    __tablename__ = 'user_type'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"name", "type":"String", "max_lenght": 20}]
