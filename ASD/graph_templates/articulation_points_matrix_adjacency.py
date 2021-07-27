# undirected graph
# is articulation point if:
# - vertiex is a root element, and have more than one children
# - or actual vertex is not a root element, but have a children which low number is lower or equal actual executing element

# complexity:
# -time O(V^2)
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
        # vertex wasn't executed before
        if low[v] == float("inf"):
            lowest(graph, n, times, low, v, u)
        # cannot backtrack to previous vertex
        if graph[u][v] == 1 and v != prev:
            low[u] = min(low[u], low[v])


def articulation_points(graph, u=0):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    time = Time()
    # DFS executing times
    DFS(graph, d, n, time, u)
    # modyfied DFS, finding candidates to articular points
    lowest(graph, n, d, low, u, u)
    p = find_articulation_points(graph, n, low, d)

    return p


# DFS alg to check if graph is an acyclic tree
def acyclic_tree(graph, n, visited, u, prev):
    visited[u] = True
    for v in range(n):
        if graph[u][v] == 1 and v != prev:
            # graph has a cycle
            if visited[v] is True:
                return False
            else:
                return acyclic_tree(graph, n, visited, v, u)
    return True


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
    # checking if is a root of acyclic tree, becouse if is not, need to remove first added element
    visited = [False]*n
    # graph has a cycle so is not acyclic
    if acyclic_tree(graph, n, visited, u, u) is False:
        if len(p) > 0:
            p.pop(0)
    return p


graph = [
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
]

print(articulation_points(graph))
