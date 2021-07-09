# Exercise in PL. lang. kintersect.png
from  queue import PriorityQueue

# running N times PriorityQueue on every element and taking greedy K best distances

# complexity:
# -time O(N^2logN)
# -space O(K)


def kintersect( A, k ):
    n = len(A)
    best_array = []
    highest_difference = 0
    for begining in range(n):
        l, r = A[begining]
        p_queue = PriorityQueue()
        counter = 1
        array = [begining]
        difference = 0
        for index,element in enumerate(A):            
            left, right = element
            if left <= l and index != begining:
                # every element ending has highter value than begining, so to priority queue I'll add negative values of endings, and indexes to memorize
                # and also negative values, becous highest priority has the lowest value
                p_queue.put((-right,index))

        while not p_queue.empty() and counter < k:
            _, index = p_queue.get()
            counter += 1
            array.append(index)

        if k == counter:
            # difference
            difference =  min(A[array[-1]][1]-l,r-l)

        if difference > highest_difference:
            highest_difference = difference
            best_array = array.copy()
            
    return best_array


A = [(0,4),(1,10),(6,7), (2,8)]
print(kintersect(A,3))