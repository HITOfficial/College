# graph representation: unweighted, list adjacency, works on direncted and undirected graph

# complexity:
# - time O(N!)
# - space O(N*P) , where P is total number of Hamiltonian paths


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


def Hamiltonian_paths(graph, b, e):
    n = len(graph)
    paths, parent, visited = [], [None]*n, [False]*n
    visited[b] = True
    rec_DFS_paths(graph, paths, parent, visited, n, 0, b, e)
    return paths


graph = [
    [1],
    [0, 2, 8],
    [1, 3, 9],
    [2, 10],
    [5],
    [4, 6, 10],
    [5, 7, 9, 10],
    [6, 8],
    [7, 9],
    [2, 6, 8, 10],
    [3, 5, 9],
]


print(Hamiltonian_paths(graph, 0, 4))
