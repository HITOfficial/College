# Graph representation: undirected weighted graph on matrix adjacency

# complexity:
# - time O(E*V^2))
# - space O(V)


def get_path(paths, actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths, paths[actual]))
    return path


# Dijkstra alg. from templates
def best_vertex(n, distances, visited):
    vertex, distance = 0, float("inf")
    for i in range(n):
        if visited[i] is False and distances[i] < distance:
            vertex, distance = i, distances[i]
    return vertex


def Dijkstra(graph, u, v):
    n = len(graph)
    distances = [float("inf")]*n
    distances[u] = 0
    visited = [False]*n
    paths = [None]*n
    for _ in range(n):
        vertex = best_vertex(n, distances, visited)
        visited[vertex] = True
        for neighbour in range(n):
            # not visited vertex, to whose is lower distance using actual visited vertex, and edge between
            if visited[neighbour] is False and graph[vertex][neighbour] != 0 and distances[neighbour] > distances[vertex] + graph[vertex][neighbour]:
                paths[neighbour] = vertex
                distances[neighbour] = distances[vertex] + \
                    graph[vertex][neighbour]
    return distances[v], paths


def min_cycle(graph):
    n = len(graph)
    min_cycle_weight, min_cycle_path, a, b = float("inf"), [], 0, 0
    for u in range(n-1):
        for v in range(u+1, n):
            # checking if has connection
            if graph[u][v] != 0:
                w = graph[u][v]
                # removing edge connection between vertices
                graph[u][v] = 0
                graph[v][u] = 0
                dist, path = Dijkstra(graph, u, v)
                # adding again connections betweeen
                graph[u][v] = w
                graph[v][u] = w
                # adding weight of removed edge
                dist += w
                if dist < min_cycle_weight:
                    min_cycle_weight, min_cycle_path, a, b = dist, path, u, v
    # condition if is cycle in graph
    if min_cycle_weight == float("inf"):
        return
    else:
        return min_cycle_weight, list(reversed(get_path(min_cycle_path, b))) + [a]


graph = [
    [0, 5, 7, 0],
    [5, 0, 23, 3],
    [7, 23, 0, 6],
    [0, 3, 6, 0],
]

print(min_cycle(graph))
