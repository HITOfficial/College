# Dynamic lowest cost of refuelings to get into destination

# complexity:
# - time O(N*D*Q^2), N, number of stations, D- total distance to reach, Q tank capacity
# - space O(N*D*Q)


def get_path(path, S, q, i, q_prev):
    p = []
    if q != 0:
        p.append((q, i))
        d = S[i]
        q, i, q_prev = path[d][q_prev]
        p.extend(get_path(path, S, q, i, q_prev))
    return p


# P-> prices for 1 fuel liter, S-> stations distance from beginning
def car_refueling_min_cost(P, S, D, Q):
    n = len(P)
    A = [[[float("inf")for _ in range(Q+1)] for _ in range(D+1)]
         for _ in range(n)]
    # path tuple: fuel taken, station index, previous fuel
    path = [[(None, None, None)]*(Q+1) for _ in range(D+1)]
    # total distance -> 0
    path[0][0] = 0, 0, 0
    for s in range(n):
        for q in range(Q+1):
            A[s][0][q] = 0

    # need to tank on first station, begining fuel == 0
    for d in range(min(D, Q)+1):
        # to wchich distance and maximal quel remaining can reach on reafueling on begining station
        for q in range(Q+1-d):
            path[d][q] = d, 0, 0
            A[0][d][q] = P[0]*(d+q)

    for i in range(1, n):
        for d in range(D+1):
            for q in range(Q+1):
                A[i][d][q] = A[i-1][d][q]
                # updating data in range
                if S[i] < D and d > S[i] and d+q <= S[i]+Q:
                    for q_prev in range(Q+1):
                        # fuel used
                        fuel_needed = (q-q_prev+d-S[i])
                        cost = A[i-1][S[i]][q_prev] + fuel_needed * P[i]
                        if cost < A[i][d][q]:
                            A[i][d][q] = cost
                            path[d][q] = fuel_needed, i, q_prev
    total_cost, fuel = float("inf"), None
    for q in range(Q+1):
        tmp_cost = A[-1][D][q]
        if tmp_cost < total_cost:
            total_cost, fuel = tmp_cost, q
    # cannot reach destination
    if total_cost == float("inf"):
        return False
    q, i, q_prev = path[D][fuel]
    used_stations = list(reversed(get_path(path, S, q, i, q_prev)))
    fuel_on_station = [0]*n
    for q, i in used_stations:
        fuel_on_station[i] += q
    # returning total cost with stations with fuel taken on them
    return total_cost, fuel_on_station


P = [4, 3, 2, 5, 7, 6]
S = [0, 4, 8, 10, 15, 18]
Q = 5
D = 16

print(car_refueling_min_cost(P, S, D, Q))
