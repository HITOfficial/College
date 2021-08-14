# Hierholzers algorithm to find Eulerian path
# graph representation: directed graph on list adjacency

# inspiration: https://www.youtube.com/watch?v=8MpoO2zA2l4

# graph has Eulerian path if in at most two vertices difference between in/out eges is equal 1

from collections import deque
# using deque as a stack to memorize path to append left in O(1)

# complexity:
# - time O(E)
# - space O(E) / O(V) -> O(V), memorizing number of in/ out edges for every vertex O(E) memorizing path


def has_Eulerian_path(graph, incoming, outcoming, n):
    # memorizning number of in/out edges
    for u in range(n):
        for v in graph[u]:
            outcoming[u] += 1
            incoming[v] += 1
    b, e, flag_in, flag_out = 0, 0, False, False
    for i in range(n):
        in_out_diff = incoming[i] - outcoming[i]
        if abs(in_out_diff) > 1:
            return None, None, False
        if in_out_diff == 1 and flag_in is False:
            e = i
            flag_in = True
        elif in_out_diff == -1 and flag_out is False:
            b = i
            flag_out = True
        # triple conjunction
        elif abs(in_out_diff) >= 1 and flag_in and flag_in:
            return None, None, False

    # this graph has Eulerian path
    return b, e, True


def DFS_visit_edges(graph, outcoming, path, u):
    while outcoming[u] > 0:
        v = graph[u].pop()
        outcoming[u] -= 1
        DFS_visit_edges(graph, outcoming, path, v)
    path.appendleft(u)


def Eulerian_path(graph):
    n = len(graph)
    incoming, outcoming = [0]*n, [0]*n
    b, e, has_path = has_Eulerian_path(graph, incoming, outcoming, n)
    # condition if graph has eulerian path
    if not has_path:
        return False
    path = deque()
    DFS_visit_edges(graph, outcoming, path, b)
    return list(path)


graph = [
    [1],
    [2],
    [3],
    [4, 11],
    [5],
    [2, 10],
    [5, 9],
    [6, 9],
    [7],
    [8, 10],
    [6, 7],
    [12],
    [3],
]

print(Eulerian_path(graph))
