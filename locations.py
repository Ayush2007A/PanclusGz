import requests
from pprint import pprint
from countryinfo import CountryInfo
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();
def print_weather(result,city):
	print("{}'s accurate temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
def get_weather(place):
    '''will give the weather conditions of the place'''
    city=place
    print()
    try:
        query='q='+city;
        w_data=weather_data(query);
        print_weather(w_data, city)
        print()
    except:
        print('City name not found...')

def area(country):
    '''will show the area of the country in square kilometer'''
    countrya = CountryInfo(country)
    try:
        print(countrya.area())
    except:
        print('country not found')
def full_info(country_name):
    '''will provide full information about the country'''
    con=CountryInfo(country_name)
    try:
        print(con.info())
    except:
        print('country not found')
def capital(country):
    '''will show capital of the required country'''
    ct=CountryInfo(country)
    try:
        print(ct.capital())
    except:
        print('country not found')
def country_code(country):
    '''will show the country code'''
    c=CountryInfo(country)
    try:
        print(c.calling_codes())
    except:
        print('country not found')
