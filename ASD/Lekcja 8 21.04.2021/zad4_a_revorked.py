

stations = [1,9,15,16,17,27,28]
def min_car_refuelings(stations,distance_to_reach,capacity,fuel=None):
    if fuel == None: # if actual fuel in car was not given, I assume, that car is fueled to maximum capacity
        fuel = capacity
    refuelings = 0
    distance = 0
    last_station = -1
    while distance+fuel < distance_to_reach:
        next_station = last_station + 1
        while next_station < len(stations) and distance+fuel < distance_to_reach:
            if stations[next_station] < distance+fuel:
                fuel = distance+fuel - stations[next_station] 
                next_station += 1
            elif last_station == next_station-1:
                return False # is not possible to reach the destination
            else:
                fuel = capacity
                distance = stations[next_station-1]
                refuelings += 1
                last_station = next_station-1

        if next_station == len(stations):
            if distance+fuel > stations[-1] and distance+fuel < distance_to_reach: # did not refueled on the last station, and can to reach the last point
                distance = stations[-1]
                refuelings += 1
                fuel = capacity
            if distance + fuel < distance_to_reach:
                return False

    return refuelings
    
print(min_car_refuelings(stations, 30, 2))