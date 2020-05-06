import django_heroku
import dj_database_url

from .base import *


SECRET_KEY: str = env.str('SECRET_KEY')

DEBUG: bool = bool(env.int('DEBUG'))

TEST_RUNNER: str = 'django_heroku.HerokuDiscoverRunner'

# Activate Django-Heroku.
django_heroku.settings(locals())
