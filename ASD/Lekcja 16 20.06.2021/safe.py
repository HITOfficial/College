# Exercise in PL lang.
# Dostałeś sejf, który odblokowuje się czterocyfrowym PINem (0000 - 9999). Pod wyświetlaczem znajduje się kilka przycisków
# z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902). Sejf ten działa inaczej niż normalny: wciśnięcie przycisku
# z liczbą powoduje dodanie liczby z przycisku do liczby na wyświetlaczu. Jeżeli suma jest większa niż 9999, to pierwsza cyfra zostaje obcięta.
# Jest tobie znany PIN oraz cyfry, które są aktualnie wyświetlane. Znajdź najkrótszą sekwencję naciśnięć przycisków, która pozwoli ci odblokować sejf.
# Jeżeli taka sekwencja nie istnieje, zwróć None.
from collections import deque

# constructing directed graph on matrix adjacency, and finding the shortest path using BFS alg. to unlock the safe

# complexity:
# -time O(V^2) BFS / constructing graph
# -memory O(V^2) Graph / numbers from K

def get_path(paths,paths_vertices,actual,begin):
    array = []
    if actual != begin:
        array.append(paths_vertices[actual])
        array.extend(get_path(paths,paths_vertices,paths[actual],begin))
    return array


# constructing directed graph
def construct_graph(k,b,n):
    graph = [[0]*n for _ in range(n)]
    prev_vertices = [[None]*n for _ in range(n)]
    # using deque as LIFO queue
    deq = deque()
    deq.appendleft(b)
    while deq:
        vertex = deq.popleft()
        for number in k:
            new_vertex = (vertex+number)%n
            if graph[vertex][new_vertex] == 0:
                graph[vertex][new_vertex] = 1
                prev_vertices[vertex][new_vertex] = number
                deq.append(new_vertex)
    return graph, prev_vertices


# finding shortest path to all verices in graph
def BFS(graph,prev_vertices,n,actual):
    visited = [False]*n
    paths = [None] *n
    paths_vertices = [None] * n
    visited[actual] = True
    # modyfied BFS alg. on matrix adjacency - not memorizing time executing
    deq = deque()
    deq.append(actual)
    while deq:
        new_deq = deque()
        # memorizing all visited vertices in actual time 
        while deq:
            actual = deq.popleft()
            for i in range(n):
                # finding all not visited neighbours
                if visited[i] is False and graph[actual][i] == 1: 
                    # on reconstruction of path, needed used vertices not vertices %N
                    paths[i] = actual
                    paths_vertices[i] = prev_vertices[actual][i]
                    visited[i] = True
                    new_deq.append(i)
        deq = new_deq
    return paths, paths_vertices


def safe(k,b,e): # Array of numbers able to use, number set before, PIN to find
    n = 10000
    graph, prev_vertices = construct_graph(k,b,n)
    # detecting if is posible to get into PIN number 
    flag = False
    for i in range(n):
        if graph[i][e] == 1:
            flag = True
            break
    if flag is False:
        return
    # BFS alg. to find shortest path, to get the PIN
    paths, paths_vertices = BFS(graph,prev_vertices,n,b)
    path = list(reversed(get_path(paths,paths_vertices,e,b)))
    return path
    

b = 0
e = 18
k = [13,223,782,390]

print(safe(k,0,18))