from random import randrange
from api.models import Routes

def random_max():
    return randrange(70, 150, 10)

def random_min():
    return randrange(20, 80, 10)

entries = Routes.objects.all()
for entry in entries :
    entry.max_fare = random_max()
    entry.min_fare = random_min()
    entry.save()