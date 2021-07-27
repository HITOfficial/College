# undirected graph
# is articulation point if:
# - vertiex is a root element, and have more than one children
# - or actual vertex is not a root element, but have a children which low number is lower or equal actual executing element

# complexity:
# - time O(V+E)
# - space O(v)


class Time:
    def __init__(self):
        self.time = 0


# DFS alg.
def DFS(graph, times, time, u):
    time.time += 1
    times[u] = time.time
    for v in graph[u]:
        # checking if is edge between vertices and new vertex wasn't visited before
        if times[v] == float("inf"):
            DFS(graph, times, time, v)


# modyfied DFS
def lowest(graph, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in graph[u]:
        # vertex wasn't executed before and cannot backtrack to previous vertex from DFS
        if v != prev and low[v] == float("inf"):
            lowest(graph, times, low, v, u)
        if v != prev:
            low[u] = min(low[u], low[v])


def find_articulation_points(graph, n, low, d):
    p = []
    for u in range(n):
        flag = False
        for v in graph[u]:
            # checking if parent vertex is an articulation point
            if d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    # checking if root vertex have at least 2 childrens
    if len(graph[0]) < 2:
        p.pop(0)
    return p


def articulation_points(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    time = Time()
    # DFS executing times
    DFS(graph, d, time, u)
    # modyfied DFS, finding candidates to articular points
    lowest(graph, d, low, u, u)
    # returning a list of articulating points
    return find_articulation_points(graph, n, low, d)


# Tests:
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

print(articulation_points(graph1))
print(articulation_points(graph2))
