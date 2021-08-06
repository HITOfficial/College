# Exercise in PL lang.
# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , |E|} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o malejących wagach
# (jeśli ścieżki nie ma to zwracamy ∞
from queue import PriorityQueue

# complexity:
# -time O(ElogV)
# -space O(E) -> space to create queue

# list adjacency on undirected weighted graph
graph = [
    [(9, 8), (4, 9), (7, 12)],
    [(9, 7), (2, 4)],
    [(1, 4), (5, 7), (3, 3)],
    [(2, 3), (6, 2), (8, 5)],
    [(0, 9), (5, 11)],
    [(4, 11), (2, 7)],
    [(3, 2)],
    [(0, 12), (8, 6)],
    [(7, 6), (3, 5)],
    [(0, 8), (1, 7)]
]


def monotonic_path(graph, b, e):
    n = len(graph)
    # sorting each edges by weight
    for i in range(n):
        graph[i].sort(key=lambda element:  element[1])
    # marking up, that every vertex can be processed only once
    processed = [False]*n
    total_distance = float("inf")
    p_queue = PriorityQueue()
    # adding best distance to get into begining
    # tuple values: (total_distance, last edge, actual vertex, previous vertex)
    p_queue.put((0, float("inf"), b, b))
    while not p_queue.empty():
        tmp_dist, weight, u, prev = p_queue.get()
        if u == e:
            total_distance = min(total_distance, tmp_dist)
        # all from acutal processing vertex
        if processed[u] is False:
            for v, w in graph[u]:
                if v != prev:
                    # descending edges condition
                    if w < weight:
                        p_queue.put((tmp_dist+w, w, v, u))
             # marking up to visited processed vertex
            processed[u] = True
    # if total distance at the end will be equal inf -> that means cannot get the monotonic descening path to destination
    return total_distance


print(monotonic_path(graph, 0, 6))
