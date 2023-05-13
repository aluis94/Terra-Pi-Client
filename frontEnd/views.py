from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import appHelper

serverURL = "http://localhost:8080/"
# Create your views here.
def home_page(request):
    #do stuff
    #send emails
    response = requests.get(serverURL+"data-entry/view-all")
    dataEntry = response.json()
    return render(request, 'home.html',{'dataEntry':dataEntry,'serverURL':serverURL})

### Devices###
def devices_page(request):
    #do stuff
    #send emails
    response = requests.get(serverURL+"device/view-all?category=device")
    devices = response.json()
    response = requests.get(serverURL+"device/view-all?category=notification")
    notifications = response.json()
    return render(request, 'devices.html',{'devices':devices, 'notifications':notifications,'serverURL':serverURL})
    

def new_device_page(request):
    #do stuff
    #send emails
    GPIOs = appHelper.createGPIOList()
    return render(request, 'device.html',{'GPIOs':GPIOs,'serverURL':serverURL})

def edit_device_page(request,id):
    #do stuff
    #send emails
    response = requests.get(serverURL+"device/view/"+id)
    device = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'device.html',{'device':device,'GPIOs':GPIOs,'serverURL':serverURL})

 ###Sensors###  
def sensors_page(request):
    #do stuff
    #send emails
    response = requests.get(serverURL+"device/view-all?category=sensor")
    devices = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensors.html',{'devices':devices,'serverURL':serverURL})
    

def new_sensor_page(request):
    #do stuff
    #send emails
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensor.html',{'GPIOs':GPIOs,'serverURL':serverURL})

def edit_sensor_page(request,id):
    #do stuff
    #send emails
    response = requests.get(serverURL+"device/view/"+id)
    device = response.json()
    GPIOs = appHelper.createGPIOList()
    return render(request, 'sensor.html',{'device':device,'GPIOs':GPIOs,'serverURL':serverURL})

### Jobs ###
def jobs_page(request):
    #dostuff
    response = requests.get(serverURL+"job/view-all")
    jobs = response.json()
    return render(request, 'jobs.html',{'jobs':jobs,'serverURL':serverURL})

def new_simple_job_page(request):
    #dostuff
    
    return render(request, 'job_simple.html',{'serverURL':serverURL})

def new_multi_job_page(request):
    #dostuff
    return render(request, 'job_multi.html',{'serverURL':serverURL})

def edit_simple_job_page(request, id):
    #dostuff
    response = requests.get(serverURL+"job/view/"+id)
    job = response.json()
    return render(request, 'job_simple.html',{'job':job,'serverURL':serverURL})

def edit_multi_job_page(request, id):
    #dostuff
    response = requests.get(serverURL+"job/view/"+id)
    job = response.json()
    return render(request, 'job_multi.html',{'job':job,'serverURL':serverURL})


### About ###
def about_page(request):
    #do stuff
    #send emails
    return render(request, 'about.html',{'serverURL':serverURL})

