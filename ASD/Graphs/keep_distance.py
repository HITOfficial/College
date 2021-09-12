from queue import Queue

# complexity:
# - time O(V^4)
# - space O(V^4) -> constructing graph


def get_path(path, u, n):
    p = []
    if u is not None:
        p.append((u//n, u % n))
        p.extend(get_path(path, path[u], n))
    return p


def BFS_path(graph, n, n2, b, e):
    queue = Queue()
    visited = [False]*n2
    visited[b*n+e] = True
    parent = [None]*n2
    queue.put(b*n+e)
    while not queue.empty():
        u = queue.get()
        for v in range(n2):
            if graph[u][v] == 1 and visited[v] is False:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    # found path
    return parent


# O(V^3) -> Floyd Warshall alg. from templates -> all minimal distances between every vertices
def Floyd_Warshall(graph):
    n = len(graph)
    distances = [[0 if u == v else float(
        "inf") if graph[u][v] == 0 else graph[u][v] for v in range(n)] for u in range(n)]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distances[u][v] > distances[u][k] + distances[k][v]:
                    distances[u][v] = distances[u][k] + distances[k][v]
    return distances


def keep_distance(M, x, y, d):
    distances = Floyd_Warshall(M)
    # creating V^2 vertices, constructing graph and than running BFS to find path
    n = len(M)
    n2 = n**2
    graph = [[0 if (M[i//n][j//n] == 0 and i//n != j//n) or (M[i % n][j % n] == 0 and i % n != j % n) or (j//n == i % n and j % n == i//n) or j//n == j % n or i//n ==
              i % n else 1 if distances[j//n][j % n] >= d else 0 for j in range(n**2)] for i in range(n**2)]

    path = BFS_path(graph, n, n2, x, y)
    return list(reversed(get_path(path, y*n+x, n)))


M1 = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

M = [
    [0, 5, 1, 0, 0, 0],
    [5, 0, 0, 5, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 5, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

print(keep_distance(M1, 0, 5, 1))
print(keep_distance(M, 0, 5, 4))
