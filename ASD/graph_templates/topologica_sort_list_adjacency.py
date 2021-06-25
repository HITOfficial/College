from collections import deque

# Topological sort on DAG matrix adjacency graph

# complexity:
# -time O(V^2)
# -memory O(V)


def topological_DFS(graph,n,topological_sorted,visited,actual):
    for neighbour in graph[actual]:
        if visited[neighbour] is False:
            visited[neighbour] = True
            topological_DFS(graph,n,topological_sorted,visited,neighbour)
    topological_sorted.appendleft(actual)


def topological_sort(graph,b=0):
    n = len(graph)
    topological_sorted = deque()
    visited = [False]*n
    topological_DFS(graph,n,topological_sorted,visited,b)
    return list(topological_sorted)


graph = [
    [1,2,3,4],
    [],
    [],
    [4,5,6],
    [1],
    [],
    [],
]

print(topological_sort(graph))
