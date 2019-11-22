import sched
import time

import requests

#schedul = sched.scheduler(time.time, time.sleep)

SEISMIC_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
LATITUDE = 35
LONGITUDE = -117
MAXRADIUSKM = 200


def get_seismic():
    data = requests.get(SEISMIC_URL, params={
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "maxradiuskm": MAXRADIUSKM,
        "format": "geojson"
    })
    print(data.json())


#schedul.enter(300, 1, get_seismic(), (schedul,))
#schedul.run()

get_seismic()
