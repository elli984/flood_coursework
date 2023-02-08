from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    # Build list of stations
    stations = build_station_list()

    x = rivers_with_station(stations)

    print(len(x), 'stations. First 10 - ', x[:10])  

    


    y = stations_by_river(stations)
    yRA = y['River Aire']
    yRC = y['River Cam']
    yRT = y['River Thames']

    print('\n',sorted(yRA))
    print('\n',sorted(yRC))
    print('\n',sorted(yRT))


if __name__ == "__main__":
    run()

            