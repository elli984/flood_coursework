#1B
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

# Build list of stations
stations = build_station_list()
p = (52.2053, 0.1218) #coordinates of Cambridge city centre

x = stations_by_distance(stations,p)

lst = []
for item in x:
    lst.append(item[2]) 
assert sorted(lst) == lst


#1C
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
#import operator

stations = build_station_list() #get list of all stations


close_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)

#close_stations.sort(key=operator.attrgetter('name'))

station_names = []
for station in close_stations:
        station_names.append(station.name)

station_names.sort()

print(station_names)



#1D
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

# Build list of stations
stations = build_station_list()

d = rivers_with_station(stations)

assert d == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop', 'Arkle Beck']

    


y = stations_by_river(stations)
yRA = sorted(y['River Aire'])
yRC = sorted(y['River Cam'])
yRT = sorted(y['River Thames'])

assert yRA[0] == 'Airmyn'
assert yRC[0] == 'Cam'
assert yRT[0] == 'Abingdon Lock'

#1E

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()
print(rivers_by_station_number(stations, 9))


#1F
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

# Build list of stations
stations = build_station_list()

a = inconsistent_typical_range_stations(stations)
lst = []
for item in a:
    for item2 in stations:
        if item2.name == item:
            lst.append(item2.typical_range_consistent())
        else:
            pass

counter = 0
for aa in lst:
    if aa == False:
        counter += 1
    else:
        pass
assert counter == len(a)
    