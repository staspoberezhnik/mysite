from .settings import *
from os import environ
import dj_database_url

DATABASE_URL = (
     'postgres://pefykhgpynkiop:ec68d402632259d226a96da' +
     '6f7b19134939d98c119f13cdf3af8e63ddedb4baa@e' +
     'c2-107-20-255-96.compute-1.amazonaws.com:5432/dalutb2uime2hc')


DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
