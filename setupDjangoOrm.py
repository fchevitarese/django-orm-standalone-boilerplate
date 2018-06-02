import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dbname',
            'HOST': 'hostname',
            'PORT': 'port',
            'USER': 'user',
            'PASSWORD': 'pass',
        }
    },
    INSTALLED_APPS=[
        'installedapp',
    ]
)
django.setup()
