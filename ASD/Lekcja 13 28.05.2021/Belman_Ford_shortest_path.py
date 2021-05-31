# complexity: O(V*E)
# Algorithm will detect negative cycles


G = [
    [-1,1,-1,-1,2,3,7],
    [1,-1,7,-1,3,-1,-1],
    [-1,7,-1,6,-1,12,-1],
    [-1,-1,6,-1,2,-1,-1],
    [2,3,-1,2,-1,-1,4],
    [3,-1,12,-1,-1,-1,-1],
    [7,-1,-1,-1,4,-1,-1]
]


def relax(weights,u,v,w): # weights to get to every vertex, edge ends, weight of vertex
    if weights[v] > weights[u] + w:
        weights[v] = weights[u] + w
        return True
    else:
        return False


def matrix_to_edges(G):
    return [(u,v,G[u][v]) for u in range(len(G)) for v in range(len(G)) if G[u][v] != -1]


def get_path(paths,u):
    path = []
    if paths[u] is not None:
        path.append(paths[u])
        path.extend(get_path(paths,paths[u]))
    return path


def Belman_Ford_shortest_path(G,b,e): # graph begining vertex, last edge
    n = len(G)
    weights = [float("inf")] * n
    parents = [None] * n
    weights[b] = 0
    E = matrix_to_edges(G)
    for _ in range(n-1):
        for u,v,w in E:
            if relax(weights,u,v,w):
                parents[v] = u

    path = get_path(parents,e)
    path = [e] + path
    path.reverse()

    return weights[e],path

    
print(Belman_Ford_shortest_path(G,5,3))