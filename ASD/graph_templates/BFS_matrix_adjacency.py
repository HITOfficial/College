from queue import Queue

# BFS on matrix adjacency

# complexity:
# -time O(V^2)
# -memory O(V)

def get_path(paths,actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def BFS(graph,b,e):
    n = len(graph)
    # to do not create extra array with visited fields, Im using times array to memorize executing time and checking if vertex was visited
    times = [float("inf")]*n
    time = 1
    times[b] = time
    paths = [None]*n
    queue = Queue()
    queue.put(b)
    while not queue.empty():
        time += 1
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for i in range(n):
                if graph[actual][i] != 0 and times[i] == float("inf"):
                    times[i] = time
                    paths[i] = actual
                    next_queue.put(i)
        queue = next_queue
    # returning executing time and path
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

print(BFS(graph,0,2))