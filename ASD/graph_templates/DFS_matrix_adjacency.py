# DFS on matrix adjacency

# complexity:
# -time O(V^2)
# -memory O(V)

# to do not declare non local variable, im using class obj.
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
    for neighbour in range(n):
        if graph[actual][neighbour] != 0 and times[neighbour] == float("inf"):
            paths[neighbour] = actual
            DFS_recursion(graph,n,times,paths,time,neighbour)


def DFS(graph,b,e):
    n = len(graph)
    times = [float("inf")]*n
    paths = [None] * n
    time = Time()
    # DFS alg.
    DFS_recursion(graph,n,times,paths,time,b)
    return times[e], list(reversed(get_path(paths,e)))


graph = [
    [0,1,0,0,1,1,1],
    [1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0],
    [0,0,1,0,1,0,0],
    [1,1,0,1,0,0,1],
    [1,0,1,0,0,0,0],
    [1,0,0,0,1,0,0]
]

print(DFS(graph,0,6))