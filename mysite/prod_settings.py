from .settings import *
from os import environ
import dj_database_url


DATABASES['default'] = dj_database_url.config()

SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = False

