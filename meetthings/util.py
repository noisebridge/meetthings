import json


def load_schema(name):
    with open("./schema/"+name+".json", 'r') as f:
        schema = json.load(f)

    return schema
