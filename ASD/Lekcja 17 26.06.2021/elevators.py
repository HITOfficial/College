# Exercise in PL lang.
# Wieżowiec ma n pięter i n wind, nie ma natomiast schodów. Każda winda posiada listę pięter, do których dojeżdża i prędkość w sekundach na piętro.
# Jesteśmy na piętrze b, chcemy się dostać na piętro e. Ile minimalnie sekund musimy spędzić w windach, aby tam dotrzeć?

# complexity:
# -time O(V^2)
# -memory O(V^2)

# Dijkstra min distance on directed matrix adjacency O(V^2)


def best_vertex(visited,distances,n):
    v,w = 0, float("inf")
    for i in range(n):
        if visited[i] is False and distances[i] < w:
            v,w = i, distances[i]
    return v


# creating weighted graph
def construct_graph(elevator,speed,n):
    return [[(elevator[i][j] * speed[i])*abs(i-j) if elevator[i][j] != 0 else 0 for j in range(n)] for i in range(n)]


def elevators(elevator,speed,b,e):
    n = len(elevator)
    graph = construct_graph(elevator,speed,n)
    
    # Dijkstra shortest path alg.
    visited = [False]*n
    distances = [float("inf")]*n
    distances[b] = 0
    for _ in range(n):
        vertex = best_vertex(visited,distances,n)
        visited[vertex] = True
        for i in range(n):
            # relaxing edges
            if visited[i] is False and graph[vertex][i] != 0 and distances[i] > distances[vertex] + graph[vertex][i]:
                distances[i] = distances[vertex] + graph[vertex][i]
    return distances[e]


graph = [
    [0,1,1,1,1,1,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,1,0,0],
    [1,0,0,1,0,0,0,0,0,1,0],
    [1,0,1,0,0,0,1,0,1,0,0],
    [1,1,1,0,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,1,0,1],
    [0,0,0,0,1,0,1,0,0,1,0]
]
elevator_speed = [2,1,4,8,19,8,5,2,16,7,9]

print(elevators(graph,elevator_speed,0,10))
