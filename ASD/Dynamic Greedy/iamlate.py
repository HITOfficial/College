# Dynamic programing

# car refueling problem: min number of refuelings to get into destination with path of used stations

# complexity:
# -time O(S*D*C^2)
# -memory(S*D*C)
# S- Stations
# D- Distance
# C- Capacity


def get_path(paths,distance,fuel):
    path = [distance]
    next_distance, next_fuel = paths[distance][fuel]
    if next_distance is not None:
        path.extend(get_path(paths,next_distance,next_fuel))
    return path


def iamlate(T,V,q,l):
    n = len(T)
    # 3 dim array: stations x distance x fuel remaining
    array = [[[float("inf")]*(q+1) for _ in range(max(l,T[-1]+q)+1)] for _ in range(n)]

    paths = [[(None,None) for _ in range(q+1)] for _ in range(max(l,T[-1]+q)+1)]

    # reaching distance 0 -> used stations 0
    # stations
    for i in range(n):
        # distance: 0
        # fuel remaining
        for k in range(q+1):
            array[i][0][k] = 0
    # filling using first station combination
    for j in range(1,l+1):
        # filling to full / taking all posible fuel from starting station
        for k in range((min(V[0],q)+1)-j):
            array[0][j][k] = 1

    for station in range(1,n):
        for distance in range(max(l,T[-1]+q)+1):
            for fuel in range(q+1):
                # without using actual station
                array[station][distance][fuel] = array[station-1][distance][fuel]
                # using actual station
                if distance > T[station] and distance <= T[station]+q:
                    # memorizing best option
                    prev_fuel, stop_station = None, float("inf")
                    for i in range(q):
                        # reducing distance, by fueling on actual station
                        if i >= fuel + distance-T[station]-min(q,V[station]) and stop_station > array[station][T[station]][i]:
                            prev_fuel, stop_station = i, T[station]

                    # checking if is less refuelings using refuel on this station
                    if array[station][distance][fuel] > stop_station+1:
                        paths[distance][fuel] = stop_station, prev_fuel
                        array[station][distance][fuel] = stop_station+1
    
    # getting path
    stations_number, dist, fuel_remaining = float("inf"), None, None
    for i in range(q+1):
        if stations_number > array[-1][l][i]:
            stations_number, dist, fuel_remaining = array[-1][l][i], paths[l][i][0], paths[l][i][1]
    if stations_number == float("inf"):
        # can not reach destination
        return []
    else:
        return [T[0]] + list(reversed(get_path(paths,dist,fuel_remaining)))
    

T1 = [0,5,10]
V1 = [10,5,20]
q1 = 100
l1 = 35

T2 = list(range(100))
V2= [1 for _ in range(100)]
q2 = 1
l2 = 100

print(iamlate(T1,V1,q1,l1))
print(len(iamlate(T2,V2,q2,l2)))