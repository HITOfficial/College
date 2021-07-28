# finding all connected components on modification algorithm to find all articulation points, and returning index of vertex with the most biconnections
# representation: undirected connected graph on matrix adjacency

# complexity:
# - time O(V^2)
# - space O(V)


class Time:
    def __init__(self):
        self.time = 0


def DFS(graph, n, times, children, time, u):
    time.time += 1
    times[u] = time.time
    for v in range(n):
        if graph[u][v] != 0 and times[v] == float("inf"):
            children[u] += 1
            DFS(graph, n, times, children, time, v)


def lowest(graph, n, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in range(n):
        if graph[u][v] == 1 and v != prev and low[v] == float("inf"):
            lowest(graph, n, times, low, v, u)
        if graph[u][v] == 1:
            low[u] = min(low[u], times[v])


def find_biconnected_components(graph, n, children, low, d):
    p = []
    biconnections = []
    if children[0] >= 2:
        biconnections.append((0, children[0]))
    for u in range(1, n):
        flag = False
        for v in range(n):
            if graph[u][v] == 1 and d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    for u in p:
        biconnections.append((u, children[u]+1))
    return biconnections


def biconnections(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    children = [0]*n
    time = Time()
    DFS(graph, n, d, children, time, u)
    lowest(graph, n, d, low, u, u)
    p = find_biconnected_components(graph, n, children, low, d)
    if len(p) == 0:
        return None
    else:
        p = max([(el, idx) for idx, el in p])
        if p[0] < 2:
            return None
        else:
            return p[1]


graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

print(biconnections(graph))
