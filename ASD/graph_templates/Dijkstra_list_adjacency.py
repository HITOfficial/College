from queue import PriorityQueue

# complexity:
# -time O(ElogV)
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
    for neighbour,d in graph[u]:
        p_queue.put((d,u,neighbour))
    while not p_queue.empty():
        d,b,e = p_queue.get()
        # checking if is posible to relax edge
        if distances[e] > distances[b] + d:
            distances[e] = distances[b] + d
            paths[e] = b
            # inserting neighbours from actual relaxed vertex
            for neighbour,d in graph[e]:
                if neighbour != b:
                    p_queue.put((d,e,neighbour))

    return distances[v], list(reversed(get_path(paths,v)))


graph = [
    [(1,1),(4,2),(5,3),(6,7)],
    [(0,1),(2,7),(4,3)],
    [(1,7),(3,6),(5,12)],
    [(2,6),(4,2)],
    [(0,2),(1,3),(3,2),(6,4)],
    [(0,3),(2,12)],
    [(0,7),(4,4)],
]

print(Dijkstra(graph,0,3))