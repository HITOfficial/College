# Prims MST alg. returning edges representing MST of graph
# Graph representation: connected undirected graph on matrix adjacency

# complexity:
# - time O(V^2)
# - space O(V) / O(E)


def best_vertex(n, distances, visited):
    lowest_dist, index = float("inf"), 0
    for idx in range(n):
        if visited[idx] is False and lowest_dist > distances[idx]:
            lowest_dist, index = distances[idx], idx
    return index


def Prims_MST_matrix_adjacency(graph):
    n = len(graph)
    MST_edges = []
    visited = [False]*n
    distances = [float("inf")]*n
    distances[0] = 0
    parent = [None]*n
    edges = 0
    while edges < n:
        u = best_vertex(n, distances, visited)
        visited[u] = True
        # adding edges to MST, condition to do not take edge on beggining of algorithm
        if parent[u] is not None:
            MST_edges.append((parent[u], u))
        edges += 1
        for v in range(n):
            if graph[u][v] != 0 and distances[v] > distances[u] + graph[u][v]:
                parent[v] = u
                distances[v] = distances[u] + graph[u][v]
    return MST_edges


graph = [
    [0, 1, 0, 0, 2, 3, 7],
    [1, 0, 7, 0, 3, 0, 0],
    [0, 7, 0, 6, 0, 12, 0],
    [0, 0, 6, 0, 2, 0, 0],
    [2, 3, 0, 2, 0, 0, 4],
    [3, 0, 12, 0, 0, 0, 0],
    [7, 0, 0, 0, 4, 0, 0]
]

print(Prims_MST_matrix_adjacency(graph))
