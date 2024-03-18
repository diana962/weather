import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CityForm
from weather.models import City


def index(request):
    appid = '9f194586bf91fabfbccedc86111956c6'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={appid}'
        res = requests.get(url).json()

        try:
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
            }
            all_cities.append(city_info)
        except KeyError:
            pass

    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, 'index.html', context)


def delete_city(request, city_name):
    if request.method == 'POST':
        City.objects.filter(name=city_name).delete()
    return HttpResponseRedirect(reverse('index'))