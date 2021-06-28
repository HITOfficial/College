# mix of directed and undirected graph
from collections import deque

# complexity:
# -time O(V^2) -> DFS on matrix
# memory O(V^2) -> creating new graph


def crate_graph(graph,n):
    # undirected edge if weight == 0
    # directed edge if weight == 1
    return [[1 if (graph[i][j] == 1 or graph[i][j] == 0) and i != j else 0 for j in range(n)] for i in range(n)]


# DFS without time executing, but within visitations
def DFS(graph,actual,deq,visited,n):
    if visited[actual] is False:
        visited[actual] = True
        for neighbour in range(n):
            if visited[neighbour] is False and graph[actual][neighbour] == 1:
                DFS(graph,neighbour,deq,visited,n)
        deq.appendleft(actual)


def tasks(T):
    n = len(T)
    graph = crate_graph(T,n)
    visited = [False]*n
    deq = deque()
    for begin in range(n):
        DFS(graph,begin,deq,visited,n)
    return list(deq)


T = [
    [0,2,1,1],
    [1,0,1,1],
    [2,2,0,1],
    [2,2,2,0]
]

print(tasks(T))