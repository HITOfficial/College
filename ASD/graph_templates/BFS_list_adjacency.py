from queue import Queue

# BFS on list adjacency

# complexity:
# -time O(V+E)
# -memory O(V)


def get_path(paths,actual):
    path = []
    if actual is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


def BFS(graph,b,e):
    n = len(graph)
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
            for neighbour in graph[actual]:
                if times[neighbour] == float("inf"):
                    times[neighbour] = time
                    paths[neighbour] = actual
                    next_queue.put(neighbour)
        queue = next_queue
    # returning executing time and path
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

print(BFS(graph,0,2))