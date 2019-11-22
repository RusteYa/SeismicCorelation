# Create your models here.
import uuid

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class SeismicEvent(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    mag = columns.Double()
    place = columns.Text()
    time = columns.DateTime()
    updated = columns.DateTime()
    tz = columns.SmallInt()
    status = columns.Text()
    tsunami = columns.TinyInt()
    sig = columns.SmallInt()
    net = columns.Text()
    code = columns.Text()
    ids = columns.Text()
    sources = columns.Text()
    types = columns.Text()
    nst = columns.SmallInt()
    dmin = columns.Double()
    rms = columns.Double()
    gap = columns.SmallInt()
    magType = columns.Text()
    type = columns.Text()
    latitude = columns.Double()
    longitude = columns.Double()
    depth = columns.Double()


class Weather(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    latitude = columns.Double()
    longitude = columns.Double()
    time = columns.DateTime()
    precipIntensity = columns.Double()
    precipProbability = columns.Double()
    temperature = columns.Double()
    apparentTemperature = columns.Double()
    dewPoint = columns.Double()
    humidity = columns.Double()
    pressure = columns.Double()
    windSpeed = columns.Double()
    windGust = columns.Double()
    windBearing = columns.Double()
    cloudCover = columns.Double()
    uvIndex = columns.Double()
    visibility = columns.Double()
    ozone = columns.Double()


