import json


def load_schema(name):
    with open("./schema/"+name+".json", 'r') as f:
        schema = json.load(f)

    return schema


def get_validators(field_schema):
    field_validators_schema = field_schema.get('validators')

    if field_validators_schema is not None:
        field_validators = [
            getattr(validators, validator)(**args)
            for validator, args in field_validators_schema.items()]
    else:
        field_validators = None

    return field_validators
