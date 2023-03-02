def stations_over_threshold(stations, tol):
    return_list = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level != None: #checking data is valid
            if relative_level > tol:
                return_list.append((station, station.relative_water_level()))
                #adds stations if the level is high enough

        return_list.sort(key = lambda i:i[1], reverse = True)
        #lambda function sorts by second value in tuple: relative water level
        #reverse = true means the highest values are listed first
    return return_list


def stations_highest_rel_level(stations, N):
    stations_with_data = []
    for station in stations:
        if station.relative_water_level() != None:
            stations_with_data.append(station)
            #this all makes sure the computer does not try to process stations with no data

    stations_with_data.sort(key= lambda i:i.relative_water_level(), reverse = True)
    #lambda function here means the list is sorted by relative water level

    return stations_with_data[0:N]


def town_average_level(towns):
    output = {}
    for town in towns:
        #adding the relative levels of each station
        total_level = 0
        n = len(towns[town]) #number of valid stations per town
        for station in towns[town]:
            if station.relative_water_level() != None:
                total_level += station.relative_water_level()
            else:
                n -= 1 #n decreases if staion has no valid data
        if n > 0:
            total_level /= n #divides by number of stations in the town
            output[town] = total_level
    return output


def town_categories(town_levels, thresh1, thresh2, thresh3, thresh4): #thresholds ordered smallest to greatest
    output = [[],[],[],[]]
    output = [{},{},{},{}]
    for town in town_levels:
    #     level = town_levels[town]
    #     if level > thresh4: #if higher than biggest threshold (severe)
    #         output[3].append(town) #added to final list
    #     elif level > thresh3: #or if bigger than third (high)
    #         output[2].append(town)
    #     elif level > thresh2: #or if bigger than second (moderate)
    #         output[1].append(town)
    #     elif level > thresh1: #or if only bigger than first (low)
    #         output[0].append(town)

        level = town_levels[town]
        if level > thresh4: #if higher than biggest threshold (severe)
            output[3][town] = level #added to final list
        elif level > thresh3: #or if bigger than third (high)
            output[2][town] = level
        elif level > thresh2: #or if bigger than second (moderate)
            output[1][town] = level
        elif level > thresh1: #or if only bigger than first (low)
            output[0][town] = level
    return output

