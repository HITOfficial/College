# In the internet cafe there is K and Application on a CD. There can be a maximum of one application on each person.
# Apps have access to accounts that may be running, have problems accessing hardware.
# You are the owner of an interface and you know how many customers (possibly zero) will want to use your application tomorrow.
# We assume that every customer uses a computer for the whole day.
# What application application on the site to each of the users, users can users who have followed up with who they want?
# If such an assignment does not exist, the algorithm should do so.
from queue import Queue

# complexity of Edmonds Karp alg on matrix adjacency


# max flow alg directed graph on matrix adjacency
def BFS_find_flow(network, residual_network, n, source, sink):
    path = [None]*n
    flow = [float("inf")]*n
    queue = Queue()
    queue.put(source)
    while not queue.empty():
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for neighbour in range(n):
                if flow[neighbour] == float("inf"):
                    if network[actual][neighbour] != 0:
                        flow[neighbour] = min(
                            network[actual][neighbour], flow[actual])
                        path[neighbour] = actual
                        next_queue.put(neighbour)
                    elif residual_network[actual][neighbour] != 0:
                        flow[neighbour] = min(
                            residual_network[actual][neighbour], flow[actual])
                        path[neighbour] = actual
                        next_queue.put(neighbour)
        queue = next_queue
    return flow[sink], path


def max_flow_Edmonds_Karp(graph, n, source, sink):
    max_flow = 0
    residual_network = [[0]*n for _ in range(n)]
    while True:
        new_flow, path = BFS_find_flow(
            graph, residual_network, n, source, sink)
        if new_flow == float("inf"):
            break
        actual = sink
        while actual != source:
            graph[path[actual]][actual] -= new_flow
            residual_network[actual][path[actual]] += new_flow
            actual = path[actual]
        max_flow += new_flow
    return max_flow


def construct_graph(n, k, A, apps):
    graph = [[0]*(n+k+2) for _ in range(n+k+2)]
    # connections from source to apps
    for idx, w in enumerate(apps):
        graph[n+k][idx] = w
    # connections from apps to PC's
    for u in range(n):
        for v in A[u]:
            graph[u][n+v] = 1
    # connections from every app to sink
    for u in range(k):
        graph[n+u][n+k+1] = 1
    return graph


def internet_cafe(A, K, apps_to_install):
    k = len(K)
    n = len(A)
    graph = construct_graph(n, k, A, apps_to_install)
    n = n+k+2
    if max_flow_Edmonds_Karp(graph, n, n-2, n-1) == sum(apps_to_install):
        return True
    else:
        return False


A = [[0, 2, 5], [2, 3, 5], [4], [1, 3]]
apps_to_install = [2, 2, 0, 1]
K = [0, 1, 2, 3, 4, 5]

print(internet_cafe(A, K, apps_to_install))
