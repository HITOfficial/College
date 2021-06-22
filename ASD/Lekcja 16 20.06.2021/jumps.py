# Exercise in PL lang.
# Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
# jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
# T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
# do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
# wartość -1.
# Przykład Dla tablicy T = [123,890,688,587,257,246] wynikiem jest liczba 767, a dla tablicy
# T = [587,990,257,246,668,132] wynikiem jest liczba -1.

import numpy as np
from queue import PriorityQueue

# creating undirected graph on matrix adjacencty, and runing Dijkstra from min number vertex to max number
# complexity:
# -time O(V^2logV) / O(V^2*N) Dijkstra on matrix Adjacency / finding same digit in numbers
# -memory O(V^2) -> matrix adjacency in graph


# creating 10*N list to have in O(1) time information about single digit in numbers
def digits(array,n):
    array_numbers = [[0]*10 for _ in range(n)]
    for i in range(n):
        tmp_number = array[i] + 0
        while tmp_number > 0:
            array_numbers[i][tmp_number%10] = 1
            tmp_number //= 10
    return array_numbers


# creating undirected graph on matrix adjacencty
def construct_graph(array,n):
    array_numbers = digits(array,n)
    # -1 <- there is no edge between vertices
    graph = [[-1]*n for _ in range(n)]
    for i in range(n-1):
        tmp_number = array[i] + 0
        while tmp_number > 0:
            digit = tmp_number % 10
            # finding the same digit in another number
            for j in range(i+1,n):
                if j != i and array_numbers[j][digit] == 1:
                    distance = abs(array[i] - array[j])
                    # adding only shortest distance
                    if graph[i][j] != -1:
                        graph[i][j] = min(graph[i][j],distance)
                        graph[j][i] = min(graph[i][j],distance)
                    else:
                        graph[i][j] = distance
                        graph[j][i] = distance
            tmp_number //= 10
    return graph
        

def jupms(array):
    n = len(array)
    max_index = np.argmax(array)
    min_index = np.argmin(array)

    # Dijkstra algorithm of min distance between vertices
    graph = construct_graph(array,n)
    distances=[float("inf")]*n
    distances[min_index] = 0
    p_queue = PriorityQueue()
    counter = n

    # adding all neighbour vertices with minimum value
    for i in range(n):
        distance = graph[min_index][i]
        if distance != -1:
            p_queue.put((distance,min_index,i))

    # starting Dijkstra alg. on Priority Queue
    while not p_queue.empty() and counter > 0:
        d,b,e = p_queue.get()
        # relaxing edge
        if distances[e] > distances[b] + d:
            # it is posible to reduce distance
            counter -= 1
            distances[e] = distances[b] + d
            for children in range(n):
                if graph[e][children] != -1 and children != b:
                    p_queue.put((graph[e][children],e,children))

    # checking if was possible to get into max value vertex
    if distances[max_index] == float("inf"):
        return -1
    else:
        return distances[max_index]


T1 = [123,890,688,587,257,246]
T2 = [587,990,257,246,668,132]

print(jupms(T1))
print(jupms(T2))