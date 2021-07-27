# undirected graph
# is articulation point if:
# - vertiex is a root element, and have more than one children
# - or actual vertex is not a root element, but have a children which low number is lower or equal actual executing element

# complexity:
# - time O(V^2)
# - space O(v)


class Time:
    def __init__(self):
        self.time = 0


# DFS alg.
def DFS(graph, times, n, time, u):
    time.time += 1
    times[u] = time.time
    for v in range(n):
        # checking if is edge between vertices and new vertex wasn't visited before
        if graph[u][v] != 0 and times[v] == float("inf"):
            DFS(graph, times, n, time, v)


# modyfied DFS
def lowest(graph, n, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in range(n):
        # vertex wasn't executed before and cannot backtrack to previous vertex from DFS
        if graph[u][v] == 1 and v != prev and low[v] == float("inf"):
            lowest(graph, n, times, low, v, u)
        if graph[u][v] == 1 and v != prev:
            low[u] = min(low[u], low[v])


def find_articulation_points(graph, n, low, d):
    p = []
    for u in range(n):
        flag = False
        for v in range(n):
            # checking if parent vertex is an articulation point
            if graph[u][v] == 1 and d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    # vertex is a root element and have at least 2 childrens
    first_vertex_sum = sum(graph[0])
    if first_vertex_sum < 2:
        p.pop(0)
    return p


def articulation_points(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    time = Time()
    # DFS executing times
    DFS(graph, d, n, time, u)
    # modyfied DFS, finding candidates to articular points
    lowest(graph, n, d, low, u, u)
    # returning a list of articulating points
    return find_articulation_points(graph, n, low, d)


# Tests:
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

print(articulation_points(graph1))
print(articulation_points(graph2))
print(articulation_points(graph3))
print(articulation_points(graph4))
