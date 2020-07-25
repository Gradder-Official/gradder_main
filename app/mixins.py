from flask.json import JSONEncoder

from bson import ObjectId
from wtforms.fields.core import Field
from wtforms.widgets import Option, Select, TextArea


class JSONForm:
    def get_form_json(self):
        fields = []
        for name, field in self.__dict__.items():
            if issubclass(field.__class__, Field):
                # Attributes we know definitely exist
                field_data = {
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
                    'description': field.description,
                    'value': None,
                    'type': 'text',
                }

                if hasattr(field, '_value'):
                    field_data['value'] = field._value()
                
                if hasattr(field, 'widget'):
                    if hasattr(field.widget.__class__, 'input_type'):
                        field_data['type'] = field.widget.__class__.input_type
                    else:
                        # If a special type, just use name
                        # This only applies for TextArea, Select and Option
                        field_data['type'] = field.widget.__class__.__name__.lower()

                fields.append(field_data)

        return fields


class JSONImproved(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(o)
