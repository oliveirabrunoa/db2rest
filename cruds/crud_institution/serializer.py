from . import models


class InstitutionSerializer:

    def serialize(self, institutions):
        data = []
        for institution in institutions:

            data.append({
                'id': institution.id,
                'name': institution.name,
                'abbreviation': institution.abbreviation,
                'cnpj':institution.cnpj,
                'address':institution.address,
                'current_program_section':institution.current_program_section
            })

        return data 
