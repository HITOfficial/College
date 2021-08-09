# minimal number of dominoes block to push to fall down all dominos
# calculating number of connected components

# complexity:
# - time O(V+E)
# - space O(V^2) -> maximal num


# creating undirected graph
def create_graph(array, n):
    graph = [list() for _ in range(n)]
    for i in range(n-1):
        _, e = array[i]
        for j in range(i+1, n):
            b, _ = array[j]
            # directed edge between dominos (while pushing i'th dominos, j'th domino will fall down too)
            if e == b:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def DFS_visit(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if visited[v] is False:
            DFS_visit(graph, visited, v)


def dominos(array):
    n = len(array)
    # to reduce complexity to create graph from (V^2 -> E), where E is number of edges, edges neeed to be sorted firstly
    array.sort()
    graph = create_graph(array, n)
    visited = [False]*n
    counter = 0
    for u in range(n):
        if visited[u] is False:
            DFS_visit(graph, visited, u)
            counter += 1
    return counter


array = [(1, 2), (1, 3), (3, 4), (3, 7), (5, 9), (10, 11), (4, 5)]

print(dominos(array))
