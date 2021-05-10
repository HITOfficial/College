# Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
# ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
# wychodząca z t.
# 1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n
# 2
# )).
# 2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.

g = [
    [0,0,1,1,1],
    [0,0,0,0,1],
    [0,1,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
]


def universal_mouths(graph):
    n = len(graph)
    i = 0
    j = 0
    while i < n and j < n:
        if graph[i][j] == 1:
            i += 1
        else:
            j += 1
            
    i = min(i,j)
    # check if really found good vertex
    for k in range(i):
        if i == k: continue
        if graph[i][k] == 1:
            return False
        if graph[k][i] == 0:
            return False
    return i


print(universal_mouths(g))

