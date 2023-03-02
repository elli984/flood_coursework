from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_threshold

stations = build_station_list()
update_water_levels(stations)

high_stations = stations_over_threshold(stations, 0.8)

for station, level in high_stations:
    print(station.name, level)