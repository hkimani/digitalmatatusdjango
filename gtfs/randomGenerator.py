from random import randrange
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'gtfs.settings'
django.setup()
from api.models import Routes

def random_max():
    return randrange(70, 150, 10)

def random_min():
    return randrange(20, 70, 10)

entries = Routes.objects.all()
for entry in entries :
    entry.max_fare = random_max()
    entry.min_fare = random_min()
    entry.save()