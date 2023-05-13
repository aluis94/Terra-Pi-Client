from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class TerraPiFormTest(LiveServerTestCase):
    #This test will not create a sensor due to invalid form input
    def testinvalidsensorform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to sensors page
        selenium.get('http://localhost:9000/terra-pi/sensors')
        time.sleep(1)
        add = selenium.find_element(By.ID,'add')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        submit_button =selenium.find_element(By.ID,'submit')
        time.sleep(1)
        #submit form
        submit_button.click()
        time.sleep(2)


    #This test will create a new sensor
    def testsensorform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to sensors page
        selenium.get('http://localhost:9000/terra-pi/sensors')
        time.sleep(1)
        add = selenium.find_element(By.ID,'add')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        sensor_name = selenium.find_element(By.ID,'name')
        sensor_type = selenium.find_element(By.ID,'type')
        sensor_gpio1 = selenium.find_element(By.ID,'GPIO1')
        sensor_gpio2 = selenium.find_element(By.ID,'GPIO2')
        sensor_gpio3 = selenium.find_element(By.ID,'GPIO3')
        submit_button =selenium.find_element(By.ID,'submit')

    

        #populate the form with data
        sensor_name.send_keys('DHT11')

        #Select dropdown values
        drop_type= Select(sensor_type)
        drop_type.select_by_index(0)

        drop_gpio1= Select(sensor_gpio1)
        drop_gpio1.select_by_index(21)

        drop_gpio2= Select(sensor_gpio2)
        drop_gpio2.select_by_index(1)

        drop_gpio3= Select(sensor_gpio3)
        drop_gpio3.select_by_index(1)

    

    
        time.sleep(1)
        #submit form
        #submit_button.click()
        time.sleep(2)

    #This test will not create a device due to invalid form input
    def testinvaliddeviceform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to sensors page
        selenium.get('http://localhost:9000/terra-pi/devices')
        time.sleep(1)
        add = selenium.find_element(By.ID,'add')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        submit_button =selenium.find_element(By.ID,'submit')
        time.sleep(1)
        #submit form
        submit_button.click()
        time.sleep(2) 

    #This test will create a new device
    def testdeviceform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to devices page
        selenium.get('http://localhost:9000/terra-pi/devices')
        time.sleep(1)
        add = selenium.find_element(By.ID,'add')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        device_name = selenium.find_element(By.ID,'name')
        device_type = selenium.find_element(By.ID,'type')
        device_gpio1 = selenium.find_element(By.ID,'GPIO1')
        device_gpio2 = selenium.find_element(By.ID,'GPIO2')
        device_gpio3 = selenium.find_element(By.ID,'GPIO3')
        submit_button =selenium.find_element(By.ID,'submit')

    

        #populate the form with data
        device_name.send_keys('Heater1')
        device_type.send_keys('Heater')
        
        #Select dropdown values
        

        drop_gpio1= Select(device_gpio1)
        drop_gpio1.select_by_index(21)

        drop_gpio2= Select(device_gpio2)
        drop_gpio2.select_by_index(1)

        drop_gpio3= Select(device_gpio3)
        drop_gpio3.select_by_index(1)

    

    
        time.sleep(1)
        #submit form
        #submit_button.click()
        time.sleep(2)

    #This test will not create a simple job due to invlid form inputs  
    def testinvalidsimplejobform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to sensors page
        selenium.get('http://localhost:9000/terra-pi/jobs')
        time.sleep(1)
        add = selenium.find_element(By.ID,'addsimple')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        submit_button =selenium.find_element(By.ID,'submit')
        time.sleep(1)
        #submit form
        submit_button.click()
        time.sleep(2) 

    #This test will not create a multi-step (conditional) job due to invlid form inputs  
    def testinvalidmultijobform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to sensors page
        selenium.get('http://localhost:9000/terra-pi/jobs')
        time.sleep(1)
        add = selenium.find_element(By.ID,'addmulti')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        submit_button =selenium.find_element(By.ID,'submit')
        time.sleep(1)
        #submit form
        submit_button.click()
        time.sleep(2) 

    def testsimplejobform(self):
        selenium = webdriver.Chrome()
        #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to jobs page
        selenium.get('http://localhost:9000/terra-pi/jobs')
        time.sleep(1)
        add = selenium.find_element(By.ID,'addsimple')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        job_name = selenium.find_element(By.ID,'name')
        job_description = selenium.find_element(By.ID,'description')
        job_message = selenium.find_element(By.ID,'message')
        job_category = selenium.find_element(By.ID,'category')
        job_device = selenium.find_element(By.ID,'currdevice')
        job_cron_check =selenium.find_element(By.ID,'cronCheck')
        job_cron_every_value =selenium.find_element(By.ID,'cronEveryValue')
        job_cron_every =selenium.find_element(By.ID,'cronEvery')
        submit_button =selenium.find_element(By.ID,'submit')

    

        #populate the form with data
        job_name.send_keys('Send Email Test')
        job_description.send_keys('Send an email')
        job_message.send_keys('This is a test message')
        #Select dropdown values
        job_cron_check.click()

        drop_category= Select(job_category)
        drop_category.select_by_index(2)

        drop_device= Select(job_device)
        drop_device.select_by_index(0)

        drop_cron_every= Select(job_cron_every)
        drop_cron_every.select_by_index(1)

        drop_cron_every_value= Select(job_cron_every_value)
        drop_cron_every_value.select_by_index(5)

        

    
        
    
        time.sleep(1)
        #submit form
        #submit_button.click()
        time.sleep(2)

    def testmultijobform(self):
        selenium = webdriver.Chrome()
         #Choose your url to visit
        selenium.get('http://localhost:9000/terra-pi/')
        time.sleep(1)
        #navigate to jobs page
        selenium.get('http://localhost:9000/terra-pi/jobs')
        time.sleep(1)
        add = selenium.find_element(By.ID,'addmulti')
        add.click()
        time.sleep(1)

        #find the elements you need to submit form
        job_name = selenium.find_element(By.ID,'name')
        job_description = selenium.find_element(By.ID,'description')
        job_message = selenium.find_element(By.ID,'message')
        job_category = selenium.find_element(By.ID,'category')
        job_device = selenium.find_element(By.ID,'currdevice')
        job_cron_check =selenium.find_element(By.ID,'cronCheck')
        job_cron_every_value =selenium.find_element(By.ID,'cronEveryValue')
        job_cron_every =selenium.find_element(By.ID,'cronEvery')
        submit_button =selenium.find_element(By.ID,'submit')

    

        #populate the form with data
        job_name.send_keys('TempNotificationOff')
        job_description.send_keys('Read temp, send notification, turn device off')
        job_message.send_keys('This is a test message')
        #Select dropdown values
        job_cron_check.click()

        drop_category= Select(job_category)
        drop_category.select_by_index(2)

        drop_device= Select(job_device)
        drop_device.select_by_index(0)

        drop_cron_every= Select(job_cron_every)
        drop_cron_every.select_by_index(1)

        drop_cron_every_value= Select(job_cron_every_value)
        drop_cron_every_value.select_by_index(5)

        

    
        
    
        time.sleep(1)
        #submit form
        #submit_button.click()
        time.sleep(2)
       