# complexity:
# -time O(V^3)
# -memory O(V^2)
# algorithm -> can recive negative weights of edges

# float("inf") -> no edges
G = [
    [float("inf"),1,float("inf"),float("inf"),2,3,7],
    [1,float("inf"),7,float("inf"),3,float("inf"),float("inf")],
    [float("inf"),7,float("inf"),6,float("inf"),12,float("inf")],
    [float("inf"),float("inf"),6,float("inf"),2,float("inf"),float("inf")],
    [2,3,float("inf"),2,float("inf"),float("inf"),4],
    [3,float("inf"),12,float("inf"),float("inf"),float("inf"),float("inf")],
    [7,float("inf"),float("inf"),float("inf"),4,float("inf"),float("inf")]
]


def get_path(paths,begin,actual): # 2 dim paths array, recreating path from vertex begin to actual
    path = []
    element = paths[begin][actual]
    if element is not None:
        path.append(element)
        path.extend(get_path(paths,begin,element))
    return path


def Floyd_Warshall_shortest_paths(G):
    n = len(G)
    weights = [[0 if u == v else G[u][v] if G[u][v] != float("inf") else float("inf") for v in range(n)] for u in range(n)] # 0 the same vertex, edge weight, if is edge else inf
    parents = [[None if u == v else u if G[u][v] != float("inf") else None for v in range(n)] for u in range(n)]

    for vertex in range(len(G)): # vertex number
        for begin in range(len(G)):
            for end in range(len(G)):
                if weights[begin][end] > weights[begin][vertex] + weights[vertex][end]:
                    weights[begin][end] = weights[begin][vertex] + weights[vertex][end]
                    parents[begin][end] = parents[vertex][end]

    for i in range(n*n):
        path = [i%n] + get_path(parents,i//n,i%n) # recreating the path
        path.reverse()
        print(f"from: {i//n} to: {i%n} total weight: {weights[i//n][i%n]} path: {path}") 
    return ""

print(Floyd_Warshall_shortest_paths(G))
