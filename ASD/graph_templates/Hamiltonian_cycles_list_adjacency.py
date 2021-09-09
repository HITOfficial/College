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
    for v in graph[u]:
        # wasn't visited
        if visited[v] is False:
            parent[v], visited[v] = u, True
            # isnt connection to last vertex
            if k < n-2 and v != e:
                rec_DFS_paths(graph, paths, parent, visited, n, k+1, v, e)
            # connection to last vertex
            elif k == n-2 and v == e:
                paths.append(list(reversed(conver_to_path(parent, e))))
            # removing dynamic memorizing processing
            parent[v], visited[v] = None, False


def Hamiltonian_paths(graph, b):
    n = len(graph)
    paths = []
    for v in graph[b]:
        parent, visited = [None]*n, [False]*n
        visited[b] = True
        in_b_idx = graph[b].index(v)
        in_v_idx = graph[v].index(b)
        # removing connections
        graph[b].pop(in_b_idx), graph[v].pop(in_v_idx)
        rec_DFS_paths(graph, paths, parent, visited, n, 0, b, v)
        # adding again connections
        graph[b].insert(in_b_idx, v), graph[v].insert(in_v_idx, b)
    # connections to beggining
    for path in paths:
        path.append(b)
    # removing duplicates from circuits
    return remove_duplicates(paths, len(paths))


graph = [
    [1, 4, 5],
    [0, 2, 3, 4],
    [1, 3],
    [1, 2, 4],
    [0, 1, 3, 5],
    [0, 4],
]

print(Hamiltonian_paths(graph, 3))
