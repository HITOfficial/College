# graph representation: directed on matrix adjacency
# inspiration to algorithm: https://www.youtube.com/watch?v=wUgWX0nc4NY
# I replaced stack on a deque, and also created an class to memorize vertices from every SCC and number of them

from collections import deque

# complexity:
# - time O(V^2) -> modyfied DFS alg. on matrix adjacency
# - space O(V)


class Time():
    def __init__(self, time=0):
        self.time = time


class SCC():
    def __init__(self, counter=0):
        self.counter = counter
        self.array = []

    def createNewList(self):
        self.array.append(list())

    def addVertex(self, vertex):
        self.array[-1].append(vertex)


graph = [
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0],
]


def deque_DFS(graph, n, times, low, on_deque, deq, time, scc, u):
    deq.append(u)
    time.time += 1
    on_deque[u] = True
    times[u] = low[u] = time.time
    for v in range(n):
        # checking if has edge connection
        if graph[u][v] == 1:
            # checking if vertex wasn't visited before
            if times[v] == float('inf'):
                deque_DFS(graph, n, times, low, on_deque, deq, time, scc, v)
            if on_deque[v] is True:
                low[u] = min(low[u], low[v])
    # taking off all elements from stack
    if times[u] == low[u]:
        # adding new array to cath all elements from actual SCC
        scc.createNewList()
        # taking of all elements from deque, being a part of actual SCC
        while deq:
            vertex = deq.pop()
            scc.addVertex(vertex)
            on_deque[vertex] = False
            low[vertex] = low[u]
            if vertex == u:
                break
        # found new strongly connected component
        scc.counter += 1


def Tarjans_strongly_connected_components(graph):
    n = len(graph)
    times = [float("inf")]*n
    low = [float("inf")]*n
    on_deque = [False]*n
    deq = deque()
    # counter for founded strongly connected components
    scc = SCC()
    time = Time()
    # running stack_DFS alg. on every vertex
    for vertex in range(n):
        # currently vertex wasn't visited before
        if times[vertex] == float("inf"):
            deque_DFS(graph, n, times, low, on_deque, deq, time, scc, vertex)
    return scc.counter, scc.array


print(Tarjans_strongly_connected_components(graph))
