# Graph representation: undirected weighted graph on list adjacency
from queue import PriorityQueue


# complexity:
# - time O(E*(ElogV))
# - space O(V)


def get_path(paths, actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths, paths[actual]))
    return path


# Dijkstra alg. from templates
def Dijkstra(graph, u, v):
    n = len(graph)
    distances = [float("inf")]*n
    distances[u] = 0
    paths = [None]*n
    p_queue = PriorityQueue()
    # inserting into Priority Queue all neighbours of starting vertex
    for neighbour, d in graph[u]:
        p_queue.put((d, u, neighbour))
    while not p_queue.empty():
        d, b, e = p_queue.get()
        # checking if is posible to relax edge
        if distances[e] > distances[b] + d:
            distances[e] = distances[b] + d
            paths[e] = b
            # inserting neighbours from actual relaxed vertex
            for neighbour, d in graph[e]:
                if neighbour != b:
                    p_queue.put((d, e, neighbour))

    return distances[v], paths


def min_cycle(graph):
    n = len(graph)
    min_cycle_weight, min_cycle_path, a, b = float("inf"), [], 0, 0
    for u in range(n-1):
        for v in range(u+1, n):
            # checking if has connection
            w = None
            # checking if those vertices are connected
            for k, l in graph[v]:
                if k == u:
                    w = l
            if w is not None:
                u_adjacency, v_adjacency = graph[u].copy(), graph[v].copy()
                graph[u].remove((v, w))
                graph[v].remove((u, w))
                dist, path = Dijkstra(graph, u, v)
                # adding again connections betweeen
                graph[u] = u_adjacency
                graph[v] = v_adjacency
                # adding weight of removed edge
                dist += w
                if dist < min_cycle_weight:
                    min_cycle_weight, min_cycle_path, a, b = dist, path, u, v
    # condition if is cycle in graph
    if min_cycle_weight == float("inf"):
        return
    else:
        return min_cycle_weight, list(reversed(get_path(min_cycle_path, b))) + [a]


graph = [
    [(1, 5), (2, 7)],
    [(0, 5), (2, 23), (3, 3)],
    [(0, 7), (1, 23), (3, 6)],
    [(1, 3), (2, 6)],
]

print(min_cycle(graph))
