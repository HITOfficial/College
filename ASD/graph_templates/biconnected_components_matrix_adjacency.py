# finding all biconnedted compoeonets on modyficated algorithm to find all articulation points
# representation: undirected connected graph on matrix adjacency

# complexity:
# - time O(V^2)
# - space O(v)


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
    # now, when alg found all articulation points, need to take from memory a number of subtrees in DFS tree
    for u in p:
        # adding +1 on DFS tree subtees, becouse graph is connected, and all vertices has one edge connection to parent in DFS tree
        biconnections.append((u, children[u]+1))
    return biconnections


def biconnected_components(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    children = [0]*n
    time = Time()
    DFS(graph, n, d, children, time, u)
    lowest(graph, n, d, low, u, u)
    # returning a list of tuples bicoonected components: vertex, biconnections number
    return find_biconnected_components(graph, n, children, low, d)


graph1 = [
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
]

graph2 = [[0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0]]

graph3 = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0],
]

graph4 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 0],
]

graph5 = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0],
]


M2 = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 0],
      [1, 1, 0, 1, 1, 1, 1, 0, 0],
      [0, 0, 1, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 1, 1],
      [0, 0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 0]]

print(biconnected_components(graph1))
print(biconnected_components(graph2))
print(biconnected_components(graph3))
print(biconnected_components(graph4))
print(biconnected_components(graph5))
print(biconnected_components(M2))
