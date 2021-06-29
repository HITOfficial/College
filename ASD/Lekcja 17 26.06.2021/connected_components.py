# finding connected components in undirected graph, using DFS algorithm V-times

# complexity: 
# -time O(V^3)
# -memory O(V)


graph = [
    [0,1,1,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0,0]
]


def DFS(graph,visited,actual,n):
    visited[actual] = True
    array = [actual]
    for i in range(n):
        # checking if has connection and vertex wasn't visited
        if graph[actual][i] == 1 and visited[i] is False:
            array.extend(DFS(graph,visited,i,n))
    return array


def connected_components(graph):
    n = len(graph)
    components = []
    visited =[False] *n
    for i in range(n):
        if visited[i] is False:
            components.append(DFS(graph,visited,i,n))
    return len(components),components


print(connected_components(graph))