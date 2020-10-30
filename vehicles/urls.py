from django.urls import path
from . import views


urlpatterns = [
    path('', views.VehiclesListView.as_view(), name='vehicles_list'),
]

from .dash import index
