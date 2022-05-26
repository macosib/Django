from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT_BUS = []

def _get_content():
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile, delimiter=","))
        CONTENT_BUS.extend(reader)

def bus_stations(request):
    page_number = request.GET.get('page', 1)
    if not CONTENT_BUS:
        _get_content()
    paginator = Paginator(CONTENT_BUS, 10)
    page = paginator.get_page(page_number)
    context = {
            'bus_stations': page.object_list,
            'page': page,
    }
    return render(request, 'stations/index.html', context)
