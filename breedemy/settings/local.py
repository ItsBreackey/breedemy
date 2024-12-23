from .base import *
import os
import environ
env = environ.Env()
environ.Env.read_env()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'breedemydb',
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': "Leblanc94",
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}
