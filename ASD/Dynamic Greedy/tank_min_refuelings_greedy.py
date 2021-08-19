# In 2050, Maksymilian travels across the desert from town A to town B. The road between
# cities is a straight line with oil spots in some places. Max
# it is driven by a 24-wheel tanker which burns 1 liter of oil for 1 kilometer of the route. Tanker equipped
# it has a pump to collect oil from spots. To get from city A to city B Maksymilian
# he will have to collect the oil from some stains (not to run out of fuel), which he requires each time
# tanker stop. Unfortunately, the road is dangerous. So Maksymilian has to plan this way
# route to stop as few times as possible. Fortunately, Maksymilian's cistern is huge - after
# Stopped can always collect all the oil from the spot (the tanker would fit all the oil on the route).
# Suggest and implement an algorithm indicating where Maximilian should stop and collect oil on the route. The algorithm should be possible as fast as possible and consume as much as possible
# least memory. Justify its correctness and estimate the computational complexity.


# The data shown in the representation is as a two-dimensional array of numeric values ​​in which it has a value,
# T [u] [v] is full on the field of history (u, v) covered (0 means no oil). Coordinates u 1 of the set {0,. . . , n − 1} and the coordinates of v to the set {0, 1,. . . , m − 1}. The city is located
# on the square (0, 0), and city B on the square (0, m - 1). Maksymilian only moves in the fields
# (0, 0), (0, 1),. . . (0, m-1). The side of each field is 1 kilometer long. Any stain of oil is any
# coherent area of ​​oil fields. The two fields for the dotago com console have a common one
# side or tool sequence of fields (oil management) with common sides. We assume that the stain is the tanker, but the field (0, 0) is the oil stain that can be collected before
# on the road. We also assume that it has a solution, i.e. can go with
# town A to town B.

from queue import PriorityQueue


# complexity:
# - time O(n*m)/(mlogm) ->  to sum up: (n*m + mlogm), n*m taking all fuel from plams, mlogm distances in greedy car refueling
# - space O(m)

# rec alg. to get size of every plan
def rec_plan_size(T, row, col, n, m):
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    plan_size = 0
    # flag to search for new fields
    was_fuel = False
    if T[row][col] > 0:
        # taking of all fuel from actual field
        plan_size += T[row][col]
        was_fuel = True
        T[row][col] = 0
    if was_fuel:
        for r, c in steps:
            new_row, new_col = r+row, c+col
            # width between [0,m-1], height between [0,n-1]
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if T[new_row][new_col] > 0:
                    plan_size += rec_plan_size(T, new_row, new_col, n, m)
    return plan_size


def calculate_refuel_capacity(T, n, m):
    refuel_capacity = [0]*m
    for idx in range(m):
        refuel_capacity[idx] = rec_plan_size(T, 0, idx, n, m)
    return refuel_capacity


def greedy_min_refuelings(T):
    n = len(T)
    m = len(T[0])
    # array, with capacity on every field in row 0
    refueling_capacity = calculate_refuel_capacity(T, n, m)
    min_refuleings_list, min_refuleings = [], float("inf")
    queue = PriorityQueue()
    # need to take all fuel from plan on field 0
    # tuples in queue: (total_distance, fuel_remaining,used stations number, used stations list)
    begining_data = (0, refueling_capacity[0], 1, [0])
    queue.put((begining_data))
    while not queue.empty():
        actual, fuel, refuelings, refuelings_list = queue.get()
        # highest priority has lowest number, so in queue, distances are negative
        actual = actual*(-1)
        if actual+fuel >= m-1:
            if min_refuleings > refuelings:
                min_refuleings = refuelings
                min_refuleings_list = refuelings_list
        else:
            for new_distance in range(actual+1, min(m, actual+fuel+1)):
                fuel_remaining = fuel-(new_distance-actual)
                if refueling_capacity[new_distance] > 0:
                    queue.put((-1*new_distance, fuel_remaining + refueling_capacity[new_distance],
                               refuelings+1, refuelings_list + [new_distance]))
    return min_refuleings_list


T = [
    [3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


print(greedy_min_refuelings(T))
