# Żeglarz Henryk mieszka na wysepce pewnego archipelagu. Wszystkie wyspy w tym archipelagu są tak małe,
# że można je reprezentować jako punkty w przestrzeni R2. Pozycje wszystkich wysp dane są jako ciąg W = ((x1, y1), … , (xn, yn)). 
# Henryk mieszka na wyspie(x1, y1), ale chce się przeprowadzić na wyspę (xn, yn).  Normalnie, każdego dnia
# może przepłynąć na wyspę znajdującą się w odległości najwyżej Z (w sensie standardowej odległości euklidesowej),
# ale może także każdego dnia przepłynąć odległość do 2Z, pod warunkiem, że cały następny dzień będzie odpoczywał.
#  Henryk musi zawsze nocować na jakiejś wyspie. Proszę zaproponować (bez implementacji) wielomianowy algorytm,
#  który oblicza ile minimalnie dni Henryk potrzebuje, żeby dostać się na swoją docelową wyspę (lub stwierdza, że to niemożliwe).
from queue import Queue

W = [(1,1),(1,2),(2,2),(3,3),(4,3),(5,1),(6,0),(6,1),(6,3),(8,1),(8,3),(8,5),(10,5)]


def distance(a,b): # Euclidean distance
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** (1/2)


def BFS_days(graph,days):
    queue = Queue()
    day = -1
    queue.put((0,0))

    while not queue.empty():
        day += 1
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            if actual[0] > 1:
                next_queue.put((actual[0]-1,actual[1]))
                continue
            days[actual[1]] = min(days[actual[1]],day) # can go to this verex using 2z or 1z

            for children in graph[actual[1]]:
                if days[children[1]] == float("inf"): # vertex wasn't visited before
                    next_queue.put(children) # becouse bool is imutable

        queue = next_queue


def sailor_bfs(W,z=1,start=None,end=None): # Coordinates, single max distance, start vertex index, end vertex index
    n = len(W)
    # I'll replace element, to heave start on index 0 and end as a last index
    if start is None: # start and end of BFS
        start = W[-1]
    else:
        W[0], W[start] = W[start], W[0]

    if end is None:
        end = W[-1]
    else:
        W[-1], W[end] = W[end], W[-1]

    distances = [[distance(W[i],W[j]) if i != j else float("inf") for j in range(n)] for i in range(n)]
    graph = [list() for _ in range(n)]


    for i in range(n): # creating edges list on graph
        for j in range(n):
            if i != j:
                if z- distances[i][j] >= 0:
                    graph[i].append((1,j)) # time what he need, to move to this island, index of vertex
                elif 2*z - distances[i][j] >= 0:
                    graph[i].append((2,j))
    
    days = [float("inf")] * n 
    BFS_days(graph,days)
    
    return days[-1]


print(sailor_bfs(W))

    
    