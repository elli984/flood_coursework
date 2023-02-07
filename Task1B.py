from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

# Build list of stations
stations = build_station_list()
p = (52.2053, 0.1218) #coordinates of Cambridge city centre

def stations_by_distance(stations, p):

    xf = []
    for station in stations:
        #Build a list of stations with its name, twon name and distance from Cambridge city centre
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
    print(xf[:10]) #Closest 10 stations
    print(xf[-10:]) #Furthest 10 stations
    
stations_by_distance(stations,p)