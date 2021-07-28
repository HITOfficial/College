# representation: directed graph on matrix adjacency

# complexity:
# - time O(F*V^2) -> where F is max flow in algorithm: in the worst case ( DFS in graph will go F times with edges of weight 1)
# - space O(V^2) -> constricting and memorizing edges in residual network


def DFS_flow_path(graph, residual_newtwork, n, path, visited, actual, sink):
    visited[actual] = True
    # to stop DFS algorithm faster in some cases, if found path to sink, algorithm will stop
    if visited[sink] is True:
        return
    for neighbour in range(n):
        if (graph[actual][neighbour] != 0 or residual_newtwork[actual][neighbour] != 0) and visited[neighbour] is False:
            path[neighbour] = actual
            if DFS_flow_path(graph, residual_newtwork, n, path, visited, neighbour, sink):
                return


def max_flow_Ford_Fulkerson(graph, source=0, sink=None):
    n = len(graph)
    if sink is None:
        sink = max(n-1, 0)
    max_flow = 0
    # creating residual network to memorize backtracking edges, after updating flow
    residual_network = [[0]*n for _ in range(n)]
    while True:
        actual = source
        path = [None]*n
        visited = [False]*n
        # checking if can update max flow
        DFS_flow_path(graph, residual_network, n, path, visited, source, sink)
        # cannot get into destination
        if visited[sink] is False:
            break
        current_flow = float("inf")
        actual = sink
        # finding flow to update max flow
        while actual != source:
            current_flow = min(current_flow, graph[path[actual]][actual])
            actual = path[actual]
        # updating residual newtwork and network from actual flow
        max_flow += current_flow
        actual = sink
        while actual != source:
            graph[path[actual]][actual] -= current_flow
            residual_network[actual][path[actual]] += current_flow
            actual = path[actual]
    return max_flow


graph = [
    [0, 5, 7, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 0, 6, 4, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


print(max_flow_Ford_Fulkerson(graph, 0, 5))
