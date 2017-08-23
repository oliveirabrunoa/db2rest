from backend import db
from . import models
import importlib


class UserTypeDestinationsSerializer:

    def serialize(self, user_type_destinations, query_parameter):
        data=[]
        module_group_data = ''

        for user_type_destination in user_type_destinations:
            if user_type_destination.group_module:
                module_path, model_name = str(user_type_destination.group_module).rsplit('.', maxsplit=1)
                module_class = getattr(importlib.import_module(module_path), model_name)
                module_group_data = str(module_class.query.get(int(query_parameter)))

            data.append(
            {'id': user_type_destination.id,
            'name':user_type_destination.name,
            'param_values_service':user_type_destination.param_values_service,
            'group': str(user_type_destination.group).replace('$', module_group_data)
            })

        return data
