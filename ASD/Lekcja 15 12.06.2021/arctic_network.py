# Algorithm to find max edge in MST
from math import ceil, sqrt
from queue import PriorityQueue

# Exercise in PL lang.
# W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary współrzędnych (x, y).
# Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować się z każdą inną osadą, która ma odbiornik satelitarny.
# Chcemy teraz w każdej osadzie umiejscowić radioodbiorniki o tym samym ograniczonym zasięgu D (liczba całkowita), aby można było się komunikować 
# pośrednio lub bezpośrednio) między każdą parą osad. Jakie jest minimalne D, które pozwoli osiągnąć ten cel?
# Uzasadnij poprawność rozwiązania.

# corectity of the exercise
# all edges need to be connected to network -> from this reason all vertexes need to have edge, with one of the others vertexes, so  minumum spanning, using Prims method will solve this problem

# matrix adjacency: K(N) graph (every vertex n-1 has edges)
# complexity:
# -time O(V^2logV) <- Prims MST on matrix adjacency
# -memory O(V^2) <- to dynamicaly memorize distance from every edges


def distance(a, b): # Euclidean distance
    a1, b1 = a
    a2, b2 = b
    return ceil(sqrt(pow(a1-a2,2)+pow(b1-b2,2))) # length of vector


def relax(dist,b,e,w):
    if dist[e] > dist[b] + w: # is worth to realx this edge
        dist[e] = dist[b] + w
        return True
    else:
        return False


def artic_network(graph):
    n = len(graph)
    distances = [[distance(graph[i],graph[j]) if i != j else float("inf") for j in range(n)] for i in range(n)]
    dist = [float("inf")] * n # lowest distance to every vertex from vertex 0
    dist[0] = 0
    counter = n
    D = 0

    p_queue = PriorityQueue()
    for i in range(1,n):
        p_queue.put((distances[0][i], 0, i)) # distance(edge weight), vertexes: from, to

    while not p_queue.empty() and counter > 0:
        w, b, e = p_queue.get()
        if relax(dist,b,e,w):
            counter -= 1
            D = max(D,w)
            for i in range(n):
                if i != b and i != e: 
                    p_queue.put((distances[e][i], e, i))

    return D


graph = [
    [9, 24], [11, 2], [-5, 26], [28, -17], [23, 11], [-24, -24], [29, 24],
    [-25, 27], [22, -16], [5, 2], [15, -25], [24, -10], [-9, 9], [18, 4],
    [-19, 10], [16, -3], [30, 10], [26, 11], [-20, -17], [-17, 27]
]

print(artic_network(graph))