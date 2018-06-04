import os
import django
from django.conf import settings

from standalone.settings import DATABASES, INSTALLED_APPS

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


settings.configure(
    DATABASES=DATABASES,
    INSTALLED_APPS=INSTALLED_APPS
)
django.setup()
