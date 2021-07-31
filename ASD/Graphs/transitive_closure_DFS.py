# algorithm: runing V times topological sort algorithm, to

# representation: directed, unweighted graph on list adjacency

# complexity:
# -time O(V*(V+E))
# -space O(V)


class Time():
    def __init__(self):
        self.time = 0


def DFS_visit(graph, n, visited, time, path, u):
    path = []
    time.time += 1
    visited[u] = True
    for v in graph[u]:
        if visited[v] is False:
            path.extend(DFS_visit(graph, n, visited, time, path, v))
    return [u] + path


def transitive_closure(graph):
    n = len(graph)
    path = []
    for u in range(n):
        time = Time()
        visited = [False]*n
        path = DFS_visit(graph, n, visited, time, path, u)
        # if DFS will start from vertex with index u, algorithm will find tansitive closure
        if time.time == n:
            break
    return path


graph = [
    [4, 5],
    [0],
    [0, 1],
    [0, 2],
    [],
    [],
]


print(transitive_closure(graph))
