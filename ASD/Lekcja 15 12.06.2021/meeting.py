# Using twice Dijkstra to find shortest distances to the best vertex for meeting (lowest sum distance to get into for professor and student)
from queue import PriorityQueue, Queue

# Exercise in Pl lang.
# Pewien znany profesor zaprosił Cię na spotkanie w Magicznym Mieście. W mieście tym niektóre drogi mogą być uczęszczane tylko przez ludzi poniżej 30 roku życia (w tym Ciebie),
# inne tylko przez ludzi w wieku od 30 lat (w tym profesora). Są też drogi, które mogą być uczęszczane przez każdego. Każda z dróg ma określoną długość, wyrażoną dodatnią liczbą naturalną, może być jedno- lub dwukierunkowa.
# Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy mieszkanie Twoje i mieszkanie profesora.
# Profesor prosi Cię, byś wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać Ty i profesor była jak najmniejsza. Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie.
# Jeżeli takie miejsce nie istnieje, algorytm również powinien to stwierdzić.


# runing Dijkstra twice, for profesor, and for student, and then finding minimum sum, of distances to vertices

# complexity:
# -time O(V^2logV)
# - memory O(V)

# graph representation- matrix adjacency
# second value in tuple:
# 0- can use profesor and student
# 1- can use only student
# 2- can use only professor



graph = [
    [(0,0),(5,0),(1,0),(8,0),(0,0),(0,0),(0,0)],
    [(5,1),(0,0),(0,0),(1,1),(0,0),(8,2),(0,0)],
    [(1,0),(0,0),(0,0),(8,0),(0,0),(0,0),(8,0)],
    [(8,0),(1,1),(8,0),(8,0),(5,0),(0,0),(1,2)],
    [(0,0),(0,0),(0,0),(5,2),(0,0),(1,1),(0,0)],
    [(0,0),(8,2),(0,0),(0,0),(1,1),(0,0),(5,0)],
    [(0,0),(0,0),(8,2),(1,1),(0,0),(5,2),(0,0)],
]


def relax(distances,b,e,w):
    if distances[e] > distances[b] + w:
        distances[e] = distances[b] + w
        return True
    else:
        return False


def Dijkstra_parameter(graph,b,paramenter): # graph matrix adjacency, begin, parameter
    n = len(graph)
    distances = [float("inf")] * n
    distances[b] = 0

    p_queue = Queue()
    for i in range(n):
        d,p = graph[b][i]
        if d != 0 and p != paramenter:
            p_queue.put((d,b,i))

    while not p_queue.empty():
        d,p,t = p_queue.get() # edge weight, begin, end
        if relax(distances,p,t,d):
            for i in range(n):
                d,p = graph[p][i]
                if d != 0 and p != paramenter:
                    p_queue.put((d,t,i))
                    
    return distances


def meeting(graph,s,p): # graph, student, profesor starting vertex
    n = len(graph)
    student_distance =  Dijkstra_parameter(graph,s,2) # shortest distances to vertices without professors path
    professor_distance =  Dijkstra_parameter(graph,p,1) # shortest distances to vertices without students path
    lowest_distance, meeting_vertex = float("inf"), None
    for i in range(n):
        if professor_distance[i] + student_distance[i] < lowest_distance:
            lowest_distance = professor_distance[i] + student_distance[i]
            meeting_vertex = i
    if lowest_distance != float("inf"): # found the best place for meeting
        return lowest_distance, meeting_vertex
    else:
        return False # cannot find place for meeting


print(meeting(graph,0,6))