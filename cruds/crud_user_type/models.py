from MapToRest.db_model import BaseClass


class UserType():

    __modelname__ = 'UserType'

    __tablename__ = 'user_type'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"name", "type":"String", "max_lenght": 20}]

    def __init__(self, description):
        BaseClass.__init__(self, id, name)
