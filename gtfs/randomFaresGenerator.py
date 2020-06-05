from random import randrange
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'gtfs.settings'
django.setup()
from api.models import *


def random_fare():
    return randrange(40, 110, 10)


route_id = "80500010511"

# Using trip ID's to populate the db
trips = ["80105110", "80105111"]

for trip in trips:

    related_trips = Trips.objects.filter(route_id=route_id, trip_id=trip)
    related_stop_times = StopTimes.objects.filter(trip_id__in=related_trips).distinct().values_list('stop_id', flat=True).order_by('stop_sequence')
    related_stops = Stops.objects.filter(stop_id__in=related_stop_times).distinct().values()

    periods = [
        "6:00-7:00",
        "7:00-8:00",
        "8:00-9:00",
        "9:00-10:00",
        "10:00-11:00",
        "11:00-12:00",
        "12:00-13:00",
        "13:00-14:00",
        "14:00-15:00",
        "15:00-16:00",
        "16:00-17:00",
        "18:00-19:00",
    ]

    route_id_instance = Routes.objects.get(route_id=route_id)
    start_point = Stops.objects.get(stop_id=related_stops[0]["stop_id"])

    print(related_stops[0]['stop_id'], related_stops[1]['stop_id'], related_stops[2]['stop_id'])

    for sidx, stop in enumerate(related_stops, start=0):
        end_point = Stops.objects.get(stop_id=stop["stop_id"])

        if (end_point == start_point):
            print(f"Terminus start point: {start_point} end point: {end_point}")
        else:
            for pidx, period in enumerate(periods, start=0):

                price = random_fare()

                Fares.objects.create(price=price, route_id=route_id_instance, origin_id=start_point, destination_id=end_point, period=period)

                print(
                    f"Added: Start point: {start_point}. end_point: {end_point}. period: {period} price: {price}")


    ''' 
    TRUNCATE TABLE fares
    '''
