import meetup.api
import meetup_config
import requests
import time
import os
#
# request_url = 'https://api.meetup.com/2/members?group_id={}&key={}'
#
config = meetup_config.Config
client = meetup.api.Client(config.SECRET_KEY)
# noisebridges = client.GetOpenVenues(state="California",
#                                     text="Noisebridge",
#                                     country="United States",
#                                     zip=94110).results

tformat = "%Y-%m-%d %H:%M:%S"
evt_datetime = "2018-11-10 13:30:00"

evt_time = int(time.mktime(time.strptime(evt_datetime, tformat)))
client.Events(
    {"name": "meetup name",
     "venue_id": 2540661,
     "how_to_find_us": "boilerplate + room",
     "urlname": "Noisebridge",
     "time": int(time.mktime(time.strptime(evt_datetime, tformat)))*1000}
)
