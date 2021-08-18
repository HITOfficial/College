# Edmonds Karp max flow in undirected graph on matrix adjacency

from queue import Queue


# complexity:
# - time O(V*E^2)
# - memory O(V), memorizing only path from source to sink, without creating extra residual network


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


graph = [
    [0, 10, 10, 4, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
]

print(max_flow_Edmonds_Karp_undirected_graph(graph))
