# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
import math
import operator
from haversine import haversine, Unit


#1b
def stations_by_distance(stations, p):

        xf = []
        for station in stations:
                #Build a list of stations with its name, town name and distance from Cambridge city centre
                coordinate = station.coord
                x = (station.name, station.town, haversine(coordinate,p))
                xf.append(x)

        def distance_sort(A):

                # Perform sorting    
                N = len(A)
                while N > 0:
                        for i in range(N - 1):
                        # Swap data if in wrong order
                                if A[i][2] > A[i + 1][2]:
                                        A[i + 1], A[i] = A[i], A[i + 1]
                    
                        N = N - 1
        
                return A
    
        distance_sort(xf)
        return xf




#1c
def stations_within_radius(stations, centre, r):

        return_list = []


        for station in stations: #checks each station in the list

                dist = haversine(station.coord,centre)
                if dist<r:
                        return_list.append(station)


        #         #latitude first
        #         y_dist = (station.coord[0]-centre[0]) * 110.574 #need to use sf to convert degrees to km

        #         #longitude multiplier depends on latitude (earth isn't perfect sphere)
        #         x_dist = (station.coord[1]-centre[1]) * 111.320 * math.cos(math.radians(centre[0]))
        #         dist = math.sqrt(x_dist**2 + y_dist**2)


        #         #debugging - ignore
        #         # if(station.name) == 'Babraham':
        #         #         print("bab dist", dist)
        #         #         print("bab xdist", x_dist)
        #         #         print("bab ydist", y_dist)
        #         #         print("bab coords", station.coord)
        
        #         #calculates distance between station and centre using pythagoras
        #         if dist < r:
        #                 return_list.append(station)




        return return_list



#1d
def rivers_with_station(stations):
    stations_freq = {}
    for station in stations:
        rivers = [station.river]
        
        for river in rivers:
            if river in stations_freq:
                stations_freq[river] += 1
            else:
                stations_freq[river] = 1
    
    rivers_1station = []
    
    for item,value in stations_freq.items():
        if value >= 1:
            rivers_1station.append(item)
    
    rivers_1station.sort()
    return rivers_1station


def stations_by_river(stations):
    river_stations = {}
    for item in stations:
        if item.river in river_stations:
            river_stations[item.river].append(item.name)
        else:
            river_stations[item.river] = [item.name]

            
    return river_stations



#1e
def rivers_by_station_number(stations, N):
        river_dict = stations_by_river(stations)
        #gets dict of rivers and their stations

        for r in river_dict:
                river_dict[r] = len(river_dict[r])
                #replaces list of stations with number of stations
        

        sorted_rivers = sorted(river_dict.items(), key=lambda x:x[1], reverse=True)
        #.items turns dict into list of tuples
        #lambda function means list is sorted by second value in tuple ([1])
        #so this line sorts the dict into a list of tuples (rivername, nu_of_stations) by value
        #reverse=true means the rivers with the most stations are first in the list

        trunc_rivers = sorted_rivers[:N]
        #leaves only the N rivers with the most stations

        for (river, station_no) in sorted_rivers:
                if station_no == trunc_rivers[-1][1] and (river, station_no) not in trunc_rivers:
                        #if the river has the same no of stations as the last river in trunc_rivers and isnt already in there
                        trunc_rivers.append((river,station_no))
                        #this adds rivers with the same number of stations

        return trunc_rivers

