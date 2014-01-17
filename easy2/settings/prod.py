"""
Django production settings for easylaughs project.
"""
from .base import *
import os
import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False)
TEMPLATE_DEBUG = os.environ.get("TEMPLATE_DEBUG", False)

EMAIL_HOST = os.environ['MAILTRAP_HOST']
EMAIL_HOST_USER = os.environ['MAILTRAP_USER_NAME']
EMAIL_HOST_PASSWORD = os.environ['MAILTRAP_PASSWORD']
EMAIL_PORT = os.environ['MAILTRAP_PORT']
EMAIL_USE_TLS = False

ADMINS = (
	('Jim Buddin', 'jimbuddin@hotmail.com'),
)
ALLOWED_HOSTS = ['*']
INSTALLED_APPS += ('storages',)

DEFAULT_FILE_STORAGE = 'easy2.settings.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'easy2.settings.s3utils.StaticRootS3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_DIRECTORY = 'media/'
STATIC_DIRECTORY = 'static/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
