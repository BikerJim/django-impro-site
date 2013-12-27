"""
Django staging server (RaspberryPi) settings for easylaughs project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import *

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'easylaughs',
        'USER': 'django',
        'PASSWORD': 'ww2cx9k',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = [*,]
