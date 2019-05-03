from models import MeetingObject, Formlet
from util import load_schema


def api_factory(schema_name):

    schema = load_schema(schema_name)

    for formlet_name, form_def in schema.items():
        FormletClass = type(formlet_name.capitalize(),
                            (Formlet, ),
                            {'schema': form_def})

        formlet = FormletClass(form_def)
        formlet.create_form()
