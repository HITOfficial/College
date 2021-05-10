# Proszę podać jak najszybszy algorytm, który znajduje w grafie
# cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie
# n to liczba wierzchołków---chodzi o rozwiązanie szybsze).

# Cycle C4 in O(n^3)

g = [
    [0,1,0,1,0,0,0],
    [1,0,1,0,0,0,0],
    [0,1,0,1,1,0,0],
    [1,0,1,0,0,0,0],
    [0,0,1,0,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,0,1,1,0],
]

def cycle_c4(graph):
    n = len(graph)
    for i in range(n):
        for j in range(i+1,n):
            if i != j:
                stack = []
                for k in range(n):
                    if graph[i][k] == graph[j][k] == 1:
                        stack.append(i)
                        stack.append(j)
                if len(stack) >= 4:
                    return True
    return False


print(cycle_c4(g))
