# Problem: Minimum edges to reverse to make path from a source to a destination in directed graph
from queue import Queue

# complexity:
# -time O(V^2)
# -space O(V^2)


graph = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
]

# marking up to weight 2 reversed of edge


def reverse_edges(graph, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # reversing edge
                graph[j][i] = 2


def edges_to_reverse(graph, b, e):
    n = len(graph)
    reverse_edges(graph, n)
    time = 0
    times = [False]*n
    times[e] = 0
    queue = Queue()
    queue.put((e, e))
    while not queue.empty():
        new_queue = Queue()
        while not queue.empty():
            actual, previus = queue.get()
            for neighbour in range(n):
                if times[neighbour] is False and graph[actual][neighbour] != 0:
                    if graph[actual][neighbour] == 1:
                        # without primary edge
                        times[neighbour] = times[actual]
                    else:
                        # using reversed edge
                        times[neighbour] = times[previus] + 1
                    new_queue.put((neighbour, actual))
        queue = new_queue
    return times[b]


print(edges_to_reverse(graph, 0, 6))
