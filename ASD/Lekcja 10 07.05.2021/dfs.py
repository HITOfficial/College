def DFS(graph,visited,vertex,time=0):
    visited[vertex] = True
    for children in graph[vertex]:
        if visited[children] == False:
            time = DFS(graph, visited, children, time+1)
    return time