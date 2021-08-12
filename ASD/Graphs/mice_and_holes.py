# Owls will atack mice, if they would't hide on time,
# mice can do maximal d distance move in 2dim, single hole can hide maximum K mice
# try to save mice as much as you can


# complexity:
# - time O(F*N^2) -> where F is max flow in algorithm: in the worst case ( DFS in graph will go F times with edges of weight 1)
# - space O(N^2) -> constructing graph to find max_flow, and extra array for residual network
# where N = M+H+2, M,H are length of mice and holes array

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


# 1:1 copy max flow Ford Fulkerson algorithm from graph templates
def max_flow_Ford_Fulkerson(graph, n, source, sink):
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


def distance(a, b):
    ax, ay = a
    bx, by, _ = b
    # length of vertor |ab|
    return ((ax-bx)**2 + (ay-by)**2)**(1/2)


def costruct_graph(M, H, distances, d, len_M, len_H):
    # edges between source and mice are directed with weight(1)
    # edges between holes and sink has weight of hole capacity
    # directed edge between vertices mouse -> hole has weight(1) single mouse
    # graph size (M+H+2) x (M+H+2), +2 becouse extra vertex: source, sink
    len_M, len_H = len(M), len(H)
    n = len_M + len_H+2
    graph = [[0]*n for _ in range(n)]
    # creating directed edges between mice and holes
    for i in range(len_M):
        for j in range(len_H):
            if distances[i][j] <= d:
                # edge between mouse and hole of weight one
                graph[i+1][len_M+j+1] = 1
    for i in range(1, len_M+1):
        # edge between source and every mouse vertex
        graph[0][i] = 1
    for i in range(len_H):
        # directed edges between every hole to sink with weight of hole capacity
        graph[len_M+i+1][-1] = H[i][2]
    return graph, n


def mice_and_holes(M, H, d):
    # calculating distance between every elements O(M*H), where M,H are length of arrays
    len_M, len_H = len(M), len(H)
    distances = [[distance(M[i], H[j]) for j in range(len_H)]
                 for i in range(len(M))]
    graph, n = costruct_graph(M, H, distances, d,  len_M, len_H)

    max_flow = max_flow_Ford_Fulkerson(graph, n, 0, n-1)
    # returning maximal number of mice which can be save
    return max_flow


M = [(1, 1), (2, 1), (3, 0), (0, 5), (1, 4), (1, 6)]
H = [(1, 5, 2), (0, 0, 1)]
d = 2

print(mice_and_holes(M, H, d))
