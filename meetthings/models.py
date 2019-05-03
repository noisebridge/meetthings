from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    DateTimeField,
    FormField,
)

import validators
from util import get_validators
from pudb import set_trace


class NoSchemaException(Exception):
    pass


class MeetingObject:

    def __init__(self, schema):
        self.schema = schema
        self.metadata = schema[self.schema_name]

        # self.metadata = schema
        self.fields = []
        self.simple_fields = []
        self.form_fields = []

    @classmethod
    def create_fields(cls):

        # TODO: when and how to handle form fields?
        for field_name, field_schema in cls.metadata.items():
            if field_schema['type'] in FIELD_MAPPING:

                field_class = FIELD_MAPPING[field_schema['type']]
                field_validators_schema = field_schema.get('validators')
                if field_validators_schema is not None:
                    field_validators = get_validators(field_validators_schema)
                else:
                    field_validators = None

                kwargs = {'name': field_name, 'validators': field_validators}
                # What to do when it should be a formfield
                cls.simple_fields.append(field_class(**kwargs))

            else:
                name = field_schema['type']
                field_class = type(name.capitalize() + "FormField",
                                   (MeetingObject, ),
                                   {"schema_name": name})
                f_field = field_class(cls.schema)
                f_field.create_fields()
                cls.form_fields.append(field_class(name))


class Formlet(FlaskForm):

    # look into FormList and FieldList to dynamically create forms
    # shouldn't be full schema, but form specific schema
    # name, form_schema

    schema = None

    def __init__(self):
        # self.schema = schema
        self.simple_fields = []
        self.form_fields = []
        self.create_form()

    # map schemas to subclasses based on top level schema items
    def create_simple_fields(self):

        for f_obj, f_def in self.schema.items():
            if f_def['type'] in FIELD_MAPPING:
                self.simple_fields.append({f_obj,
                                           FIELD_MAPPING[f_def['type']](f_def)})  # NOQA
            else:
                self.form_fields.append((f_obj, f_def))

    @classmethod
    def create_form_fields(cls):
        form_fields = []
        for (obj, obj_def) in cls.form_fields:
            FormletClass = type(obj.capitalize(),
                                (Formlet, ),
                                {'schema': obj_def})
            form_fields.append(FormField(FormletClass))
        cls.form_fields = form_fields

    @classmethod
    def create_form(cls):
        cls.create_simple_fields()
        cls.create_form_fields()

    @classmethod
    def bind_field(cls, field_dict):
        field_name = field_dict['name']
        field = field_dict['base']
        field.bind(cls, field_name)
        # cls[field_name] = field

        if "validators" in field_dict:
            field.validators = field_dict['validators']


FIELD_MAPPING = {
    'string': StringField,
    'integer': IntegerField,
    'boolean': BooleanField,
    'datetime': DateTimeField,
    # 'rsvp': RsvpForm,
}
