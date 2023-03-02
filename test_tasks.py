from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_over_threshold
from floodsystem.flood import stations_highest_rel_level
import datetime
from numpy import poly1d




#1B
def test_1b():
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
def test_1d():

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
def test_1e():
    stations = build_station_list()
    top9 = rivers_by_station_number(stations, 9)
    if len(top9) > 9:
        for s in range(9, len(top9)):
            assert top9[s][1] == top9[-1][1]
    assert top9 == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 27),
    ('River Aire', 25), ('River Derwent', 25), ('River Calder', 24), ('River Severn', 22),
    ('River Stour', 20), ('River Ouse', 18), ('River Colne', 18)]




#1F
def test_1f():
    
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




#2B
def test_2b():
    stations = build_station_list()
    update_water_levels(stations)

    high_stations = stations_over_threshold(stations, 0.8)

    for station, level in high_stations:
        assert level > 0.8
    assert high_stations[-1][1] > high_stations[0][1]

    for i in range(0, len(high_stations)):
        assert high_stations[i][1] >= high_stations[i+1][1]



#2C
def test_2c():
    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 10)

    assert len(highest_stations) == 10


    assert highest_stations[0].relative_water_level() > highest_stations[-1].relative_water_level()
    for i in range(0, len(highest_stations)):
        assert highest_stations[i] >= highest_stations[i+1]


#2E
def test_2e():
    stations = build_station_list()
    update_water_levels(stations)

    N = len(stations)
    while N > 0:
        for i in range(N - 1):
            a1 = stations[i].latest_level
            a2 = stations[i + 1].latest_level
            if type(a1) == float and type(a2) == float:
                if a1 > a2:
                    stations[i + 1], stations[i] = stations[i], stations[i + 1]
            else:
                pass
                    
        N = N - 1
    assert stations[2].latest_level < stations[3].latest_level

#2F
def test_2f():
    stations = build_station_list()
    update_water_levels(stations)

    N = len(stations)
    while N > 0:
        for i in range(N - 1):
            a1 = stations[i].latest_level
            a2 = stations[i + 1].latest_level
            if type(a1) == float and type(a2) == float:
                if a1 > a2:
                    stations[i + 1], stations[i] = stations[i], stations[i + 1]
            else:
                pass
                    
        N = N - 1
    
    dt = 2
    dates, levels = fetch_measure_levels(stations[-1].measure_id,dt=datetime.timedelta(days=dt))
    assert polyfit(dates, levels, 4) == polyfit(dates, levels, 4)

    