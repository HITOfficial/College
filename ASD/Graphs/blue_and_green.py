# Given is a weighted undirected graph represented by the matrix T by three n × n (for
# each i, j. T [i] [j] = T [j] [i]; the value of T [i] [j]> 0 means that the edge exists between
# vertex and vertex j with weight T [i] [j]). The real number d is also given. Every
# vertex in G has one of the colors green or blue. Suggest an algorithm that determines
# Natural correction `, such that in the graph` there are pairs of vertices (p, q) ∈ V × V satisfying the conditions:
# 1.q is green and p is blue,
# 2. the distance between p and q (calculated as the sum of the edge of the leading edge) is not the shortest segment than d,
# 3. every vertex.
# The solution should be implemented as a function: def Blue Green (T, K, D):
# T: graph represented by a square adjacency matrix, where 0 means none edge, and a number greater than 0 represents the distance between the vertices,
# K: name list, vertex colors
# D: distance referred to in condition 2 of the job description.

from queue import Queue

# complexity:
# - time O(f*V^2), where f is a maximal flow
# - space O(V^2), disteces between every vertices from  Floyd Warshall alg.


# max flow alg. from graph templates
class Flow():
    def __init__(self, flow=float("inf")):
        self.flow = flow

    def updateFlow(self, f):
        if f < self.flow:
            self.flow = f


def BFS_find_path(graph, n, flow, parent, source, sink):
    visited = [False]*n
    visited[source] = True
    queue = Queue()
    queue.put(source)
    while not queue.empty():
        u = queue.get()
        for v in range(n):
            if graph[u][v] > 0 and visited[v] is False:
                parent[v] = u
                visited[v] = True
                queue.put(v)
    if visited[sink]:
        k = sink
        while k != source:
            flow.updateFlow(graph[parent[k]][k])
            k = parent[k]
        return True
    else:
        return False


def max_flow_Edmonds_Karp_undirected_graph(graph, source=0, sink=None):
    n = len(graph)
    if sink is None:
        sink = max(n-1, 0)
    parent = [None]*n
    flow = Flow()
    total_flow = 0
    while BFS_find_path(graph, n, flow, parent, source, sink):
        total_flow += flow.flow
        k = sink
        while k != source:
            graph[parent[k]][k] -= flow.flow
            graph[k][parent[k]] += flow.flow
            k = parent[k]
        flow.flow = float("inf")
    return total_flow


# Floyd Warshall distances O(V^3)
def Floyd_Warshall(graph, n):
    distances = [[0 if i == j else graph[i][j] if graph[i][j] !=
                  0 else float("inf") for j in range(n)] for i in range(n)]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distances[u][v] > distances[u][k] + distances[k][v]:
                    distances[u][v] = distances[u][k] + distances[k][v]
    # returning distances between every vertices
    return distances


def blue_and_green(T, K, D):
    n = len(T)
    graph = [[0]*(n+2) for _ in range(n+2)]
    # index: source -> n, sink -> n+1
    distances = Floyd_Warshall(T, n)
    for u in range(n):
        for v in range(n):
            # q -> green, p -> blue
            if distances[u][v] >= D and K[u] == "B" and K[v] == "G":
                # between blue and green
                graph[u][v] = 1
                graph[v][u] = 1
                # between source and blue
                graph[n][u] = 1
                graph[u][n] = 1
                # between green and sink
                graph[v][n+1] = 1
                graph[n+1][v] = 1
    return max_flow_Edmonds_Karp_undirected_graph(graph, n, n+1)


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
K = ["B", "B", "G", "G", "B"]
D = 2

print(blue_and_green(T, K, D))
