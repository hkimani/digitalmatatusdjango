from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def data_all(request):
    response_data = {
        "success": "true",
        "message": "All gtfs data"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")