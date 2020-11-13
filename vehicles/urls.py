from django.urls import path
from . import views


urlpatterns = [
    # path('', views.VehiclesListView.as_view(), name='vehicles_list'),
    path('', views.vehicles_app, name='vehicles_list'),
    path('pipe-channel', views.pipe_channel, name='pipe_channel'),
]

from .dash import index
from .dash import test_pipe_channel
