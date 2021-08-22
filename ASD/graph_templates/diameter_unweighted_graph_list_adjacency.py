# Diameter in tree
# representation: undirected tree (acyclic connected graph) on list adjacency

from queue import Queue

# complexity:
# - time O(V+E)
# - space O(V)


def BFS_times(graph, n, b=0):
    time = 1
    # if dist == float("inf") -> vertex wasn't processed
    times = [float("inf")]*n
    path = [None]*n
    queue = Queue()
    queue.put(b)
    while not queue.empty():
        time += 1
        next_queue = Queue()
        while not queue.empty():
            u = queue.get()
            for v in graph[u]:
                if times[v] == float("inf"):
                    times[v] = time
                    if v != b:
                        path[v] = u
                    next_queue.put(v)
        queue = next_queue
    return times, path


def get_max(times):
    idx, time = 0, 0
    for i, t in enumerate(times):
        if t > time:
            time = t
            idx = i
    return idx


def get_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u]))
    return p


# returning diameter length, and path one of the diameters
def diameter_BFS(graph):
    n = len(graph)
    # running 1st time BFS
    times, _ = BFS_times(graph, n)
    left_end = get_max(times)
    # running second time BFS
    times, path = BFS_times(graph, n, left_end)
    right_end = get_max(times)
    return times[right_end], get_path(path, right_end)


graph = [
    [2],
    [2],
    [0, 1, 3],
    [2, 4],
    [3, 5, 6],
    [4],
    [4]
]
print(diameter_BFS(graph))
