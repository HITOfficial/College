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


def edge_statement(M, distances, n, d, i, j):
    # close to much, or moving using single edge/ two verices in the same point / replacing vertices
    if distances[j//n][j % n] < d or j//n == j % n or i//n == i % n or (i//n == j % n and i % n == j//n):
        return 0
    # first car stay in place
    elif i//n == j//n and M[i % n][j % n] > 0:
        return 1
    # second car stay in place
    elif i % n == j % n and M[i//n][j//n] > 0:
        return 1
    # two cars changing position
    elif M[i//n][j//n] > 0 and M[i % n][j % n] > 0:
        return 1
    else:
        return 0


def keep_distance(M, x, y, d):
    distances = Floyd_Warshall(M)
    # creating V^2 vertices, constructing graph and than running BFS to find path
    n = len(M)
    n2 = n**2
    # 1st type of constructing graph
    graph = [[0 if (M[i//n][j//n] == 0 and i//n != j//n) or (M[i % n][j % n] == 0 and i % n != j % n) or (j//n == i % n and j % n == i//n) or j//n == j % n or i//n ==
              i % n else 1 if distances[j//n][j % n] >= d else 0 for j in range(n**2)] for i in range(n**2)]
    # second type
    graph2 = [[edge_statement(M, distances, n, d, i, j)
               for j in range(n2)] for i in range(n2)]

    path = BFS_path(graph, n, n2, x, y)
    path2 = BFS_path(graph2, n, n2, x, y)
    return list(reversed(get_path(path, y*n+x, n))), list(reversed(get_path(path2, y*n+x, n)))


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
