"""
Django staging server (RaspberryPi) settings for easylaughs project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#from unipath import Path
from .base import *

#SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")
SECRET_KEY = "psst-this-is-my-secret-key-shhh"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = '/var/www/easylaughs.nl/static/'
MEDIA_ROOT = '/var/www/easylaughs.nl/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

ADMINS = (
	('Jim Buddin', 'jimbuddin@hotmail.com'),
)

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

ALLOWED_HOSTS = ['192.168.1.113']
