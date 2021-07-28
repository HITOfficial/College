# Edmonds Karp algorithm to find max flow in network
# representation: directed graph on matrix adjacency
from queue import Queue

# complexity:
# - time O(V*E^2)
# - memory O(V^2) -> creating residual network


def BFS_find_flow(network, residual_network, n, source, sink):
    path = [None]*n
    flow = [float("inf")]*n
    queue = Queue()
    queue.put(source)
    while not queue.empty():
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for neighbour in range(n):
                if flow[neighbour] == float("inf"):
                    # maximum capacity what can taken is minimum value of edge weight, and capacity to parent
                    # default edge remaing capacity
                    if network[actual][neighbour] != 0:
                        flow[neighbour] = min(
                            network[actual][neighbour], flow[actual])
                        path[neighbour] = actual
                        next_queue.put(neighbour)
                    # residual edge capacity
                    elif residual_network[actual][neighbour] != 0:
                        flow[neighbour] = min(
                            residual_network[actual][neighbour], flow[actual])
                        path[neighbour] = actual
                        next_queue.put(neighbour)
        queue = next_queue
    # returning actual flow what can be done, and path to recreate
    return flow[sink], path


def max_flow_Edmonds_Karp(graph, source=0, sink=None):
    n = len(graph)
    if sink is None:
        sink = max(n-1, 0)
    max_flow = 0
    residual_network = [[0]*n for _ in range(n)]
    while True:
        new_flow, path = BFS_find_flow(
            graph, residual_network, n, source, sink)
        # checking if found path, to destionation vertex
        if new_flow == float("inf"):
            break
        actual = sink
        while actual != source:
            graph[path[actual]][actual] -= new_flow
            residual_network[actual][path[actual]] += new_flow
            actual = path[actual]
        # updating maximum flow in network
        max_flow += new_flow
    return max_flow


graph = [
    [0, 5, 7, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 0, 6, 4, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

print(max_flow_Edmonds_Karp(graph))
