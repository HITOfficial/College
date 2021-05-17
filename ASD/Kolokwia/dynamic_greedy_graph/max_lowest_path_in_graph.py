# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def enlarge(G, s, t):
# ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
# warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
# sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
# Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
# krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
# nie było ścieżki z s do t to funkcja powinna zwrócić None.

from queue import Queue
from copy import deepcopy



# nie jest podane w treści, że graf nie posiada cykli, więc może je mieć, inaczej bym robił to drogą eulera, dopinając s do t krawędzią
# Puszam BFS i znajduję najkrótszą ścieżkę, następnie usuwam kazdą z możliwych krawędzi i ponownie puszczam BFS, dzięki temu mam gwarancje że uzyskam najlepszy wynik

# złożoność obliczeniowa  O(N^2*(N+E)) macierz kwadratowa + BFS, chociaż bę znacznie lepsza złożoność, ponieważ z reguły nigdy nie dojdzie do N^2, bo drugi foor loop zaczyna z indexem późniejszym niż pierwszy
# złożoność pamięciowa O(N^2)

def BFS_waves(graph,s,t): # graf, start
    times = [float("inf")] * len(graph)
    queue = Queue()
    time = -1 # zaczynam sztucznie przed poczatkiem
    queue.put(s)

    while not queue.empty():
        time += 1
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            times[actual] = min(time,times[actual]) # ustawiam fale, kiedy przyszła
            for children in graph[actual]:
                if times[children] == float("inf"): # nie odwiedzony dotychczas
                    next_queue.put(children) # wrzucam wierzchołki do następnej fali
        queue = next_queue # nadmieniam starą kolejkę(aktualny czas, która jest pusta), na nową do przetworzenie w nastepnym czasie    

    return times[t]
    

def enlarge(G,s,t):
    n = len(G)
    G_copy = deepcopy(G)

    edges = [[False] * n for _ in range(n)] # sztucznie tworzę wszystkie możliwości
    # przerabiam na postac macierzową ścieżkę
    for vertex in range(n): # markuje znalezione krawędzie, żeby potem mieć dostęp O(1)
        for children in G[vertex]:
            edges[vertex][children] = True
            edges[children][vertex] = True


    lowest = BFS_waves(G,s,t)
    if lowest == float("inf"): # mógł bym sprawdzić to DFS'em (było by szybciej zazwyczaj) ale przy BFS'ie otrzymam dotychczasowo najkrótszą ścieżkę
        return None
    lowest_tmp = lowest
    coord = (0,0)
    for i in range(n-1):
        for j in range(i+1,n): # żeby dwókrotnie nie sprawdzac tych samych pól
            if edges[i][j] == True: # ma krawędź, więc mogę ją usunąć
                index1 = None # index krawedzi w 1wszym
                index2 = None # index krawedzi w 2gim
                for k in range(len(G[i])): # znajduję tą krawedz w postaci listowej O(E)
                    if k < len(G[i]): # zeby nie wyskoczyc poza zasieg
                        if G[i][k] == j: # znalazlo index krawędzi
                            index1 = k
                    if k < len(G[j]):
                        if G[j][k] == i:
                            index2 = k
                
                if index1 != None:
                    del G[i][index1] # usuwam aktualna krawedz
                if index2 != None:
                    del G[j][index2]
                
                new_lowest = BFS_waves(G,s,t) # puszam fale

                if index1 != None:
                    G[i].append(j) # dokładam z powrotem tą krawędź
                if index2 != None:
                    G[j].append(i)
                if new_lowest != float("inf") and lowest < new_lowest: # udało się uzyskać tą krawędź
                    lowest = new_lowest
                    coord = (i,j)
                    
    G = G_copy # ustawiam w nienaruszonym stanie
    if lowest > lowest_tmp: # znalazło lepszy wynik
        return coord
    return None # nie znalazło lepszego wyniku
