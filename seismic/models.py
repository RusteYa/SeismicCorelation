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
    lon = columns.Double()
    lat = columns.Double()
    dt = columns.DateTime()
    temp = columns.Double()
    pressure = columns.Double()
    humidity = columns.Double()
    visibility = columns.Double()
    windSpeed = columns.Double()
    windGust = columns.Double()
    windDeg = columns.Double()
    clouds = columns.Double()


class Correlation(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    dt = columns.DateTime()
    val = columns.Double()

