import requests
import json
 
r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
for raw_rsvp in r.iter_lines():
    if raw_rsvp:
        rsvp = json.loads(raw_rsvp)
        print rsvpa