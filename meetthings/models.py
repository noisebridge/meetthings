from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    DateTimeField,
)

import validators


class NoSchemaException(Exception):
    pass


class MeetingObject:

    def __init__(self, schema):
        self.metadata = schema[self.schema_name]
        self.validators = {}

    def compose_form(self):
        if self.schema_name is None:
            raise NoSchemaException

        self.fields = {
            field_name: FIELD_MAPPING[field['type']](field_name)
            for field_name, field in self.metadata.items()
            if field['type'] in FIELD_MAPPING}

        self.enrich_fields()

    def enrich_fields(self):
        for field in self.fields.keys():
            if (field in self.metadata
                    and 'validators' in self.metadata[field]):
                field_schema = self.metadata[field]
            else:
                continue

            self.validators[field] = [
                getattr(validators, validator)(**args)
                for validator, args
                in field_schema['validators'].items()]


class Event(MeetingObject):
    schema_name = 'event'


class Venue(MeetingObject):
    schema_name = 'venue'


class Rsvp(MeetingObject):
    schema_name = 'rsvp'


class Address(MeetingObject):
    schema_name = 'address'


FIELD_MAPPING = {
    'string': StringField,
    'integer': IntegerField,
    'boolean': BooleanField,
    'datetime': DateTimeField,
}
