from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('routes/', views.routes, name='routes'),
    path('stops/', views.stops, name='stops'),
    path('trips/', views.trips, name='trips'),
    path('priceVerified/', views.saveVerifiedFares, name='verifiedFares'),
    path('stats/', views.stats, name='stats')
]
