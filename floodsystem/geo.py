# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
import math



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
