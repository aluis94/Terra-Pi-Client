from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    #do stuff
    #send emails
    return render(request, 'home.html',{'name':'albert'})

def sensors_page(request):
    #do stuff
    #send emails
    return render(request, 'sensors.html',{'name':'albert'})

def sensor_page(request):
    #do stuff
    #send emails
    return render(request, 'sensor.html',{'name':'albert'})

def devices_page(request):
    #do stuff
    #send emails
    return render(request, 'devices.html',{'name':'albert'})

def about_page(request):
    #do stuff
    #send emails
    return render(request, 'about.html',{'name':'albert'})