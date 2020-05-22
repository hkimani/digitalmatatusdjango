from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('data/', views.data_all, name='all_data'),
]
