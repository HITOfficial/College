# Please implement the count shortest paths (G, s, t) function that will calculate how many different shortest
# of paths leads in the graph M G from vertex s to vertex t. Two paths are different if
# they are approaching the edge. Graph G is represented in a matrix (G [i] [j] == True if there is an edge
# G [i][j] == False in other case]).

# alg. a bit modyfied BFS on matrix adjacency, using time to memorize executing time of every vertex.
# If are more than one shortest path, updating number of shortest paths by uncluding shortest path, of equal executing time

# complexity:
# - time O(V^2)
# - space O(V)


from queue import Queue


def count_shortest_paths(G, s, t):
    n = len(G)
    # shortest path of begining: 1
    shortest_paths = [0]*n
    shortest_paths[s] = 1
    times = [float("inf")] * n
    times[s] = 0
    time = 0
    # adding only once every verex into queue to execute using BFS waves
    shortest_paths[s] = 1
    # BFS algorithm, to find shortest paths, without time to execute
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        next_queue = Queue()
        time += 1
        while not queue.empty():
            idx = queue.get()
            for v in range(n):
                if G[idx][v]:
                    # has equal executing time, so V vertex is already in queue
                    if times[v] == time:
                        shortest_paths[v] += shortest_paths[idx]
                        times[v] = time
                    # visiting vertex for first time
                    elif times[v] == float("inf"):
                        next_queue.put(v)
                        shortest_paths[v] += shortest_paths[idx]
                        times[v] = time
        queue = next_queue
    return shortest_paths[t]


G = [
    [False, True, True, False, True],
    [False, False, True, True, False],
    [False, False, False, True, False],
    [False, False, False, False, False],
    [False, False, False, True, False]
]

print(count_shortest_paths(G, 0, 3))
