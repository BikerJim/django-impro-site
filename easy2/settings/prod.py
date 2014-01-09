"""
Django production settings for easylaughs project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import *
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")
#DB_PASSWORD = get_env_variable("DB_PASSWORD")
#DB_NAME = get_env_variable("DB_NAME")
#DB_USER = get_env_variable("DB_USER")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
ADMINS = (
	('Jim Buddin', 'jimbuddin@hotmail.com'),
)

#EMAIL_HOST = 

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'DB_NAME',
#        'USER': 'DB_USER',
#        'PASSWORD': 'DB_PASSWORD',
#        'HOST': '',
#        'PORT': '',
#    }
#}
ALLOWED_HOSTS = ['*']
