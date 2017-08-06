from .settings import *
from os import environ
import dj_database_url
import os

DATABASE_URL = (
     'postgres://pefykhgpynkiop:ec68d402632259d226a96da' +
     '6f7b19134939d98c119f13cdf3af8e63ddedb4baa@e' +
     'c2-107-20-255-96.compute-1.amazonaws.com:5432/dalutb2uime2hc')

DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'stas-mysite'
STATICFILES_STORAGE = 'mysite.s3utils.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'mysite.s3utils.MediaRootS3BotoStorage'
S3_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('storages',)

DEBUG = False


