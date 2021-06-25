# DFS on list adjacency

# complexity:
# -time O(V+E)
# -memory O(V)

class Time():
    def __init__(self,time=-1):
        self.time = time


def get_path(paths,actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def DFS_recursion(graph,n,times,paths,time,actual):
    time.time += 1
    times[actual] = time.time
    for neighbour in graph[actual]:
        if times[neighbour] == float("inf"):
            paths[neighbour] = actual
            DFS_recursion(graph,n,times,paths,time,neighbour)


def DFS(graph,b,e):
    n = len(graph)
    times = [float("inf")]*n
    paths = [None] * n
    time = Time()
    DFS_recursion(graph,n,times,paths,time,b)
    return times[e], list(reversed(get_path(paths,e)))


graph = [
    [1,4,5,6],
    [0,2,4],
    [1,3,5],
    [2,4],
    [0,1,3,6],
    [0,2],
    [0,4]
]

print(DFS(graph,0,6))