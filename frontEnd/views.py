from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import appHelper


# Create your views here.
def home_page(request):
    #do stuff
    #send emails
    return render(request, 'home.html',{'name':'albert'})

### Devices###
def devices_page(request):
    #do stuff
    #send emails
    response = requests.get("http://127.0.0.1:8080/device/view-all?category=device")
    devices = response.json()
    response = requests.get("http://127.0.0.1:8080/device/view-all?category=notification")
    notifications = response.json()
    return render(request, 'devices.html',{'devices':devices, 'notifications':notifications})
    

def new_device_page(request):
    #do stuff
    #send emails
    GPIOs = appHelper.createGPIOList()
    return render(request, 'device.html',{'GPIOs':GPIOs})

def edit_device_page(request,id):
    #do stuff
    #send emails
    response = requests.get("http://127.0.0.1:8080/device/view/"+id)
    device = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'device.html',{'device':device,'GPIOs':GPIOs})

 ###Sensors###  
def sensors_page(request):
    #do stuff
    #send emails
    response = requests.get("http://127.0.0.1:8080/device/view-all?category=sensor")
    devices = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensors.html',{'devices':devices})
    

def new_sensor_page(request):
    #do stuff
    #send emails
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensor.html',{'GPIOs':GPIOs})

def edit_sensor_page(request,id):
    #do stuff
    #send emails
    response = requests.get("http://127.0.0.1:8080/device/view/"+id)
    device = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensor.html',{'device':device,'GPIOs':GPIOs})

### Jobs ###
def jobs_page(request):
    #dostuff
    response = requests.get("http://127.0.0.1:8080/job/view-all")
    jobs = response.json()
    return render(request, 'jobs.html',{'jobs':jobs})

def new_simple_job_page(request):
    #dostuff
    return render(request, 'job_simple.html',{'job':''})

def new_multi_job_page(request):
    #dostuff
    return render(request, 'job_multi.html',{'job':''})

def edit_simple_job_page(request, id):
    #dostuff
    response = requests.get("http://127.0.0.1:8080/job/view/"+id)
    jobs = response.json()
    return render(request, 'job_simple.html',{'':''})

def edit_multi_job_page(request, id):
    #dostuff
    response = requests.get("http://127.0.0.1:8080/job/view/"+id)
    jobs = response.json()
    return render(request, 'job_multi.html',{'':''})


### About ###
def about_page(request):
    #do stuff
    #send emails
    return render(request, 'about.html',{'name':'albert'})

