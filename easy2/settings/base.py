"""
Django settings for easy2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from unipath import Path
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
	""" Get the env variable or return exception """
	try:
		return os.environ[var_name]
	except KeyError:
		error_msg = "Set the %s environment variable" % var_name
		raise ImproperlyConfigured(error_msg)

PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (PROJECT_DIR.child("assets"),)
TEMPLATE_DIRS = (PROJECT_DIR.child("templates"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Additions for all_auth
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)
# Authentication
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
'facebook': {
    'SCOPE':['email','publish_stream'],
    'METHOD':'js_sdk'
    }
}

AUTHENTICATION_BACKENDS = (
#    # Needed to login by username in Django Admin
    "django.contrib.auth.backends.ModelBackend",
#    # Allauth specific auth methods, like login by email
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # allauth providers
    'allauth.socialaccount.providers.facebook',
    'south',
    'events',
    'booking',
    'home',
    'casting',
#    'allauth.socialaccount.providers.google',
#    'allauth.socialaccount.providers.twitter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'easy2.urls'
WSGI_APPLICATION = 'easy2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
