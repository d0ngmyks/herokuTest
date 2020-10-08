from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageTemplateView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
]
