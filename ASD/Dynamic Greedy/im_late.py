# reduced complexity of "imlate.py" problem

# complexity:
# - time O(N*Q^2) , where N is number of stations, Q is tank capacity
# - space O(L*Q) , where L in distance to reach


def get_path(path, dist, fuel):
    p = []
    station_idx, dist, fuel = path[dist][fuel]
    if station_idx is not None:
        p.append(station_idx)
        p.extend(get_path(path, dist, fuel))
    return p


# distance from beggining to station, fuel in station, capacity, distance to reach
def im_late(T, V, q, l):
    # 2 dim array: l x q
    stops = [[float("inf")]*(q+1) for _ in range(l+1)]
    # tuple in path: (index, prev distance, fuel on prev)
    path = [[(None, None, None)]*(q+1) for _ in range(l+1)]
    # actual station
    s = 0
    stations_len = len(T)
    stops[0][0] = 0
    for idx in range(stations_len):
        dist = T[idx]
        # next station stops are out of range distance to reach
        if dist > l:
            break
        # fuel remaining in actual distance
        for fuel in range(q+1):
            fuel_after_tanking = min(fuel+V[idx], q)
            distance_to_reach = fuel_after_tanking + dist
            for new_dist in range(dist, min(distance_to_reach, l)+1):
                fuel_remaining = fuel_after_tanking - (new_dist-dist)
                if stops[new_dist][fuel_remaining] > stops[dist][fuel]+1:
                    stops[new_dist][fuel_remaining] = stops[dist][fuel]+1
                    path[new_dist][fuel_remaining] = idx, dist, fuel
    min_stops, fuel = float("inf"), None
    # finding best option
    for f in range(q+1):
        if stops[-1][f] < min_stops:
            min_stops = stops[-1][f]
            fuel = f
    # wasn't enought fuel on road, to reach distance
    if min_stops == float("inf"):
        return False
    else:
        return list(reversed(get_path(path, l, fuel)))


T1 = [0, 5, 10]
V1 = [10, 5, 20]
q1 = 100
l1 = 35

T2 = list(range(100))
V2 = [1 for _ in range(100)]
q2 = 1
l2 = 100

print(im_late(T1, V1, q1, l1))
print(len(im_late(T2, V2, q2, l2)))
