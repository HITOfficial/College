from queue import PriorityQueue

# min car fueling greedy algorithm

# complexity:
# -time O(NlogN)
# -memory O(N)

def min_car_fueling(array,capacity):
    n = len(array)
    index = 0
    refuelings = 1
    distance = 0
    p_queue = PriorityQueue()
    while distance+capacity < n:
        for index in range(distance+1,min(distance+capacity+1,n)):
            # there is an stop
            if array[index] != 0:
                # priority queue, so lowest numbers has the bigest priority
                p_queue.put(-1*(index))
        if p_queue.empty():
            # cannot get the distance
           return -1 
        d = p_queue.get()
        distance = -1*d
        refuelings += 1
    return refuelings


array1 = [1,0,0,0,1,0,0,1,0,0]
array2 = [1,0,0,0,0,0,0,1,0,0]
array3 = [0,1,1,0,0,0,1,1,0,1,0,1,0]

print(min_car_fueling(array1,4))
print(min_car_fueling(array2,4))
print(min_car_fueling(array3,4))

