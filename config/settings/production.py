import django_heroku
import dj_database_url

from .base import *


SECRET_KEY: str = env.str('SECRET_KEY')

DEBUG: bool = bool(env.str('DEBUG'))

ALLOWED_HOST = ['.herokuapp.com']

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Activate Django-Heroku.
django_heroku.settings(locals())