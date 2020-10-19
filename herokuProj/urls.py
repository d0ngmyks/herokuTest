from django.contrib import admin
from django.urls import path
from . import views
# from django.conf import settings

urlpatterns = [
    path('', views.HomepageTemplateView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
]
