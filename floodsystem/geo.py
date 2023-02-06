# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
import math
import operator


#1b
def stations_by_distance(stations, p):
        pass




#1c
def stations_within_radius(stations, centre, r):
        return_list = []
        for station in stations: #checks each station in the list
                #latitude first
                y_dist = (station.coord[0]-centre[0]) * 110.574 #need to use sf to convert degrees to km

                #longitude multiplier depends on latitude (earth isn't perfect sphere)
                x_dist = (station.coord[1]-centre[1]) * 111.320 * math.cos(math.radians(centre[0]))
                dist = math.sqrt(x_dist**2 + y_dist**2)


                #debugging - ignore
                # if(station.name) == 'Babraham':
                #         print("bab dist", dist)
                #         print("bab xdist", x_dist)
                #         print("bab ydist", y_dist)
                #         print("bab coords", station.coord)
        
                #calculates distance between station and centre using pythagoras
                if dist < r:
                        return_list.append(station)
        return return_list



#1d

def rivers_with_station(stations):
        pass

def stations_by_river(stations):
        pass


#1e
def rivers_by_station_number(stations, N):
        river_dict = stations_by_river(stations)
        #gets dict of rivers and their stations

        for r,s in river_dict:
                river_dict[r] = len(s)
                #replaces list of stations with number of stations
        

        sorted_rivers = sorted(river_dict.items(), key=lambda x:x[1])
        #.items turns dict into list of tuples
        #lambda function means list is sorted by second value in tuple ([1])
        #so this line sorts the dict into a list of tuples (rivername, nu_of_stations) by value

        trunc_rivers = sorted_rivers[:N]
        #leaves only the N rivers with the most stations

        for (river, station_no) in sorted_rivers:
                if station_no == trunc_rivers[-1][1] and (river, station_no) not in trunc_rivers:
                        #if the river has the same no of stations as the last river in trunc_rivers and isnt already in there
                        trunc_rivers.append((river,station_no))
                        #this adds rivers with the same number of stations

        return trunc_rivers

