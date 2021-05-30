# Transitive closure path in directed graph

# Exercise in PL lang:
# Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować algorytm, który oblicza domknięcie przechodnie grafu G
# (domknięcie przechodnie grafu G to takie graf H, że w H mamy krawędź z u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).


# Using modyfied DFS to find the directed path in graph from vertex u->v
# Only once move every vertex

# Complexity O(V*E)


class Time():
    def __init__(self,time):
        self.time = time
        

def DFS(G,time,visited,path,u): # Graph, time to DFS, mark up visited vertex, path to transitive closure, actual vertex
    time.time += 1
    visited[u] =  True
    path[time.time] = u
    for children in range(len(G)):
        if G[u][children] == 1 and visited[children] is False:
            if DFS(G,time,visited,path,children): # found path
                return True
    if time.time < len(G)-1: # using this edge can not recive path to transitive closure
        path[time.time] = None
        time.time -= 1
        visited[u] = False
        return False
    return True


def transitive_closure(G,u,v): # Graph begin, end
    n = len(G)
    visited = [False] * n  # to mark up visited vertexes
    time = Time(-1)
    path = [None] * n
    if DFS(G,time,visited,path,u): # found path
        return path
    else:
        return False


G = [
    [0,1,0,1,0,0],
    [0,0,0,0,1,1],
    [0,1,0,0,0,0],
    [0,1,1,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,1,0],
    ]

print(transitive_closure(G,0,4))

