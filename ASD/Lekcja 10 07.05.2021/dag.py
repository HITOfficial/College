# DAG - directed acycling graph


# 1. run DFS
# 2. after processing the vertex -> put

# directed acycling graph topologic sort
g = {
    0 : [1,2,4],
    1 : [3],
    2 : [],
    3 : [4,5,6],
    4 : [],
    5 : [],
    6 : []
}


def DAG_topologic_sort(graph):
    n = len(graph)
    visited = [False] * n
    topologic_sorted = []

    def DFS(graph,visited,vertex):
        nonlocal topologic_sorted
        visited[vertex] = True # was visited
        for children in graph[vertex]:
            if visited[children] == False:
                DFS(graph, visited, children)
        topologic_sorted.insert(0,vertex)

    for vertex in range(n):
        if visited[vertex] == False: # has not children, or those were visited, then insert as first element
            DFS(graph,visited,vertex)

    return topologic_sorted

print(DAG_topologic_sort(g))