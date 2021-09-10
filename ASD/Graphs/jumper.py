# Given is a weighted unguided G-plot and two-mile shoes - a special way of moving after the chart.
# Two-mile boots prevent you from negotiating broken paths from the two edges of the graph yes
# Hello, that is now the continuation of the edge of equal order that brings both edges out of the path.
# However, there is a limiting factor - every sentence of two-mile shoes belongs
# each edge price appears on the chart as usual. The matrix G contains the edge weight
# in an edge chart with edge numbers, 0 indicates the edge. Please describe, implement and estimate the complexity
# of the shortest path search algorithm in the graph on the use of two-mile shoes. The solution should be implemented as a function:
from queue import PriorityQueue

# complexity:
# - time O(VlogV) -> 2Vlog(V^2) -> tree structure of graph with double edges connections
# - space O(V) -> 2V


def get_path(paths, actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths, paths[actual]))
    return path


def jumper(graph, b, e):
    n = len(graph)
    distances = [[float("inf")]*2 for _ in range(n)]
    distances[b][0], distances[b][1] = 0, 0
    paths = [[None]*2 for _ in range(n)]
    # 1 -> single jump. 2 -> double jump
    # tuples: (edge weight, from, to, jump)
    p_queue = PriorityQueue()
    for v, d in graph[b]:
        # single jump
        p_queue.put((d, b, v, 1))
        for k, w in graph[v]:
            # double jump
            p_queue.put((max(d, w), b, k, 2))

    while not p_queue.empty():
        d, u, v, j = p_queue.get()
        # checking if is posible to relax edge
        # dobule jump relaxation
        if j == 2:
            if distances[v][1] > distances[u][0] + d:
                distances[v][1] = distances[u][0] + d
                paths[v][1] = u, 1
            # single jumps only avaiable
            for k, w in graph[v]:
                if k != v:
                    p_queue.put((w, v, k, 1))
        else:
            # single jump, two options:
            if distances[v][0] > distances[u][0] + d:
                distances[v][0] = distances[u][0] + d
                paths[v][0] = u, 1
                # single jump
                for k, w in graph[v]:
                    if k != v:
                        p_queue.put((w, v, k, 1))
                    # double jump
                    for g, s in graph[k]:
                        p_queue.put((max(w, s), v, g, 2))
    return min(distances[e])


graph = [
    [(1, 1)],
    [(0, 1), (2, 1)],
    [(1, 1), (3, 7)],
    [(2, 7), (4, 8)],
    [(3, 8)],
]

print(jumper(graph, 0, 4))
