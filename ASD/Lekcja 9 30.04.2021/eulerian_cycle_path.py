# Euler cycle path in graph

# n^2 euler path on matrix

# I assume that has an euler path


g = [
    [0,1,0,0,0,1,0],
    [1,0,1,0,0,1,1],
    [0,1,0,1,1,0,1],
    [0,0,1,0,1,0,0],
    [0,0,1,1,0,1,1],
    [1,1,0,0,1,0,1],
    [0,1,1,0,1,1,0]
]

def eulerian_cycle_edges(graph): # has only Euler cycle, only if every vertex dim is even
    edges = 0
    for i in range(len(graph)):
        vertex = 0
        for j in range(len(graph)):
            if graph[i][j] == 1:
                vertex += 1
                edges += 1
        if vertex %2 == 1:
            return False, edges
    return True, edges


def eulerian_cycle_path(graph):
    can_create_path, edges = eulerian_cycle_edges(graph)
    if  can_create_path == False:
        return False
    n = len(graph)
    visited = [[False]*n for _ in range(n)]
    path = []
    path.append(0)
    # memorizing to which vertex should, not came in
    def DFS_search(graph,visited,vertex,skip= float("inf")): # in skip will memorize, which, i should to not come in 
        nonlocal path, edges
        flag = False
        for neighbour in range(len(graph)):
            if visited[vertex][neighbour] == False and skip != neighbour and graph[vertex][neighbour] == 1:
                flag = True # found new elemenet in path
                visited[vertex][neighbour] = True
                visited[neighbour][vertex] = True
                path.append(neighbour)
                DFS_search(graph, visited, neighbour,float("inf"))
                break
        if vertex == path[0] and len(path) >= edges//2:
            return # It means, that algorithm found corectly path
        if flag == False: # doesn't found now element in path
            skip = path.pop()
            vertex = path[-1] # last element will be where I'll search for corectly path
            visited[vertex][skip] = False
            visited[skip][vertex] = False
            DFS_search(graph, visited, vertex, skip)

    DFS_search(graph,visited,0)
    return path


print(eulerian_cycle_path(g))