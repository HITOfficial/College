# minimum petrol station visits


# I assume that, car start with full capacity
def car_refuelings(L,S,T): # capacity, stations, distance
    max_capacity = fuel = L # starting with full capacity
    distance_to_reach = T
    distance = 0 # actual distance
    refuelings = 0
    stations = S
    last_station = -1

    while distance < distance_to_reach:
        next_station = last_station + 1
        while len(stations) > next_station and distance_to_reach > distance:
            if stations[next_station] <= fuel: # is able to skip this station
                fuel -= stations[next_station]
                distance += stations[next_station]
                next_station += 1
            elif next_station == last_station+1 and fuel< stations[next_station]:
                return False # car is not able reach next station
            else: # car need to refuel in actual petrol station
                fuel = max_capacity
                refuelings += 1
                last_station = next_station-1
                distance += stations[last_station]
        if next_station == len(stations) and distance < distance_to_reach:
            return False # no more stations
    return refuelings


L = 21
S = [5,19,17,12,6,3]
T = 51

print(car_refuelings(L,S,T))

        
    
