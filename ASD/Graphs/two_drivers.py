# Exercise in PL lang.
# (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki
# to miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
# zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi
# pierwszy. Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede
# wszystkim poprawny).
from queue import PriorityQueue

# mix of Dijkstra and BFS
# memorizing only Alice distance to minimalize, while will be Bob's turn weight of edge is 0

# complexity:
# -time O(ElogV)
# -space O(V)


# list adjacency, positive edge weights
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

# checking if is posible to reduce distance between vertices


def get_path(paths, actual):
    path = [actual]
    if paths[actual] is not None:
        path.extend(get_path(paths, paths[actual]))
    return path


def realx(distances, parents, u, v, w):
    if distances[v] > distances[u] + w:
        distances[v] = distances[u] + w
        parents[v] = u
        return True
    else:
        return False


# running twice this alg.
def two_drivers(graph, b, e, flag):
    n = len(graph)
    distances = [float("inf")]*n
    distances[b] = 0
    parents = [None]*n
    p_queue = PriorityQueue()
    for v, w in graph[b]:
        # Alice starting
        if flag is True:
            p_queue.put((w, b, v))
        else:
            p_queue.put((w, b, v))

    while not p_queue.empty():
        w, u, v = p_queue.get()
        if realx(distances, parents, u, v, w):
            for end, weight in graph[v]:
                if u != v:
                    # Bob's turn
                    if w != 0:
                        p_queue.put((0, v, end))
                    else:
                        p_queue.put((weight, v, end))
    return distances, parents


def alice_bob(graph, b, e):
    # alice starting
    alice_dist, alice_path = two_drivers(graph, b, e, True)
    # bob starting
    bob_dist, bob_path = two_drivers(graph, b, e, False)
    # returning who should start, total distance, path
    if alice_dist < bob_dist:
        path = list(reversed(get_path(alice_path, e)))
        return "Alice starting", bob_dist[e], path
    else:
        path = list(reversed(get_path(bob_path, e)))
        return "Bob starting", bob_dist[e], path


print(alice_bob(graph, 0, 3))
