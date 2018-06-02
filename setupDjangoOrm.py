import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

settings.configure(
    settings.DATABASES,
    settings.INSTALLED_APPS
)

django.setup()
