The directory `schema` holds json files which describe data requirements. Right now only `meetthings.json` is important.

The model is:

`form_name: { field name : {'type': field type, 'validators': validator, ...}}}`

A dictionary of the forms is passed to the rendered, and used by the templates.

Some extra information is required. In a file in the `instance` directory put this in `meetup-test-api.cfg`:

```python
URLNAME="Meetup-API-Testing"

SECRET_KEY='80b2c1c4-5024-49c2-816f-3c449109c53'
MEETUP_API_SECRET='get your own'

GROUP_ID="1556336"
GROUP_URLNAME="Meetup-API-Testing"
URLNAME="Meetup-API-Testing"

VENUE_ID="4567"

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
```
you’ll need to install the package:
`pip install -e .`

this should theoretically work at this stage:
`$ flask run`

which will lauch a wsgi on port 5000. you can go to localhost:5000/NewEvent to see if everything went well.
