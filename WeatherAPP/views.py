from django.shortcuts import render
import urllib.request
import json


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=c2c23b09069b94e0051095e3ca568115').read()
        api_url2 = json.loads(api_url)
        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "feel_temperature": api_url2['main']['feels_like'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity": api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
            "wind_speed":api_url2['wind']['speed'],
            "visibility":api_url2['visibility']
        }
    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "feel_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_icon": None,
            "wind_speed":None,
        }
    print(data['weather_icon'])
    return render(request, 'index.html', {"city": city, "data": data})