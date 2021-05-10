# Dany jest spójny graf nieskierowany G = (V,E). Proszę
# zaproponować algorytm, który znajdzie taką kolejność usuwania
# wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
# przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
# dotykające go krawędzie).

# using BFS and making waves -> removing all vertices, without disconnections on graph

g = [
    [1,3],
    [0,2,7],
    [1,4],
    [0,2],
    [2,5,6],
    [4,6],
    [4,5],
    [2,8],
    [7,9],
    [8]
]


def BFS_waves(graph, parent=0): # graph, starting element
    path = [parent]
    wave = [parent]
    visited = [False] * len(graph) # to do not take the same vertex twice, or more
    visited[parent] = True

    while len(wave) > 0:
        parent = wave.pop(0)    
        for children in graph[parent]:
            if visited[children] == False:
                wave.append(children) # creating next wave
                path.append(children)
                visited[children] = True

    path.reverse()
    return path


print(BFS_waves(g))

        
