import pudb
from collections import defaultdict
from flask_wtf import FlaskForm
from util import get_validators
from wtforms import (
    StringField,
    BooleanField,
    IntegerField,
    DateTimeField,
    FormField,
)

from pudb import set_trace

FIELD_MAPPING = {
    'string': StringField,
    'boolean': BooleanField,
    'integer': IntegerField,
    'datetime': DateTimeField,
}


class Promise:

    def __init__(self, name, field_def):
        self.name = name
        self.schema = field_def

    def resolve(self):
        pass


def create_field(name, field_def):
    # if field is not in FIELD_MAPPING, we need to create a FormField.
    # hold a promise to do that, then reprocess once all top level fields
    # are done.

    field_class = FIELD_MAPPING.get(field_def['type'])

    if field_class is None:
        return(Promise(name, field_def))

    field_validator_defs = field_def.get('validators')
    if field_validator_defs:
        field_validators = get_validators(field_validator_defs)
    else:
        field_validators = None

    kwargs = {'name': name,
              'validators': field_validators}

    return field_class(**kwargs)


def form_factory(schema):
    promises = defaultdict(list)
    forms = {}

    for form, form_def in schema.items():
        form_obj = type(form, (FlaskForm, ), {})

        for field, field_def in form_def.items():
            field_obj = create_field(field, field_def)

            if isinstance(field_obj, Promise):
                promises[form].append(field_obj)
            else:
                setattr(form_obj, field, field_obj)

        if form not in promises:
            FIELD_MAPPING[form] = FormField

        forms[form] = form_obj

    counter = 0
    while len(promises) != 0:

        # needed a I am modifying the dictionary during iteration.  Probably
        # could clean this up but not for now
        promised_fields = zip(list(promises.keys()), list(promises.values()))
        for form, fields in promised_fields:

            for field_idx in range(len(fields)):
                field_name = fields[field_idx].name

                if field_name in FIELD_MAPPING:
                    field = FormField(forms[field_name])
                    setattr(form_obj, field_name, field)
                    del(promises[form][field_idx])

                if len(promises[form]) == 0:
                    FIELD_MAPPING[form] = forms[form]
                    del(promises[form])

        # just in case I messed something up and we hit an infinite loop
        counter += 1
        if counter > 100:
            raise Exception

    return(forms)
