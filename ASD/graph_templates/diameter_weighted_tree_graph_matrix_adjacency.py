# representation: weighted  undirected tree graph on matrix adjacency
# edges can have positive and negative numbers but not equal 0


# complexity:
# - time O(V*E)
# - space O(V)


def Bellman_Ford_distances(graph, edges, n, b=0):
    distances = [float("inf")]*n
    distances[b] = 0
    path = [None]*n
    for _ in range(n):
        for e in edges:
            u, v, w = e
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                path[v] = u
    return distances, path


def convert_to_edges(graph, n):
    E = []
    for i in range(n-1):
        for j in range(i+1, n):
            # statement if has edge betweeen
            if graph[i][j] != 0:
                # tuple (vertices, edge weight)
                E.append((i, j, graph[i][j]))
                E.append((j, i, graph[i][j]))
    return E


def max_dist_index(distances, n):
    max_dist, index = -float("inf"), None
    for i in range(n):
        if max_dist < distances[i]:
            max_dist, index = distances[i], i
    return index


def get_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u]))
    return p


def diameter_weigted_graph(graph):
    n = len(graph)
    edges = convert_to_edges(graph, n)
    # running twice Bellman Ford algorithm
    distances, _ = Bellman_Ford_distances(graph, edges, n)
    index = max_dist_index(distances, n)
    # running second time Bellman ford shortest path
    distances, path = Bellman_Ford_distances(graph, edges, n, index)
    end_index = max_dist_index(distances, n)
    path = get_path(path, end_index)
    # returning total maximum distance, and path, which needn't be reversed, becouse in tree, from two sides is same diameter
    return distances[end_index], path


graph = [
    [0, 7, 8, 6, 5, 0, 0, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 3, 4],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
]

print(diameter_weigted_graph(graph))
