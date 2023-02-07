from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

# Build list of stations
stations = build_station_list()
p = (52.2053, 0.1218) #coordinates of Cambridge city centre

x = stations_by_distance(stations,p)
print(x[:10])
print(x[-10:])