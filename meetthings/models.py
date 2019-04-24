class MeetingObject:

    def __init__(self, schema):
        self.metadata = schema[self.schema_name]

    def set_schema(self, schema):
        self.metadata = schema[self.name]


class Event(MeetingObject):
    schema_name = 'event'


class Venue(MeetingObject):
    schema_name = 'venue'


class Rsvp(MeetingObject):
    schema_name = 'rsvp'


class Address(MeetingObject):
    schema_name = 'address'
