"""
Django staging server (RaspberryPi) settings for easylaughs project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
from .base import *

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child("media")
#STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (PROJECT_DIR.child("assets"),)
TEMPLATE_DIRS = (PROJECT_DIR.child("templates"),)

STATIC_ROOT = '/var/www/raspberrypi.jim/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

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

ALLOWED_HOSTS = ['*',]
