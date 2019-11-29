"""
WSGI config for SeismicCorelation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from threading import Thread

from django.core.wsgi import get_wsgi_application

import insert_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SeismicCorelation.settings')

application = get_wsgi_application()

thread_seismic = Thread(target=insert_data.insert_seismic, daemon=True)
thread_weather = Thread(target=insert_data.insert_weather, daemon=True)
thread_correlation = Thread(target=insert_data.count_correlation, daemon=True)

thread_seismic.start()
thread_weather.start()
thread_correlation.start()

