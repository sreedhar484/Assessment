import json
from math import radians, cos, sin, asin, sqrt

def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    dlon = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371* c
    return km

lat=float(input())
lon=float(input())
file=open("C:/Users/sree/Downloads/cars.json")
arr=json.load(file)
k=[]
for i in arr:
    k.append([i,dist(lat,lon,float(i["location"][0]),float(i["location"][1]))])
k=list(sorted(k,key=lambda x:x[1]))
print(k[:5])
