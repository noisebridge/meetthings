class EventMetadataHandeler:

    def __init__(self):
        pass


class Event:

    id = 0
    name = ""
    desc = ""
    venue_id = 0
    published = False
    start_datetime = ""
    end_datetime = ""

    rrule = None
    metadata = None  # various calendar specific metadata?

    def __init__(self):
        pass


class Venue:

    address = None
    id = None

    metadata = None

    def __init_(meetup_venue=None):
        if meetup_venue:
            venue_from_meetup(meetup_venue)

    def venue_from_meetup(venue_data):
        for k, v in ven_data.items():
            setattr(self, k, v)
