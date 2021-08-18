# Checking if graph is bipartite, using BFS waves

from queue import Queue

# complexity:
# - time O(V^2)
# - space O(V)


def bipartite_graph(graph, s=0):
    n = len(graph)
    # color: 0, unvisited, -1: first color, 1: second color
    colors = [0]*n
    colors[s] = 1
    color = 1
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        next_queue = Queue()
        # changing color every next wave
        if color == 1:
            color = -1
        else:
            color = 1
        while not queue.empty():
            u = queue.get()
            for v in range(n):
                if graph[u][v] == 1:
                    if colors[v] == colors[u]:
                        return False, [], []
                    elif colors[v] == 0:
                        colors[v] = color
                        next_queue.put(v)
        queue = next_queue
    colorA, colorB = [], []
    for i in range(n):
        # graph is not connected
        if colors[i] == 0:
            return False, [], []
        elif colors[i] == 1:
            colorA.append(i)
        else:
            colorB.append(i)
    # returining boolean, idexdes for every color
    return True, colorA, colorB


graph = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]


print(bipartite_graph(graph))
