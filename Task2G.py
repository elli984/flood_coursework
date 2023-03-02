'''
criteria:

risk of flood when water level outside normal range
(relative level > 1)



plan:

list of towns
list of stations per town
average relative water level of each towns stations

compare to threshold values



'''


from floodsystem.geo import stations_by_town
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_threshold
from floodsystem.flood import town_average_level
from floodsystem.flood import town_categories

stations = build_station_list()
towns = stations_by_town(stations)

update_water_levels(stations)

town_levels = town_average_level(towns)

print(town_levels)

low, moderate, high, severe = town_categories(town_levels, 0.8, 1, 1.2, 1.4)
print("\n\nsevere:", severe)
print("\n\nhigh", high)
print("\n\nmoderate", moderate)
print("\n\nlow", low)

