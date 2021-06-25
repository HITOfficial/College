from queue import PriorityQueue

# complexity:
# -time O(V^2)
# -memory O(V)

def get_path(paths,actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def best_vertex(n,distances,visited):
    vertex,distance = 0, float("inf") 
    for i in range(n):
        if visited[i] is False and distances[i] < distance:
            vertex, distance = i, distances[i]
    return vertex


def Dijkstra(graph,u,v):
    n = len(graph)
    distances = [float("inf")]*n
    distances[u] = 0
    visited = [False]*n
    paths  = [None]*n
    
    for _ in range(n):
        vertex = best_vertex(n,distances,visited)
        visited[vertex] = True
        for neighbour in range(n):
            # not visited vertex, to whose is lower distance using actual visited vertex, and edge between
            if visited[neighbour] is False and graph[vertex][neighbour] != 0 and distances[neighbour] > distances[vertex] + graph[vertex][neighbour]:
                paths[neighbour] = vertex
                distances[neighbour] = distances[vertex] + graph[vertex][neighbour]
    return distances[v], list(reversed(get_path(paths,v)))


graph = [
    [0,1,0,0,2,3,7],
    [1,0,7,0,3,0,0],
    [0,7,0,6,0,12,0],
    [0,0,6,0,2,0,0],
    [2,3,0,2,0,0,4],
    [3,0,12,0,0,0,0],
    [7,0,0,0,4,0,0]
]

print(Dijkstra(graph,0,3))