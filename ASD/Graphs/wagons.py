# Exercise in Pl lang. wagons.png

# I rejected condition about ID's
# Graph is has a tree structure, so running twice BFS, will calculate diameter of s

from queue import Queue
# finding longest diameter in graph

# complexity:
# -time O(V+E)
# -space o(V)


def BFS_visited(graph,visited,times,n,b,flag=False):
    queue = Queue()
    queue.put(b)
    time = 1
    times[b] = time
    while not queue.empty():
        time += 1
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for neighbour in graph[actual]:
                if times[neighbour] == float("inf"):
                    visited[neighbour] = True
                    times[neighbour] = time
                    next_queue.put(neighbour)
        queue = next_queue
    # returning executing times
    return diameter_length(times,visited,graph,b,n,flag)


def diameter_length(times,visited,graph,b,n,flag):
    index, time = b, 0
    for i,t in enumerate(times):
        if t > time and t != float("inf"):
            index, time = i, t
    if flag == False:
        times = [float("inf")]*n
        # reseting executing time, and running again BFS algorithm
        return BFS_visited(graph,visited,times,n,index,True)
    else:
        return time,times
    # running again BFS from 
        

def wagons_diameter(connections):
    n = len(connections)
    visited = [False]*n
    longest_diameter = 0
    # starting BFS, overy connected components    
    for i in range(n):
        if visited[i] is False:
            times = [float("inf")]*n
            diameter, times = BFS_visited(connections,visited,times,n,i)
            if diameter > longest_diameter:
                longest_diameter = diameter
    return longest_diameter



graph = [
    [1,3,4],
    [0,2],
    [1],
    [0],
    [0,5],
    [4,6],
    [5],
    [8],
    [7,9,10,11],
    [8],
    [8],
    [8,12],
    [11,13],
    [12,14],
    [13,15],
    [14]
]

print(wagons_diameter(graph))