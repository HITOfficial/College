# finding max matching in undirected bipartite graph using Edmonds Karp max flow algorithm

from queue import Queue

# complexity:
# - time O(V*E^2)
# - space O(V)


# condition to check if graph is bipartite and reciving array
# 1:1 copy algorithm from: "bipartite_graph_matrix_adjacency.py"
def bipartite_graph(graph, s=0):
    n = len(graph)
    # color: 0, unvisited, -1: first color, 1: second color
    colors = [0]*n
    colors[s] = 1
    color = 1
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        next_queue = Queue()
        # changing color every next wave
        if color == 1:
            color = -1
        else:
            color = 1
        while not queue.empty():
            u = queue.get()
            for v in range(n):
                if graph[u][v] == 1:
                    if colors[v] == colors[u]:
                        return False, [], []
                    elif colors[v] == 0:
                        colors[v] = color
                        next_queue.put(v)
        queue = next_queue
    colorA, colorB = [], []
    for i in range(n):
        # graph is not connected
        if colors[i] == 0:
            return False, [], []
        elif colors[i] == 1:
            colorA.append(i)
        else:
            colorB.append(i)
    # returining boolean, idexdes for every color
    return True, colorA, colorB


# 1:1 copy algorithm from "max_flow_Edmonds_Karp_undirected_graph.py"
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
    # BFS with single queue
    while not queue.empty():
        u = queue.get()
        for v in range(n):
            if graph[u][v] > 0 and visited[v] is False:
                parent[v] = u
                visited[v] = True
                queue.put(v)
    if visited[sink]:
        k = sink
        # finding new flow to update total flow
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
        # adding new flow
        total_flow += flow.flow
        k = sink
        while k != source:
            graph[parent[k]][k] -= flow.flow
            graph[k][parent[k]] += flow.flow
            k = parent[k]
        # reseting flow value in Class
        flow.flow = float("inf")
    return total_flow


def max_matching_bipartite_graph(graph):
    n = len(graph)
    boolean, colorA, colorB = bipartite_graph(graph)
    # condition graph isn't bippartite
    if boolean is False:
        return False
    # updating graph by adding two vertices(source,sink)
    graph.append([0]*(n))
    graph.append([0]*(n))
    for i in range(n+2):
        graph[i].append(0)
        graph[i].append(0)
    # connecting all elements from first color with source
    for idx in colorA:
        graph[-2][idx] = 1
        graph[idx][-2] = 1
    # connecting all elements from second color with sink
    for idx in colorB:
        graph[-1][idx] = 1
        graph[idx][-1] = 1
    source, sink = n, n+1
    return max_flow_Edmonds_Karp_undirected_graph(graph, source, sink)


graph = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]

print(max_matching_bipartite_graph(graph))
