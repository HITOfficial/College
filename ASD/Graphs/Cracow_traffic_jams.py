# There are traffic jams in Krakow during rush hours, so you limit yourself to time rather than the actual distance between points. We have a map of Krakow,
# between street intersections and times are marked. In Krakow (like everyone else;)) there are one-way and two-way streets.
# The drivers were looking for an app that browsed the way you browse the way you want it to be as short as possible, the kind of search you want to be, and the shortest way by angle.
# We are to process Q. at junctionA, junctionB) and for each of them with a pair (time, distance) of the best path. All queries follow the same graph.
# What each solution gives your complexity class on the page level?
# Q = O (1), E = O (V) -> Dijkstra O(ElogV)
# Q = O (1), E = O (V ^ 2) -> Dijkstra O(V^2) -> matrix adjacency
# Q = O (V), E = O (V) -> Dijkstra O(V*ElogV)
# Q = O (V), E = O (V ^ 2) -> O(V^3) Floyd Warshall/ V times Dijkstra on matrix adjacency (without Priority Queue)

# space complexity: O(V^2)

def Cracow_traffic_jams(graph, graph_times, Q):
    # Floyd Warshall alg.
    n = len(graph)
    distances = [[0 if u == v else float(
        "inf") if graph[u][v] == 0 else graph[u][v] for v in range(n)] for u in range(n)]
    times = [[0 if u == v else float(
        "inf") if graph_times[u][v] == 0 else graph_times[u][v] for v in range(n)] for u in range(n)]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                dist = distances[u][k] + distances[k][v]
                time = times[u][k] + times[k][v]
                if (distances[u][v] > dist or (distances[u][v] == dist and times[u][v] > time)):
                    distances[u][v] = dist
                    times[u][v] = time
    for u, v in Q:
        print((u, v), "dist:", distances[u][v], "times:",
              times[u][v])


graph = [
    [0, 3, 0, 0, 2, 3, 7],
    [3, 0, 7, 0, 3, 0, 0],
    [0, 7, 0, 6, 0, 12, 0],
    [0, 0, 6, 0, 2, 0, 0],
    [2, 3, 0, 2, 0, 0, 4],
    [3, 0, 12, 0, 0, 0, 0],
    [7, 0, 0, 0, 4, 0, 0]
]

graph_times = [
    [0, 9, 0, 0, 2, 3, 70],
    [9, 0, 7, 0, 3, 0, 0],
    [0, 7, 0, 6, 0, 12, 0],
    [0, 0, 6, 0, 2, 0, 0],
    [2, 3, 0, 2, 0, 0, 13],
    [3, 0, 12, 0, 0, 0, 0],
    [70, 0, 0, 0, 13, 0, 0]
]

Q = [(0, 2), (6, 0)]
print(Cracow_traffic_jams(graph, graph_times, Q))
