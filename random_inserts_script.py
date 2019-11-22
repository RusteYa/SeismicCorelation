import os
import random
import string
import time
from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SeismicCorelation.settings")
django.setup()

from seismic.models import SeismicEvent, Weather

if __name__ == '__main__':
    random_name = lambda length: ''.join(random.sample(string.ascii_letters, length))

    events = []
    weathers = []

    for i in range(1000):
        event = SeismicEvent()
        event.mag = random.uniform(0, 10)
        event.place = random_name(20)
        event.time = datetime.now()
        event.updated = datetime.now()
        event.tz = random.randint(0, 10)
        event.status = random_name(20)
        event.tsunami = random.randint(0, 10)
        event.sig = random.randint(0, 10)
        event.net = random_name(20)
        event.code = random_name(20)
        event.ids = random_name(20)
        event.sources = random_name(20)
        event.types = random_name(20)
        event.nst = random.randint(0, 10)
        event.dmin = random.random() * 10
        event.rms = random.random() * 10
        event.gap = random.randint(0, 10)
        event.magType = random_name(10)
        event.type = random_name(10)
        event.latitude = random.random() * 10
        event.longitude = random.random() * 10
        event.depth = random.random() * 10

        weather = Weather()
        weather.latitude = random.random() * 10
        weather.longitude = random.random() * 10
        weather.time = datetime.now()
        weather.precipIntensity = random.random() * 10
        weather.precipProbability = random.random() * 10
        weather.temperature = random.random() * 10
        weather.apparentTemperature = random.random() * 10
        weather.dewPoint = random.random() * 10
        weather.humidity = random.random() * 10
        weather.pressure = random.random() * 10
        weather.windSpeed = random.random() * 10
        weather.windGust = random.random() * 10
        weather.windBearing = random.random() * 10
        weather.cloudCover = random.random() * 10
        weather.uvIndex = random.random() * 10
        weather.visibility = random.random() * 10
        weather.ozone = random.random() * 10

        events.append(event)
        weathers.append(weather)

    start_time = time.time()

    for e in events:
        e.save()
    for w in weathers:
        w.save()

    print("--- %s seconds ---" % (time.time() - start_time))
