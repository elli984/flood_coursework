#Eliana Stockdale
#06/02/2023


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

# debugging = []
# for station in stations:
#         if station.name == 'Comberton':
#                 print(station.coord)
#                 debugging.append(station)



# for station in close_stations:
#         print(station)

# print(len(close_stations))
