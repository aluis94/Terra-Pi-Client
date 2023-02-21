from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('home/', views.home_page),
    path('sensors/', views.sensors_page),
    path('sensor/', views.sensor_page),
    path('devices/', views.devices_page),
    path('about/', views.about_page),
]