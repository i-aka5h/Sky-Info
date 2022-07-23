from tkinter import E
from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from dotenv import load_dotenv
import os

# Create your views here.

def index(request):
    
    if 'city' in request.POST :
        city=request.POST['city']
        placeholder=city
    else:
        placeholder='Enter City'
        messages.error(request,'kuchh bhi likh sakte hai :) ')
        return render(request,'weatherapp/index.html')
    
    url= 'https://api.openweathermap.org/data/2.5/weather'
    
    # Enter your api key here
    api= os.getenv('api')
    
    parameters={
        'q':city,
        'appid' : api,
        'units' : 'metric'
    }
    
    day=datetime.date.today()
    res = requests.get(url,parameters).json()
    
    if(res['cod']==200):
        temperature=res['main']['temp']
        icon=res['weather'][0]['icon']
        description=res['weather'][0]['main']
        pressure=res['main']['pressure']
        try:
            country=res['sys']['country']
        except:
            country="N/A"
        humidity=res['main']['humidity']
    
    
        return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temperature':temperature, 'day':day, 'country':country,'pressure':pressure,'humidity':humidity ,'city':city, 'placeholder':placeholder})


    elif(res['cod']=='404'):
        messages.info(request, 'City Not Found !')
        return render(request,'weatherapp/index.html')
    else:
        messages.info(request,'Please Enter a city name!')
        return render(request,'weatherapp/index.html')
