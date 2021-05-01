# Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd.
# Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.
# a) Policz, ile jezior jest w tablicy
# b) Policz, ile komórek zawiera największe jezioro
# c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0] do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
# d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce

 # 1- land
 # 0 - water


G = [
    [1,0,1,1,1,1,1,1],
    [1,0,1,0,0,1,1,1],
    [1,1,1,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,1,0,0,1,1,1,1],
    [1,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,1],
    [1,1,1,0,1,1,1,1]
]

def dfs_b(graph,mark_up,i,j,size):
    if i < 0 or i >= len(graph) or j < 0 or j >= len(graph) or mark_up[i][j] == True or graph[i][j] == 1: # outside indexes, land/ visided
        return size
    else:
        size += 1
        mark_up[i][j] = True

    size_tmp = size
    size_tmp = dfs_b(graph,mark_up,i-1,j,size_tmp)
    size_tmp = dfs_b(graph,mark_up,i+1,j,size_tmp)
    size_tmp = dfs_b(graph,mark_up,i,j-1,size_tmp)
    size_tmp = dfs_b(graph,mark_up,i,j+1,size_tmp)
    return size_tmp


def dfs_a_b(graph): # graph in matrix performance
    n = len(graph)
    visited = [[False, 0] * n for _ in range(n)] # graph is NxN
    max_lake = 0
    lake = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] == 0: # was'nt visited, and field is a water
                lake += 1 # it means it found start of the new lake
                max_lake = max(max_lake,dfs_b(graph,visited,i,j,0))

    return f"max lake size: {max_lake}, lakes: {lake}"

print(dfs_a_b(G))