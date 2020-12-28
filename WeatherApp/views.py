import requests
from django.conf.urls import url
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1f96b42d038719a2ca60c999e426b07a'
    city = request.POST.get('city_name')

    details = requests.get(url.format(city)).json()

    cityWeather = {
        'city':city,
        'temparature' : details['main']['temp'],
        'min_temparature' : details['main']['temp_min'],
        'max_temparature' : details['main']['temp_max'],
        'humidity' : details['main']['humidity'],
        'wind_speed':details['wind']['speed'],
        'icon':details['weather'][0]['icon'],
        'main':details['weather'][0]['main'],
        'desc' : details['weather'][0]['description']

    }

    contest = {'city_weather':cityWeather}
    return render(request, 'index.html',contest)