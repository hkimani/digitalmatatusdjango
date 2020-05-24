from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
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
        route_id = request.GET.getlist('route_id')[0]

        response = None

        try:
            related_trips = Trips.objects.filter(route_id=route_id)
            related_stop_times = StopTimes.objects.filter(trip_id__in=related_trips).order_by(
                'stop_id').distinct().values_list('stop_id', flat=True)
            related_stops = Stops.objects.filter(
                stop_id__in=related_stop_times).order_by('stop_id').distinct()
            response = related_stop_times.values()

        except Exception as e:
            response_data = {
                "success": "false",
                "message": f"{e}"
            }
        else:
            response_data = {
                "success": "True",
                "message": "Successfully retireved stops",
                "info": {"trips": list(related_trips.values()), "stops": list(response), "length": len(list(response))}
            }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def trips(request):
    if request.method == "GET":
        route_id = request.GET.getlist('route_id')[0]

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
