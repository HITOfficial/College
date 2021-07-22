# Exercise in PL lang.
# (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , |E|} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o malejących wagach
# (jeśli ścieżki nie ma to zwracamy ∞
from queue import PriorityQueue

# complexity:
# -time O(ElogV)
# -space O(V) -> creating two O(V) arrays: total min distance to each vertex, last edge weight icomming to

# list adjacency
graph = [
    [(9, 8), (4, 9), (7, 12)],
    [(9, 7), (2, 22)],
    [(1, 22), (5, 7), (3, 4)],
    [(2, 4), (6, 3), (8, 5)],
    [(0, 9), (5, 11)],
    [(4, 11), (2, 7), (6, 5)],
    [(5, 5), (3, 3)],
    [(0, 12), (8, 15)],
    [(7, 15), (3, 5)],
    [(0, 8), (1, 7)]
]


def descending_edges(graph, b, e):
    n = len(graph)
    distances = [float("inf")]*n
    last_edge_weight = [float("inf")]*n
    distances[b] = 0
    p_queue = PriorityQueue()
    for v, w in graph[b]:
        # tuple values (edge weight, ending of edge)
        p_queue.put((w, b, v))

    while not p_queue.empty():
        w, u, v = p_queue.get()
        if distances[v] > distances[u] + w and last_edge_weight[u] > w:
            distances[v] = distances[u] + w
            last_edge_weight[v] = w
            for neighbour, weight in graph[v]:
                if neighbour != u:
                    p_queue.put((weight, v, neighbour))

    return distances[e]


print(descending_edges(graph, 0, 1))
