from collections import deque

# Topological sort on DAG matrix adjacency graph

# complexity:
# -time O(V^2)
# -memory O(V)


def topological_DFS(graph,n,topological_sorted,visited,actual):
    for neighbour in range(n):
        if graph[actual][neighbour] != 0 and visited[neighbour] is False:
            visited[neighbour] = True
            topological_DFS(graph,n,topological_sorted,visited,neighbour)
    # working on deuque to have O(1) insert vertex
    topological_sorted.appendleft(actual)


def topological_sort(graph,b=0):
    n = len(graph)
    topological_sorted = deque()
    visited = [False]*n
    topological_DFS(graph,n,topological_sorted,visited,b)
    return list(topological_sorted)


graph = [
    [0,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

print(topological_sort(graph))
