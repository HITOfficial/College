# undirected graph
# is articulation point if:
# - root vertex, have more than one children in DFS tree
# - other vertex is a articulation point if  has a children which low number is lower or equal actual executing element

# complexity:
# - time O(V^2)
# - space O(v)


class Time:
    def __init__(self):
        self.time = 0


# DFS alg. with memorizing number of children in DFS tree
def DFS(graph, n, times, children, time, u):
    time.time += 1
    times[u] = time.time
    for v in range(n):
        # checking if is edge between vertices and new vertex wasn't visited before
        if graph[u][v] != 0 and times[v] == float("inf"):
            children[u] += 1
            DFS(graph, n, times, children, time, v)


# modyfied DFS to find low number for every vertices
def lowest(graph, n, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in range(n):
        # vertex wasn't executed before and cannot backtrack to previous vertex from DFS
        if graph[u][v] == 1 and v != prev and low[v] == float("inf"):
            lowest(graph, n, times, low, v, u)
        if graph[u][v] == 1:
            low[u] = min(low[u], times[v])


def find_articulation_points(graph, n, children, low, d):
    p = []
    # checking root vertex if has at least two children in DFS tree
    if children[0] >= 2:
        p.append(0)
    for u in range(1, n):
        flag = False
        for v in range(n):
            # checking if parent vertex is an articulation point
            if u != 0 and graph[u][v] == 1 and d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    return p


def articulation_points(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    # memorizing number of children in DFS tree
    children = [0]*n
    time = Time()
    # DFS executing times
    DFS(graph, n, d, children, time, u)
    # modyfied DFS, finding candidates to articular points
    lowest(graph, n, d, low, u, u)
    # returning a list of articulating points
    return find_articulation_points(graph, n, children, low, d)


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

print(articulation_points(graph1))
print(articulation_points(graph2))
print(articulation_points(graph3))
print(articulation_points(graph4))
print(articulation_points(graph5))
print(articulation_points(M2))
