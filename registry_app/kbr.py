import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'registry.settings'

django.setup()

from models import RegistryModel
