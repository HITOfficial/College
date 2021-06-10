# finding ends of diameter in graph (not only in tree)
from queue import Queue
# matrix adjaciency
# compexity O(V^3) -> runing BFS V times on every vertex


# graph not weighted
def bfs(graph,b):
    n = len(graph)
    time = 0
    times = [float("inf")] * n
    counter = n
    queue = Queue()
    queue.put(b)
    times[b] = time # time 0 to get into start vertex

    while not queue.empty() and counter > 0:
        actual  = queue.get()
        time += 1
        for children in range(n):
            if graph[actual][children] != 0 and times[children] == float("inf"): # children vertex wasn't visited before
                queue.put(children)
                times[children] = time

    index, max_time = b, 0 # finding element with maximum time to get into 
    for i in range(n):
        if max_time < times[i]:
            index, max_time = i, times[i]

    return max_time, b, index # returning max_time and vertexes


def diameter(graph):
    n = len(graph)
    b,e,d = 0,0,0 # begin end distance
    for begin in range(n):
        new_diameter = bfs(graph,begin)
        if new_diameter[0] > d:
            d,b,e = new_diameter
    return b,e,d            


graph = [
    [0,1,0,0,0,1,0],
    [1,0,1,0,0,1,1],
    [0,1,0,1,1,0,1],
    [0,0,1,0,1,0,0],
    [0,0,1,1,0,1,1],
    [1,1,0,0,1,0,1],
    [0,1,1,0,1,1,0]
]

print(diameter(graph))
