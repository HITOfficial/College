# Hierholzers algorithm to find Eulerian circuit path
# graph representation: undirected graph on list adjacency

# inspiration: https://www.youtube.com/watch?v=8MpoO2zA2l4


from collections import deque
# using deque as a stack to memorize path to append left in O(1)

# complexity:
# - time O(E)
# - space O(E) / O(V)


# almost 1:1 alg as alg. to find Euelrian path, only one change is that, all vertices need to have even number of edges
def has_Eulerian_circuit(graph, edges, n):
    for i in range(n):
        edges[i] = len(graph[i])
        if edges[i] % 2 == 1:
            return False
    return True


def DFS_visit_edges(graph, edges, path, u):
    while edges[u] > 0:
        v = graph[u].pop()
        # removing same edge in source and in sing
        for idx in range(len(graph[v])):
            if graph[v][idx] == u:
                graph[v].pop(idx)
                break
        edges[u] -= 1
        edges[v] -= 1
        DFS_visit_edges(graph, edges, path, v)
    path.appendleft(u)


def Eulerian_path(graph):
    n = len(graph)
    edges = [0]*n
    has_path = has_Eulerian_circuit(graph, edges, n)
    # condition if graph has eulerian path
    if not has_path:
        return False
    path = deque()
    DFS_visit_edges(graph, edges, path, 0)
    return list(path)


graph = [
    [1, 2],
    [0, 2],
    [3, 5],
    [2, 4, 11, 12],
    [3, 5],
    [2, 4, 6, 10],
    [5, 7, 9, 10],
    [6, 8, 9, 10],
    [7, 9],
    [6, 7, 8, 10],
    [5, 6, 7, 9],
    [3, 12],
    [3, 11],
]

print(Eulerian_path(graph))
