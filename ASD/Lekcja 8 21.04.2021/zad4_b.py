stations = [2,9,15,16,17,27,28]
prices = [1,100,10,15,1,30,30]


# to algorithm works fine: need to first station distance be lower or equal to starting fuel
def refuelings_min_cost(stations ,prices ,distance_to_reach ,capacity ,fuel=None):
    if fuel is None: # assuming with not adding starting fuel, will be equal to maximum capacity
        fuel = capacity
    n = len(stations)
    lowest_costs  = [[float("inf")]*(distance_to_reach+1) for _ in range(len(stations))]
    for i in range(fuel+1):
        lowest_costs[0][i] = 0
    for i in range(n):
        lowest_costs[i][0] = 0
    for i in range(stations[0]+2,min(stations[0]+capacity+1,distance_to_reach)): # using only first station the best combination
        if lowest_costs[0][i] != 0: # beggining fuel has ended
            lowest_costs[0][i] = lowest_costs[0][i-1]+prices[0]

    for i in range(1,n):
        for distance in range(1,distance_to_reach+1):
            lowest_costs[i][distance] = lowest_costs[i-1][distance] # without including actual station
            if distance > stations[i] and distance <= stations[i]+capacity:
                lowest_costs[i][distance] = min(lowest_costs[i][distance], lowest_costs[i][distance-1]+prices[i])

    for el in lowest_costs[-1]:
        if el == float("inf"):
            return False
    return lowest_costs[-1][-1]

    
print(refuelings_min_cost(stations,prices, 30, 14,3))