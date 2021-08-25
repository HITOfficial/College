# Dijkstra min distance using vertex multiplication, and also, liear table

# complexity:
# - time O(N*M*N*M)
# - space O(N*M)


def best_vertex(distances, visited):
    idx, dist = 0, float("inf")
    for i, d in enumerate(distances):
        if d < dist and visited[i] is False:
            idx, d = i, d
    return idx


def get_path(path, m, v):
    p = []
    if v is not None:
        p.append(v//m)
        p.extend(get_path(path, m, path[v]))
    return p


def get_into(G, P, d, a, b):
    n = len(G)
    m = d+1
    t = n*m
    # O(n*m), where n is node, m remaining fuel into vertex
    stations = [False]*n
    # marking up stations to have O(1) acces if this vertex has station
    for s in P:
        stations[s] = True
    visited, parent = [False]*t, [None]*t
    distances = [float("inf")]*t
    distances[a] = 0
    for _ in range(t):
        idx = best_vertex(distances, visited)
        visited[idx] = True
        fuel = idx % n
        if stations[idx % n] == True:
            # in this station is fuel to take
            fuel = d
        for i in range(t):
            # checking if new vertex wasn't visited
            w = G[idx // m][i // m]
            # is edge between condition
            if visited[i] is False and w != -1 and w <= fuel:
                fuel_remaining = (i % n)
                # checking if can update graph to have this at least remaining fuel
                if fuel >= fuel_remaining + w:
                    # never came into there
                    if distances[i] > distances[idx] + w:
                        distances[i] = distances[idx] + w
                        parent[i] = idx

    idx, lowest = 0, float("inf")
    for i in range(b*m, (b+1)*m):
        if distances[i] < lowest:
            idx = i
            lowest = distances[i]
    # cannot get into destination
    if lowest == float("inf"):
        return None
    # returning shortest distance, and path
    return distances[idx], list(reversed(get_path(parent, m, idx)))


G = [
    [-1, 6, -1, 5, 2],
    [-1, -1, 1, 2, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, 4, -1, -1],
    [-1, -1, 8, -1, -1]
]
P = [0, 1, 3]

print(get_into(G, P, 6, 0, 2))
print(get_into(G, P, 5, 4, 1))
