# Every setting in base.py can be overloaded by redefining it here.
from .base import *

# These are required for Django to function properly. Don't touch.
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
SECRET_KEY = '{{ secret_key }}'

# This is where css/images will be placed for your webserver to read
STATIC_ROOT = "/var/www/{{ project_name }}/static/"

# Change this to change the name of the auth site displayed
# in page titles and the site header.
SITE_NAME = '{{ project_name }}'

# Change this to enable/disable debug mode, which displays
# useful error messages but can leak sensitive data.
DEBUG = False

# Add any additional apps to this list.
INSTALLED_APPS += [
    
]

# Enter credentials to use MySQL/MariaDB. Comment out to use sqlite3
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alliance_auth',
    'USER': '',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com
# Select publicData and all available scopes starting with esi-
ESI_SSO_CLIENT_ID = ''
ESI_SSO_CLIENT_SECRET = ''
ESI_SSO_CALLBACK_URL = ''

# Emails are validated before new users can log in.
# It's recommended to use a free service like SparkPost or Mailgun to send email.
# https://www.sparkpost.com/docs/integrations/django/
# Set the default from email to something like 'noreply@example.com'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''

#######################################
# Add any custom settings below here. #
#######################################