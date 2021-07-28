# undirected graph
# is articulation point if:
# - root vertex, have more than one children in DFS tree
# - other vertex is a articulation point if  has a children which low number is lower or equal actual executing element

# complexity:
# - time O(V+E)
# - space O(v)


class Time:
    def __init__(self):
        self.time = 0


# DFS alg. with memorizing number of children in DFS tree
def DFS(graph, times, children, time, u):
    time.time += 1
    times[u] = time.time
    for v in graph[u]:
        # checking if is edge between vertices and new vertex wasn't visited before
        if times[v] == float("inf"):
            children[u] += 1
            DFS(graph, times, children, time, v)


# modyfied DFS to find low number for every vertices
def lowest(graph, times, low, u, prev):
    low[u] = min(low[u], times[u])
    for v in graph[u]:
        # vertex wasn't executed before and cannot backtrack to previous vertex from DFS
        if v != prev and low[v] == float("inf"):
            lowest(graph, times, low, v, u)
        low[u] = min(low[u], times[v])


def find_articulation_points(graph, n, children, low, d):
    p = []
    # checking root vertex if has at least two children in DFS tree
    if children[0] >= 2:
        p.append(0)
    for u in range(1, n):
        flag = False
        for v in graph[u]:
            # checking if parent vertex is an articulation point
            if d[u] <= low[v]:
                flag = True
                break
        if flag is True:
            p.append(u)
    return p


def articulation_points(graph):
    n = len(graph)
    d = [float("inf")]*n
    low = [float("inf")]*n
    # memorizing number of children in DFS tree
    children = [0]*n
    time = Time()
    # DFS executing times
    DFS(graph, d, children, time, 0)
    # modyfied DFS, finding candidates to articular points
    lowest(graph, d, low, 0, 0)
    # returning a list of articulating points
    return find_articulation_points(graph, n, children, low, d)


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
