# finding all biconnedted compoeonets on modyficated algorithm to find all articulation points
# representation: undirected connected graph on matrix adjacency

# complexity:
# - time O(V+E)
# - space O(v)


class Time:
    def __init__(self):
        self.time = 0


def DFS(graph, times, children, time, u):
    time.time += 1
    times[u] = time.time
    for v in graph[u]:
        if times[v] == float("inf"):
            children[u] += 1
            DFS(graph, times, children, time, v)


def lowest(graph, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in graph[u]:
        if v != prev and low[v] == float("inf"):
            lowest(graph, times, low, v, u)
        low[u] = min(low[u], times[v])


def find_biconnected_components(graph, n, children, low, d):
    p = []
    biconnections = []
    if children[0] >= 2:
        biconnections.append((0, children[0]))
    for u in range(1, n):
        flag = False
        for v in graph[u]:
            if d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    # now, when alg found all articulation points, need to take from memory a number of subtrees in DFS tree
    for u in p:
        # adding +1 on DFS tree subtees, becouse graph is connected, and all vertices has one edge connection to parent in DFS tree
        biconnections.append((u, children[u]+1))
    return biconnections


def biconnect_components(graph):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    children = [0]*n
    time = Time()
    DFS(graph, d, children, time, 0)
    lowest(graph, d, low, 0, 0)
    return find_biconnected_components(graph, n, children, low, d)


graph1 = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2, 4],
    [3, 5, 6],
    [4, 6],
    [4, 5],
]

graph2 = [
    [3],
    [4],
    [5],
    [0, 6],
    [1, 6],
    [2, 6],
    [3, 4, 5],
]

print(biconnect_components(graph1))
print(biconnect_components(graph2))
