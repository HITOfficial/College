# Exercise in PL lang.
# Dany jest graf ważony z dodatnimi wagami G. Dana jest też lista E’ krawędzi, które nie należą do grafu, ale są krawędziami między wierzchołkami z G. Dane są również dwa wierzchołki s i t.
# Podaj algorytm, który stwierdzi, którą jedną krawędź z E’ należy wszczepić do G, aby jak najbardziej zmniejszyć dystans między s i t.
# Jeżeli żadna krawędź nie poprawi dystansu między s i t, to algorytm powinien to stwierdzić.

from queue import PriorityQueue

# complexity:
# -time O(ElogV)
# -memory O(V)


def Dijkstra_distances(graph,begin):
    n = len(graph)
    distances = [float("inf")] * n
    p_queue = PriorityQueue()
    distances[begin] = 0
    for e,w in graph[begin]:
        p_queue.put((begin,e,w)) # begin, end, weight of edge

    while not p_queue.empty():
        b,e,w = p_queue.get()
        if distances[e] > distances[b] + w:
            distances[e] = distances[b] + w
            for children,weight in graph[e]:
                p_queue.put((e,children,weight))

    return distances


def best_edge(graph,extra_edges,s,t):
    s_distances = Dijkstra_distances(graph,s) # runing twice Dijkstra, to find lowest distances to every vertices, from s, t vertex
    t_distances = Dijkstra_distances(graph,t)
    best_edge = False
    lowest_distance = s_distances[t] + 0 # removing reverence

    for b,e,w in extra_edges:
        if s_distances[b] + t_distances[e] + w < lowest_distance:
            lowest_distance = s_distances[b] + t_distances[e] + w
            best_edge = b,e,w
    return best_edge


# undirected graph list adjacency
graph = [
    [(1,4),(3,3)],
    [(0,4),(4,10),(5,2)],
    [(3,9),(4,5),(5,6)],
    [(0,3),(2,9),(4,9)],
    [(1,10),(2,5),(3,9),(5,7)],
    [(1,2),(2,6),(4,7)]
]

extra_edges = [(0,4,15),(4,0,15),(1,0,3),(2,5,7),(5,2,7),(1,4,3),(4,1,3),(2,4,1),(4,2,1)]

print(best_edge(graph,extra_edges,0,4))