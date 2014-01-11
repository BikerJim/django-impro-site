"""
Django production settings for easylaughs project.
"""
from .base import *
import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
ADMINS = (
	('Jim Buddin', 'jimbuddin@hotmail.com'),
)
ALLOWED_HOSTS = ['*']
INSTALLED_APPS += ('storages',)

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'easy2.settings.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'easy2.settings.s3utils.StaticRootS3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_DIRECTORY = 'media/'
STATIC_DIRECTORY = 'static/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
#MEDIA_ROOT = MEDIA_URL 
