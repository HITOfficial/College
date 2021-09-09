# graph representation: matrix adjacency, works on direncted and undirected graph

# complexity:
# - time O(N*N!), N is a number of vertices
# - space O(N*P) , where P is total number of Hamiltonian paths

def remove_duplicates(paths, n):
    duplicated = [False]*n
    for i in range(n-1):
        if not duplicated[i]:
            p_reversed = list(reversed(paths[i]))
            for j in range(i+1, n):
                if p_reversed == paths[j]:
                    duplicated[j] = True
    return [path for i, path in enumerate(paths) if not duplicated[i]]


def conver_to_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(conver_to_path(path, path[u]))
    return p


def rec_DFS_paths(graph, paths, parent, visited, n, k, u, e):
    # last vertex
    for v in range(n):
        # has edge
        if graph[u][v] != 0 and visited[v] is False:
            parent[v], visited[v] = u, True
            # isnt connection to last edge
            if k < n-2 and v != e:
                rec_DFS_paths(graph, paths, parent, visited, n, k+1, v, e)
            # connection to last edge
            elif k == n-2 and v == e:
                paths.append(list(reversed(conver_to_path(parent, e))))
            # removing dynamic memorizing processing
            parent[v], visited[v] = None, False


def Hamiltonian_paths(graph, b):
    n = len(graph)
    paths = []
    for v in range(n):
        w = graph[b][v]
        if w != 0:
            parent, visited = [None]*n, [False]*n
            visited[b] = True
            # removing connections
            graph[b][v], graph[v][b] = 0, 0
            rec_DFS_paths(graph, paths, parent, visited, n, 0, b, v)
            # adding again connections
            graph[b][v], graph[v][b] = w, w
    # connections to beggining
    for path in paths:
        path.append(b)
    return remove_duplicates(paths, len(paths))


graph = [
    [0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0],
]

print(Hamiltonian_paths(graph, 3))
