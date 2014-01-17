"""
Django local settings for easy2 project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import *

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )
ALLOWED_HOSTS = []

import debug_toolbar
from django.conf.urls import patterns, include, url
from easy2.urls import urlpatterns
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$',
    'django.views.static.serve', {
    'document_root': MEDIA_ROOT}),
    (r'^__debug__/', include(debug_toolbar.urls)),
)

