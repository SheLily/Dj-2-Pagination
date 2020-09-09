from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from urllib.parse import urlencode


with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    reader = list(csv.DictReader(csvfile))


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page', 0)) or 1

    data = reader[10 * current_page - 1: 10 * current_page + 10]

    next_params = urlencode({'page': current_page + 1})
    next_page_url = reverse('bus_stations') + '?' + str(next_params) if data[-1] == reader[-1] else None

    prew_params = urlencode({'page': current_page - 1})
    prev_page_url = reverse('bus_stations') + '?' + str(prew_params) if current_page != 1 else None

    return render(request, 'index.html', context={
        'bus_stations': data,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
