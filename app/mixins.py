from wtforms.fields import Field

class JSONForm:
    def get_form_json(self):
        return [
            {
                'id': field.id,
                'name': field.short_name,
                'label': {
                    'field_id': field.label.field_id,
                    'text': field.label.text,
                },
                'flags': [
                    {'name': flag_name, 'value': flag_value}
                    for flag_name, flag_value in field.flags.__dict__.items()
                ],
                'default': field.default,
                'description': field.description

            }
            for name, field in self.__dict__.items()
            if issubclass(field.__class__, Field)
        ]