import datetime
import time
import numpy
import requests
from seismic.models import SeismicEvent, Weather, Correlation

LATITUDE = 35
LONGITUDE = -117
MAXRADIUSKM = 200
SEISMIC_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
APPID = '048532a13c4497741ec64e2d46f4df39'


def insert_seismic():
    starttime = time.time()
    while True:
        data = requests.get(SEISMIC_URL, params={
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "maxradiuskm": MAXRADIUSKM,
            "starttime": (datetime.datetime.fromtimestamp(starttime) - datetime.timedelta(minutes=5)).isoformat(),
            "format": "geojson"
        })
        starttime = time.time()

        if 'features' in data.json():
            events = data.json()['features']

            for e in events:
                event = SeismicEvent()
                event.mag = e['properties']['mag']
                event.place = e['properties']['place']
                event.time = datetime.datetime.fromtimestamp(e['properties']['time']/1000)
                event.updated = datetime.datetime.fromtimestamp(e['properties']['updated']/1000)
                event.tz = e['properties']['tz']
                event.status = e['properties']['status']
                event.tsunami = e['properties']['tsunami']
                event.sig = e['properties']['sig']
                event.net = e['properties']['net']
                event.code = e['properties']['code']
                event.ids = e['properties']['ids']
                event.sources = e['properties']['sources']
                event.types = e['properties']['types']
                event.nst = e['properties']['nst']
                event.dmin = e['properties']['dmin']
                event.rms = e['properties']['rms']
                event.gap = e['properties']['gap']
                event.magType = e['properties']['magType']
                event.type = e['properties']['type']
                event.longitude = e['geometry']['coordinates'][0]
                event.latitude = e['geometry']['coordinates'][1]
                event.depth = e['geometry']['coordinates'][2]
                event.save()

        time.sleep(300.0 - time.time() + starttime)


def insert_weather():
    starttime = time.time()
    while True:
        data = requests.get(WEATHER_URL, params={
            "lat": LATITUDE,
            "lon": LONGITUDE,
            "appid": APPID
        })
        w = data.json()

        if w['cod'] == 200:
            weather = Weather()
            weather.lon = w['coord']['lon']
            weather.lat = w['coord']['lat']
            weather.dt = datetime.datetime.now() - datetime.timedelta(hours=3)
            weather.temp = w['main']['temp']
            weather.pressure = w['main']['pressure']
            weather.humidity = w['main']['humidity']
            weather.visibility = w['visibility']
            weather.windSpeed = w['wind']['speed']
            weather.windGust = w['wind']['deg']
            weather.windDeg = w['wind']['gust']
            weather.clouds = w['clouds']['all']
            weather.save()

        time.sleep(1.0 - ((time.time() - starttime) % 1.0))


def count_correlation():
    starttime = time.time()
    while True:
        events = SeismicEvent.objects.all()
        event_magnitudes = []
        wind_speeds = []
        for event in events:
            gte = datetime.datetime(
                year=event.time.year,
                month=event.time.month,
                day=event.time.day,
                hour=event.time.hour,
                minute=event.time.minute,
                second=event.time.second
            )
            lte = gte + datetime.timedelta(seconds=1)
            weather = Weather.objects.filter(dt__gte=gte, dt__lte=lte).first()
            event_magnitudes.append(event.mag)
            if weather is not None:
                wind_speeds.append(weather.windSpeed)
            else:
                lte = gte + datetime.timedelta(minutes=1)
                weather = Weather.objects.filter(dt__gte=gte, dt__lte=lte).first()
                if weather is not None:
                    wind_speeds.append(weather.windSpeed)
                else:
                    wind_speeds.append(0)

        cor = Correlation()
        cor.val = numpy.corrcoef(event_magnitudes, wind_speeds)[0, 1]
        cor.dt = datetime.datetime.now() - datetime.timedelta(hours=3)
        cor.save()

        time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))

