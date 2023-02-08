from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number





#1B
# Build list of stations
stations = build_station_list()
p = (52.2053, 0.1218) #coordinates of Cambridge city centre

x = stations_by_distance(stations,p)

lst = []
for item in x:
    lst.append(item[2]) 
    assert sorted(lst) == lst


#1C

def test_1c():

    stations = build_station_list() #get list of all stations


    close_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)

    #close_stations.sort(key=operator.attrgetter('name'))

    station_names = []
    for station in close_stations:
            station_names.append(station.name)

    

    station_names.sort()

    assert station_names == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
    'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill',
    'Lode', 'Oakington', 'Stapleford']





#1D
from floodsystem.stationdata import build_station_list


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
def test_1f():
    stations = build_station_list()
    top9 = rivers_by_station_number(stations, 9)
    assert top9 == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 27),
    ('River Aire', 25), ('River Derwent', 25), ('River Calder', 24), ('River Severn', 22),
    ('River Stour', 20), ('River Ouse', 18), ('River Colne', 18)] 



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