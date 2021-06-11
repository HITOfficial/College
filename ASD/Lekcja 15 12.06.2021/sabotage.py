# Finding max flow in flow network, and edges to remove to get min cut
# to run this, need to see Edmonds_Karp_max_flow.py from same folder 
from Edmonds_Karp_max_flow import *
from queue import Queue

# Exercise in PL lang.
# W pewnym kraju trwa wojna domowa. W ramach sabotażu rebelianci chcą uniemożliwić komunikację telegraficzną z miasta A do B. Otrzymujemy listę miast i linii telegraficznych między nimi.
# Linie telegraficzne są skierowane. Każda z linii ma przypisany koszt zniszczenia jej. Chcemy wybrać zbiór połączeń do zniszczenia o łącznym minimalnym koszcie.
# Interesuje nas nie tylko koszt, ale które konkretnie linie telegraficzne mamy zniszczyć.

# complexity:
# -time O(V*E^2)
# -memory O(V^2)


def separate(graph,A):
    n = len(graph)
    visited = [False] * n
    visited[A] = True
    queue = Queue()
    queue.put(A)

    while not queue.empty():
        actual = queue.get()
        for children in range(n):
            if graph[actual][children] != 0 and visited[children] is False:
                visited[children] = True
    return visited # returning vertexes from S array


def sabotage(graph,A,B):
    n = len(graph)
    max_flow = Edmonds_Karp_max_flow(graph, A, B)
    # separating graph into two parts:
    # S- All vertices, to which can get into from A vertex
    # T - other vertices 
    S = separate(graph,A)
    edges=[]
    cost = 0
    for s in range(n):
        for t in range(n):
            if S[s] is True and S[t] is False: # vertex from S and from T
                if graph[t][s] != 0: # removing edges between S and T vertices
                    edges.append((s,t))
                    cost += graph[t][s]
                
    return edges, cost, max_flow # edges to remove, cost of edges to remove, max flow


graph = [
    [0,8,5,0,0,0,0,0],
    [0,0,0,2,0,4,0,0],
    [0,0,0,0,4,0,0,0],
    [0,0,0,0,2,3,0,0],
    [0,0,0,0,0,0,4,6],
    [0,0,0,0,0,0,2,0],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,0],
]

print(sabotage(graph,0,7))
