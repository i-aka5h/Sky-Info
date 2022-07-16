from django.shortcuts import render
import requests
import datetime
from dotenv import load_dotenv
import os

# Create your views here.

def index(request):
    
    if 'city' in request.POST :
        city=request.POST['city']
        placeholder=city;
    else:
        city='noida'
        placeholder='Enter City'
    
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
    
    temperature=res['main']['temp']
    icon=res['weather'][0]['icon']
    description=res['weather'][0]['main']
    pressure=res['main']['pressure']
    country=res['sys']['country']
    humidity=res['main']['humidity']
    
    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temperature':temperature, 'day':day, 'country':country,'pressure':pressure,'humidity':humidity ,'city':city, 'placeholder':placeholder})