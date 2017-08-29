

class Field(object):

    def __init__(self, *initial_data, **kwargs):
            for dictionary in initial_data:
                for key in dictionary:
                    setattr(self, key, dictionary[key])
            #Para parâmetros extras (kwargs)
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __get__(self, instance, owner):
        return getattr(self, '__dict__')
