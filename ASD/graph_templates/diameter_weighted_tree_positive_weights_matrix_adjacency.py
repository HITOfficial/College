# representation: connected undirected graph on matrix adjacency

# complexity:
# - time O(V^2)
# - space O(V)


def best_vertex(n, distances, visited):
    vertex, distance = 0, float("inf")
    for i in range(n):
        if visited[i] is False and distances[i] < distance:
            vertex, distance = i, distances[i]
    return vertex


def Dijkstra(graph, n, u):
    distances = [float("inf")]*n
    distances[u] = 0
    visited = [False]*n
    path = [None]*n
    for _ in range(n):
        vertex = best_vertex(n, distances, visited)
        visited[vertex] = True
        for neighbour in range(n):
            if visited[neighbour] is False and graph[vertex][neighbour] != 0 and distances[neighbour] > distances[vertex] + graph[vertex][neighbour]:
                distances[neighbour] = distances[vertex] + \
                    graph[vertex][neighbour]
                path[neighbour] = vertex
    return distances, path


def get_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u]))
    return p


def max_dist(distances):
    idx, max_dist = 0, 0
    for i, d in enumerate(distances):
        if d > max_dist:
            max_dist = d
            idx = i
    return idx


def diameter_tree_positive_weights(graph):
    n = len(graph)
    distances, _ = Dijkstra(graph, n, 0)
    left_end = max_dist(distances)
    # running second time Dijkstra
    distances, path = Dijkstra(graph, n, left_end)
    right_end = max_dist(distances)
    diameter = get_path(path, right_end)
    return distances[right_end], diameter


graph = [
    [0, 1, 0, 0, 2, 3, 7],
    [1, 0, 7, 0, 3, 0, 0],
    [0, 7, 0, 6, 0, 12, 0],
    [0, 0, 6, 0, 2, 0, 0],
    [2, 3, 0, 2, 0, 0, 4],
    [3, 0, 12, 0, 0, 0, 0],
    [7, 0, 0, 0, 4, 0, 0]
]

print(diameter_tree_positive_weights(graph))
