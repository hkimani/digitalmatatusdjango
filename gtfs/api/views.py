from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import *
import json


def root(request):
    response_data = {
        "success": "true",
        "message": "Server is live"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Create your views here.


def data_all(request):

    if request.method == 'GET':
        current_page = int(request.GET.getlist('page')[0])
        page_count = int(request.GET.getlist('page_count')[0])

        query_range_start = (page_count * current_page) - page_count
        query_range_end = (page_count * current_page) - 1

        print(query_range_start, query_range_end)

        routes = None;

        try:
            routes = list(Routes.objects.all()[query_range_start:query_range_end].values())
        except Exception as e:
            response_data = {
                "success": "false",
                "message": e
            }
        else:
            response_data = {
                "success": "True",
                "message": f"Successfully retireved page: {current_page} data",
                "info": routes
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
