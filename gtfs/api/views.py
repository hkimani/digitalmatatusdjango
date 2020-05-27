from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.

def root(request):
    response_data = {
        "success": "true",
        "message": "Server is live"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def routes(request):

    if request.method == 'GET':
        current_page = int(request.GET.getlist('page')[0])
        page_count = int(request.GET.getlist('page_count')[0])

        query_range_start = (page_count * current_page) - page_count
        query_range_end = (page_count * current_page)

        print(query_range_start, query_range_end)

        try:
            routes = list(Routes.objects.all()[
                          query_range_start:query_range_end].values())
            total_routes = Routes.objects.all().count()

        except Exception as e:
            response_data = {
                "success": "false",
                "message": f"{e}"
            }
        else:
            response_data = {
                "success": "True",
                "message": f"Successfully retireved page: {current_page} data",
                "info": {"routes": routes, "total": total_routes}
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def stops(request):

    def listToDict(lst):
        fares = { lst[i]['destination_id']: lst[i] for i in range(0, len(lst)) }
        return fares

    # Equivalent SQL Query
    '''
    SELECT stop_id, stop_name FROM stops WHERE stop_id IN 
    ( SELECT DISTINCT stop_id FROM stop_times WHERE trip_id IN 
    ( SELECT trip_id FROM trips WHERE route_id = 80500010511))
    '''

    # Using Join
    '''
    SELECT DISTINCT stops.stop_id, stops.stop_name
    FROM trips
    INNER JOIN stop_times ON stop_times.trip_id = trips.trip_id
    INNER JOIN stops ON stops.stop_id = stop_times.stop_id
    WHERE route_id = <route_id>;
    '''

    if request.method == 'GET':
        route_id = request.GET.getlist('route_id')[0];
        trip_id = request.GET.getlist('trip_id')[0];
        current_page = int(request.GET.getlist('page')[0]);
        page_count = int(request.GET.getlist('page_count')[0]);

        query_range_start = (page_count * current_page) - page_count;
        query_range_end = (page_count * current_page);

        try:
            related_trips = Trips.objects.filter(route_id=route_id, trip_id=trip_id)
            related_stop_times = StopTimes.objects.filter(trip_id__in=related_trips).distinct().values_list('stop_id', flat=True).order_by('stop_sequence')
            related_stops = Stops.objects.filter(stop_id__in=related_stop_times).distinct()
            related_fares = Fares.objects.filter(origin_id__in=related_stops, destination_id__in=related_stops).distinct().values('price', 'route_id', 'origin_id', 'destination_id', 'period')
            total_stops = Stops.objects.filter(stop_id__in=related_stop_times).distinct().count()

        except Exception as e:
            response_data = {
                "success": "false",
                "message": f"{e}"
            }
        else:
            response_data = {
                "success": "True",
                "message": "Successfully retireved stops",
                "info": { 
                    "total_stops": total_stops, 
                    "stops": list(related_stops.values()[query_range_start:query_range_end]), 
                    "stop_times": list(related_stop_times.values())[query_range_start:query_range_end],
                    "fares": list(related_fares[query_range_start:query_range_end])
                    }
            }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def trips(request):
    if request.method == "GET":
        route_id = request.GET.getlist('route_id')[0];

        try:
            related_trips = Trips.objects.filter(route_id=route_id)

        except Exception as e:
            response_data = {
                "success": "false",
                "message": f"{e}"
            }
        else:
            response_data = {
                "success": "True",
                "message": "Successfully retireved trips",
                "info": {"trips": list(related_trips.values())}
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def saveVerifiedFares(request):
    if request.method == "POST":

        # # Params
        route_id = request.POST.get("route_id")
        origin_id = request.POST.get("origin_id")
        destination_id = request.POST.get("destination_id")
        price = request.POST.get("price")

        try:
            route_instance = Routes.objects.get(route_id=route_id)
            origin_instance = Stops.objects.get(stop_id=origin_id)
            destination_instance = Stops.objects.get(stop_id=destination_id)

            fare_price = Fares(route_id=route_instance, origin_id=origin_instance, destination_id=destination_instance, price=price)
            fare_price.save();

        except Exception as e:
            response_data = {
                "success": False,
                "message": f"{e}"
            }
        else:
            response_data = {
                "success": True,
                "message": "Successfully saved fare price",
            }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


