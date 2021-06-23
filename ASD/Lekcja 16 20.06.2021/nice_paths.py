# Exercise in PL lang.
# Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo ścieżką między v i u,
# ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych ścieżek w sensie liczby krawędzi wśród najkrótszych ścieżek w sensie wagowym).
# Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne ścieżki do pozostałych wierzchołków.
from queue import PriorityQueue

# Dijkstra alg. with small modyfication- on relax function 2 options. lowest distance to new edge, or equeal distance, and less edges

# compelxity:
# -time O(ElogV)
# -memory O(V)


# recreating nice path
def get_path(paths,actual):
    array = []
    if paths[actual] is not None:
        array.append(paths[actual])
        array.extend(get_path(paths,paths[actual]))
    return array


def nice_path(graph,u,v):
    n = len(graph)
    distances = [(float("inf"),float("inf")) for _ in range(n)]
    paths  =[None] * n
    p_queue = PriorityQueue()
    distances[u] = (0,0)
    # inserting all neigbour vertices of starting vertex to Priority Queue
    for e,d in graph[u]:
        p_queue.put((d,u,e))
    # Dijkstra alg. on list adjacency
    while not p_queue.empty():
        d,b,e = p_queue.get()
        # relaxing edge: lowest distance / equal distance less edges
        if distances[e][0] > distances[b][0]+d or (distances[e][0] == distances[b][0]+d and distances[e][1] > distances[b][1]+1):
            distances[e] = distances[b][0] + d, distances[b][1] + 1
            paths[e] = b
            # insterting all neigbours of relaxed edge
            for neighbour,w in graph[e]:
                if b != neighbour:
                    p_queue.put((w,e,neighbour))

    path = list(reversed(get_path(paths,v))) + [v]
    # returining minumum distance, number of used edges, path
    return *distances[v], path


graph = [
    [(1,10),(4,2)],
    [(0,10),(3,6)],
    [(3,9),(4,5)],
    [(1,6),(2,9),(4,21)],
    [(0,2),(2,5),(3,21)],
]

print(nice_path(graph,0,3))