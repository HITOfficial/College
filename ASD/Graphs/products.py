# Exercise in PL lang.
# Mamy dany graf G = (V, E) z wagami w: E → N−{0}(dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Proszę zaproponować
# algorytm.
from queue import PriorityQueue

# Modyfied Dijkstra alg. -> multiplaying edges/ not summing edge weights

# complexity:
# -time O(ElogV)
# -space O(V)

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


def product(graph, b, e):
    n = len(graph)
    distances = [float("inf")]*n
    distances[b] = 1
    p_queue = PriorityQueue()
    for v, w in graph[b]:
        p_queue.put((w, b, v))
    while not p_queue.empty():
        w, u, v = p_queue.get()
        if distances[v] > distances[u] * w:
            distances[v] = distances[u] * w
            for end, weight in graph[v]:
                if u != v:
                    p_queue.put((weight, v, end))
    return distances[e]


print(product(graph, 0, 2))
