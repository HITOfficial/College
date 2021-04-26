# Car fueling - Dynamicaly O(n*distance)
# refuelings only to full tank capacity



# to algorithm works fine: need to first station distance be lower or equal to starting fuel
def refuelings_min_cost(stations ,prices ,distance_to_reach ,capacity ,fuel=None):
    if fuel is None: # assuming with not adding starting fuel, will be equal to maximum capacity
        fuel = capacity
    n = len(stations)
    lowest_costs  = [[[float("inf"),0] for _ in range(distance_to_reach+1)] for _ in range(len(stations))] # minimum_cost remaining fuel

    for i in range(fuel+1):
        lowest_costs[0][i][0] = 0 # tuples (min_cost,fuel_remaining)
        lowest_costs[0][i][1] = fuel-i # fuel remaing
    for i in range(n):
        lowest_costs[i][0][0] = 0
    for i in range(stations[0]+2,min(stations[0]+capacity+1,distance_to_reach)): # using only first station the best combination
        if lowest_costs[0][i][0] != 0: # beggining fuel has ended
            lowest_costs[0][i][0] = prices[0] * (capacity -(fuel-stations[0])) # filling
            lowest_costs[0][i][1] = capacity - (i-stations[0]) # fueal remaing in actaul distance


    for i in range(1,n):
        for distance in range(1,distance_to_reach+1):
            lowest_costs[i][distance] = lowest_costs[i-1][distance][:] # copy combination to staion
            if distance > stations[i] and distance <= stations[i]+capacity:
                tmp_cost = prices[i] * (capacity -(lowest_costs[i][stations[i]][1])) # filling to full in actual station
                tmp_fuel = capacity - (distance-stations[i]) # distance from last station
                if tmp_cost < lowest_costs[i][distance][0]:
                    lowest_costs[i][distance] = [tmp_cost, tmp_fuel]


    for el in lowest_costs[-1]:
        if el[0] == float("inf"):
            return False
    return f"Cost: {lowest_costs[-1][-1][0]} Fuel remaining: {lowest_costs[-1][-1][1]}"


stations = [2,9,15,16,17,27,28]
prices = [1,100,10,15,1,30,30]
distance = 31
capacity = 11

print(refuelings_min_cost(stations, prices, distance, capacity))