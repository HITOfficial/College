# Floyd Warshall algorithm, to find all shortest paths between every veritces
# algorithm works graph representation: matrix adjacency directed / undirected

# complexity:
# - time O(V^3)
# - space O(V^2) / O(V^2*P), where P in a length of single path


def get_path(paths, u, v):
    path = []
    if v is not None:
        path.append(v)
        path.extend(get_path(paths, u, paths[u][v]))
    return path


def Floyd_Warshall(graph):
    n = len(graph)
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

    # reconstructed path between every fertices in direceted/ undirected graph
    constructed_paths = [[list(reversed(get_path(paths, i, j)))
                          for j in range(n)] for i in range(n)]

    return distances, constructed_paths


graph = [
    [0, 1, 0, 0, 2, 3, 7],
    [1, 0, 7, 0, 3, 0, 0],
    [0, 7, 0, 6, 0, 12, 0],
    [0, 0, 6, 0, 2, 0, 0],
    [2, 3, 0, 2, 0, 0, 4],
    [3, 0, 12, 0, 0, 0, 0],
    [7, 0, 0, 0, 4, 0, 0]
]

print(Floyd_Warshall(graph))
