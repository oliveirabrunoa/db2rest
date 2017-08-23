from MapToRest.db_model import UserTypeBase


class UserType(UserTypeBase):

    __modelname__ = 'UserType'

    __tablename__ = 'user_type'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"name", "type":"String", "max_lenght": 20}]

    def __init__(self, description):
        super().__init__(self, id, name)
