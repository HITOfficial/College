# In the world is an Island. The cost of the trip on the islands
# to the other island is 8B, the ferry costs 5B, you have to pay for crossing the bridge
# fee 1B. We are looking for a route from To island B, which means islands in the islands,
# transport to another and minimizes the cost of the trip.
# Given is the table G, the designation of the connection between the islands. The value of 0 in the matrix
# means no direct connection. Please implement the island function (G, A, B)
# Triggering island travel costs to an island
# has nothing to do, the revision is nothing.


# complexity:
# - time O(V^2) -> Dijkstra on matrix adjacency with 3 types of transport -> 3*V^2
# - space O(V)

def get_path(path, u, t):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u][t][0], path[u][t][1]))
    return p


def best_vertex(visited, distances, n):
    # vertex, transport type, lowest distance
    u, t, w = 0, 0, float("inf")
    for v in range(n):
        # 3 types of transport
        for k in range(3):
            if visited[v][k] is False and distances[v][k] < w:
                u, t, w = v, k, distances[v][k]
    # returning vertex with type of transport
    return u, t


def islands(G, A, B):
    n = len(G)
    visited = [[False]*3 for _ in range(n)]
    distances = [[float("inf")]*3 for _ in range(n)]
    parent = [[(None, None)]*3 for _ in range(n)]
    # distance to get into begining distance
    distances[A] = [0, 0, 0]
    # every next stage of travel with another transport type
    for _ in range(n):
        u, t = best_vertex(visited, distances, n)
        visited[u][t] = True
        for v in range(n):
            for k in range(3):
                # cannot use same transport type
                if t != k:
                    if G[u][v] != 0 and distances[v][k] > distances[u][t] + G[u][v]:
                        distances[v][k] = distances[u][t] + G[u][v]
                        parent[v][k] = u, t
    t, d = 0, float("inf")
    # finding shortest path after getting
    for k in range(3):
        if distances[B][k] < d:
            d = distances[B][k]
            t = k
    # cannot get into destination
    if d == float("inf"):
        return
    else:
        # returning total minimal distance, and path
        return d, list(reversed(get_path(parent, B, t)))


G = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]
]

print(islands(G, 5, 2))
print(islands(G, 5, 0))
