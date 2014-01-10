"""
Django production settings for easylaughs project.
"""
from .base import *
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

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
