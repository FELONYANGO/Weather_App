import requests
from dotenv import load_dotenv
import os
import pprint
from dataclasses import dataclass


api_keys=os.getenv('API_KEY')


#wather class for actally cupturing the required data and turning them to the reqyuired format.
@dataclass
class Weather:
    # main:str
    pressure:int
    temperature:float
load_dotenv()

# the function below will return the latitude and longitude while passed with the city name and the api_key
def get_lat_long(city_name,APIkey):
    res= requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={APIkey}')
    
    result= res.json()
    city_info=result[0]
    lat,long = city_info.get('lat'),city_info.get('lon')
    return lat,long


# the curent waether now grabs the cordinate provided by the above 
# functio and givr the waearthe results
def get_current_weather(lat,lon,API_key):
     
     responses=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metrics')

     data= responses.json()
     wather_data= Weather(
           
          temperature=data['main']['temp'],
          pressure=data['main']['pressure']
     )
   
          
     print(wather_data)


# let define a function will take the city name and return the weather
def main(city_name):
     lat,lon=get_lat_long('Toronto',api_keys)
     Weather_d=get_current_weather(lat,lon,api_keys)
     return Weather_d


# the below line of code now allowa our code to run as a script
if __name__ == '__main__':
     lat,lon=get_lat_long('Toronto',api_keys)
     
     get_current_weather(lat,lon,api_keys)