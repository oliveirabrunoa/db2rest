
'''
class Field(object):

    def __init__(self, name, type, primary_key=False, max_lenght=None, default=None, nullable=False):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.max_lenght = max_lenght
        self.default = default
        self.nullable = nullable

    def attributes():
        return dict(name=self.name,type=self.type,primary_key=self.primary_key,max_lenght=self.max_lenght,
                     default=self.default,nullable=self.nullable)

    def __str__(self):
        return self.name
'''
