# Problem: counting all edges on shortest paths
# Graph representation: undirected, weighted on list adjacency, with positive edge weights
from queue import PriorityQueue

# complexity:
# - time O(ElogV) / O(K*V), counting all edges on shortest paths, where K is a number of shortest paths
# - space O(V^2) -> dynamic boolean all edges


def paths_edges(parent, edges, u):
    counter = 0
    if u is not None:
        # checking if was used actual edge in another shortest path
        if parent[u] is not None and not edges[u][parent[u]]:
            edges[u][parent[u]] = True
            edges[parent[u]][u] = True
            counter += 1
        counter += paths_edges(parent, edges, parent[u])
    return counter


# Dijkstra list adjacency
def Dijkstra_distance(graph, n, b, e, flag=False, d=None):
    n = len(graph)
    distances = [float("inf")]*n
    distances[b] = 0
    p_queue = PriorityQueue()
    e_good_vertex = [False]*n
    parent = [None]*n
    for k, w in graph[b]:
        p_queue.put((w, b, k))
    while not p_queue.empty():
        w, u, v = p_queue.get()
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            parent[v] = u
            for k, weight in graph[v]:
                p_queue.put((weight, v, k))
        # when running second time Dijkstra memorizing, every edge connected to e, which creating shortest path
        if flag is True and v == e and d == distances[u] + w:
            e_good_vertex[u] = True
    return distances[e], parent, e_good_vertex


def paths(graph, s, t):
    n = len(graph)
    # memorizing distance to reach only once
    d, _, _ = Dijkstra_distance(graph, n, s, t)
    _, parent, e_good_edges = Dijkstra_distance(graph, n, s, t, True, d)
    edges = [[False]*n for _ in range(n)]
    counter = 0
    for i in range(n):
        if e_good_edges[i] is True:
            # counting used edges
            edges[t][i] = True
            edges[i][t] = True
            # counting number of edges on every shortest path
            counter += 1 + paths_edges(parent, edges, i)
    return counter


G = [
    [(1, 2), (2, 4)],
    [(0, 2), (3, 11), (4, 3)],
    [(0, 4), (3, 13)],
    [(1, 11), (2, 13), (5, 17), (6, 1)],
    [(1, 3), (5, 5)],
    [(3, 17), (4, 5), (7, 7)],
    [(3, 1), (7, 3)],
    [(5, 7), (6, 3)]
]
s, t = 0, 7


print(paths(G, s, t))
