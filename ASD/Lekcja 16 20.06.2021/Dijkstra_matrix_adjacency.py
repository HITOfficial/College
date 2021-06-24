# Dijkstra on matrix adjacency:

# complexity:
# -time O(V^2)
# -memory O(V)

# inspiration https://algorithms.tutorialhorizon.com/djkstras-shortest-path-algorithm-adjacency-matrix-java-code/





def get_path(paths,actual):
    path = []
    if actual != None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def minimum_vertex(n,distances,visited):
    vertex, d = -1, float("inf")
    for i in range(n):
        if visited[i] is False and d > distances[i]:
            vertex,d = i, distances[i]
    return vertex


# O(V^2)
def Dijkstra(graph,u,v):
    n = len(graph)
    distances =[float("inf")]*n
    distances[u] = 0
    paths = [None]*n
    visited =[False]*n

    for _ in range(n):
        b = minimum_vertex(n,distances,visited)
        visited[b] = True
        for e in range(n):
            # checking if need to update edge
            if graph[b][e] != 0 and visited[e] is False:
                # relaxing edge
                d = distances[b] + graph[b][e]
                if distances[e] > d:
                    paths[e] = b
                    distances[e] =  d
    path = list(reversed(get_path(paths,v)))
    return distances[v], path


graph = [
    [0,1,0,0,2,3,7],
    [1,0,7,0,3,0,0],
    [0,7,0,6,0,12,0],
    [0,0,6,0,2,0,0],
    [2,3,0,2,0,0,4],
    [3,0,12,0,0,0,0],
    [7,0,0,0,4,0,0]
]

print(Dijkstra(graph,0,5))