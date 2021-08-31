# Graph representation: directed weighted graph on matrix adjacency

# compelxity:
# - time O(V^3)
# - space O(V^2)


def get_path(paths, u, v):
    path = []
    if v is not None:
        path.append(v)
        path.extend(get_path(paths, u, paths[u][v]))
    return path


# copy of Floyd Warshall alg.
def Floyd_Warshall(graph, n):
    distances = [[0 if u == v else float(
        "inf") if graph[u][v] == 0 else graph[u][v] for v in range(n)] for u in range(n)]
    paths = [[None if u == v else u if graph[u][v] !=
              0 else None for v in range(n)] for u in range(n)]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distances[u][v] > distances[u][k] + distances[k][v]:
                    distances[u][v] = distances[u][k] + distances[k][v]
                    paths[u][v] = paths[k][v]
    return distances, paths


def min_cycle(graph):
    n = len(graph)
    distances, paths = Floyd_Warshall(graph, n)
    # each edge
    a, b, min_cycle_weight = 0, 0, float("inf")
    for u in range(n-1):
        for v in range(u+1, n):
            if distances[u][v] + distances[v][u] < min_cycle_weight:
                a, b, min_cycle_weight = u, v, distances[u][v] + \
                    distances[v][u]
    a_b_path = list(reversed(get_path(paths, a, b)))
    # to not return in path same vertex
    a_b_path.pop()
    b_a_path = list(reversed(get_path(paths, b, a)))
    if min_cycle_weight == float("inf"):
        return
    else:
        # returning minimal cycle with path of it
        return min_cycle_weight, a_b_path + b_a_path


graph = [
    [0, 0, 7, 0],
    [5, 0, 0, 0],
    [0, 0, 0, 6],
    [0, 3, 0, 0],
]

print(min_cycle(graph))
