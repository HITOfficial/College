# Each undirected, consistent and acyclic graph G = (V, E) can be treated as a tree. The root of this tree can be any vertex v ∈ V. Write a best root (L) function that
# takes an undirected, connected and acyclic graph G (represented as a neighborhood list) and
# chooses such its top, by the height of the rooted at this vertex, which would be cultivating it. If several vertices have the correct conditions, a function can have any of the
# niche. We define a tree tree as an edge solution from the root to the farthest leaf. Justification
# Correctness of the proposed algorithm and estimate its computational complexity.

from queue import Queue

# complexity:
# - time O(V+E) -> BFS on list adjacency complexity
# - space O(V)


def get_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u]))
    return p


def BFS_distances(graph, n, b=0):
    queue = Queue()
    distance = [float("inf")]*n
    parent = [None]*n
    queue.put(b)
    distance[b] = 0
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if distance[v] > distance[u] + 1:
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)
    return distance, parent


def best_root(L):
    n = len(L)
    # running BFS to find diameter in undirected connected acyclic tree
    b = max(enumerate(BFS_distances(L, n)[0]), key=lambda x: x[1])[0]
    distance, parent = BFS_distances(L, n, b)
    # index of ending in diameter
    e = max(enumerate(distance), key=lambda x: x[1])[0]
    path = get_path(parent, e)
    # middle vertex of diameter from reconstructing path between b and e vertices
    return path[len(path)//2]


L = [
    [2],
    [2],
    [0, 1, 3],
    [2, 4],
    [3, 5, 6],
    [4],
    [4]
]

print(best_root(L))
