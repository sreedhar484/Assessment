from django.shortcuts import render, redirect
import json
from math import radians, cos, sin, asin, sqrt
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
import os


def home(request):
    return render(request, 'welcome.html')


def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


def location(request):
    try:
        lat = float(request.POST['lat'])
        lon = float(request.POST['lon'])
    except:
        return redirect("home")
    url = os.path.join(settings.STATIC_ROOT, 'cars.json')
    file = open(url)
    arr = json.load(file)
    k = []
    for i in arr:
        k.append(
            [i, dist(lat, lon, float(i["location"][0]), float(i["location"][1]))])
    k = list(sorted(k, key=lambda x: x[1]))
    m = []
    for i in k[:5]:
        m.append([i[0]["Name"], i[0]["location"][0], i[0]
                  ["location"][1], i[1]])
    return render(request, 'home.html', {'data': m})
