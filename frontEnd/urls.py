from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('home/', views.home_page),
    path('devices/', views.devices_page),
    path('device/new/', views.new_device_page),
    path('device/<id>/', views.edit_device_page),
    path('sensor/new/', views.new_sensor_page),
    path('sensor/<id>/', views.edit_sensor_page),
    path('sensors/', views.sensors_page),
    path('job/new/simple/', views.new_simple_job_page),
    path('job/new/multi/', views.new_multi_job_page),
    path('job/simple/<id>/', views.edit_simple_job_page),
    path('job/multi/<id>/', views.edit_multi_job_page),
    path('jobs/', views.jobs_page),
    path('about/', views.about_page),
]