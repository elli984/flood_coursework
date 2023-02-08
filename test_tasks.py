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




#1D
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

# Build list of stations
stations = build_station_list()

d = rivers_with_station(stations)

assert d[0] == 'Addlestone Bourne'

    


y = stations_by_river(stations)
yRA = sorted(y['River Aire'])
yRC = sorted(y['River Cam'])
yRT = sorted(y['River Thames'])

assert yRA[0] == 'Airmyn'
assert yRC[0] == 'Cam'
assert yRT[0] == 'Abingdon Lock'

#1E




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

if 'True' in lst:
    print('Error')
else:
    print('No problem with 1f')