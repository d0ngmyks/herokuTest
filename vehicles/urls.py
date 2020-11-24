from django.urls import path
from . import views


urlpatterns = [
    # path('', views.VehiclesListView.as_view(), name='vehicles_list'),
    path('', views.vehicles_app, name='vehicles_list'),
    path('pipe-channel', views.pipe_channel, name='pipe_channel'),

    path('dash2', views.load_main_layout, name='vehicles_dash2'),
]

from .dash import index
from .dash import test_pipe_channel

from .dash2 import index
