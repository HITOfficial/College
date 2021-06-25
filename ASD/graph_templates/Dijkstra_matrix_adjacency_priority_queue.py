from queue import PriorityQueue

# complexity:
# -time O(V^2logV)
# -memory O(V)


def get_path(paths,actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def Dijkstra(graph,u,v):
    n = len(graph)
    distances = [float("inf")]*n
    distances[u] = 0
    paths  = [None]*n
    p_queue  = PriorityQueue()
    # inserting into Priority Queue all neighbours of starting vertex
    for neighbour in range(n):
        if graph[u][neighbour] != 0:
            p_queue.put((graph[u][neighbour],u,neighbour))
    while not p_queue.empty():
        d,b,e = p_queue.get()
        # checking if is posible to relax edge
        if distances[e] > distances[b] + d:
            distances[e] = distances[b] + d
            paths[e] = b
            # inserting neighbours from actual relaxed vertex
            for neighbour in range(n):
                if graph[e][neighbour] != 0 and neighbour != b:
                    p_queue.put((graph[e][neighbour],e,neighbour))

    return distances[v], list(reversed(get_path(paths,v)))


graph = [
    [0,1,0,0,2,3,7],
    [1,0,7,0,3,0,0],
    [0,7,0,6,0,12,0],
    [0,0,6,0,2,0,0],
    [2,3,0,2,0,0,4],
    [3,0,12,0,0,0,0],
    [7,0,0,0,4,0,0]
]

print(Dijkstra(graph,0,3))