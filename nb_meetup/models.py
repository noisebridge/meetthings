# import meetup.api
# import meetup_config
# import requests
import time
import os
#
# request_url = 'https://api.meetup.com/2/members?group_id={}&key={}'
#
# config = meetup_config.Config
# client = meetup.api.Client(config.SECRET_KEY)
# group = client.GetGroup({'urlname': config.GROUP_URLNAME})
#
# info = requests.get(request_url.format(group_info.id, config.SECRET_KEY))
#
# # e.g.
# info.json()
#
# noisebridges = client.GetOpenVenues(state="California",
#                                     text="Noisebridge",
#                                     country="United States",
#                                     zip=94110).results
#

tformat = "%Y-%m-%d %H:%M:%S"
evt_datetime = "2018-11-10 13:30:00"

evt_time = int(time.mktime(time.strptime(evt_datetime, tformat)))
event = {
    'description': "A fund thing to do",
    'duration': 10,
    'email_reminders': True,
    'group_id': 1556336,
    'group_urlname': "noisebridge",
    'guest_limit': 60,
    'host_instructions': None,
    'hosts': None,
    'how_to_find_us': "Upstairs to church",
    'name': "A thing with the thing",
    'publish_status': None,
    'question_{n}': None,
    'rsvp_alerts': True,
    'rsvp_close': None,
    'rsvp_limit': 60,
    'rsvp_open': None,
    'simple_html_description': "A thing with <h1>Another</h1> thing",
    'time': evt_time,
    'venue_id': 2540661,
    'venue_visibility': "public",
    'waitlisting': "off",
    'why': "Because we can"}

cliente.Events(
    {"name": "meetup name",
     "venue_id": 2540661,
     "how_to_find_us": "boilerplate + room",
     "urlname": "Noisebridge",
     "time": int(time.mktime(time.strptime(evt_datetime, tformat)))*1000}
)
