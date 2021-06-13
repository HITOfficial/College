# Exercise in PL lang.

# Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą).
# Dane jest także słowo W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G,
# której wierzchołki układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki). Jeśli takiej ścieżki nie ma, należy zwrócić -1. 
# Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i.
# E jest listą krawędzi i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki połączone krawędzią o wadze w. Przykład. Rozważmy graf G przedstawiony poniżej: 0∶ k 1∶ k 2∶ o 3∶ o 4∶t 5∶t 2 1 2 3 5 1 3
# W reprezentacji przyjętej w zadaniu mógłby być zapisany jako: # 0 1 2 3 4 5 L = ["k","k","o","o","t","t"] E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ] G = (E,L) 
# Rozwiązaniem dla tego grafu i słowa W = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8.
from queue import PriorityQueue

# complexity:
# -time O(K*VlogE) where K is a number of vertices that start W word
# -memory O(V)


def list_adjacency(E,n):
    graph = [[] for _ in range(n)]
    for b,e,w in E: # undirected graph
        graph[e].append((b,w))
        graph[b].append((e,w))
    return graph


# mix of Dijkstra and Prims MST algorithm
def Dijkstra_Prims_word(graph,L,letters,remaing,start): # graphm list adjacenct, dictionary of letters, letters array, letters left to find, starting vertex
    # "ot" neet to be find
    p_queue = PriorityQueue()
    distances = [float("inf")] * len(graph)
    distances[start] = 0
    for children, weight in graph[start]:
        if letters[ord(L[children])] > 0: # need to find this letter
            p_queue.put((start,children, weight))

    edges = [(start,start,0)]

    while not p_queue.empty() and remaing > 0:
        b,e,w = p_queue.get()
        if letters[ord(L[e])] > 0 and distances[e] > distances[b] + w: # need to take this letter, and distance can be reduced
            remaing -= 1
            letters[ord(L[e])] -= 1 # reducing letters to find
            edges.append((b,e,w)) # memorizing edge
            for children,weight in graph[e]:
                if letters[ord(L[children])] > 0 and children != b: # need to take this letter
                    p_queue.put((e,children,weight))

    if remaing > 0: # doesnt found a path
        return float("inf"), []
    else:
        return sum([weight for _, _, weight in edges]), [vertex for _ ,vertex ,_ in edges]


def MST_word(G,W):
    L = G[1]
    E = G[0]
    n = len(L)
    # data incomming can be in 
    ASCI_array = [[] for _ in range(128)] # letters can be only from ASCI code 
    # extra array to take only letters which need to find
    remaing_letters = [0] * 128 # ASCI symbols

    # memorizing on which vertices can start letter
    for number, _, _ in E:
        ASCI_array[ord(L[number])].append(number)
        ASCI_array[ord(L[number])] = list(set(ASCI_array[ord(L[number])])) # removing eventual copies of every vertices
    for letter in W:
        remaing_letters[ord(letter)] += 1 # memorizing which letters need to be find

    lowest_distance, best_path = float("inf"), []
    graph = list_adjacency(G[0],n)
    
    for start in ASCI_array[ord(W[0])]: # running mixed Dijkstra from vertices on which in a starting letter of word
        letters = remaing_letters.copy()
        remaing = len(W) - 1        
        letters[ord(W[0])] -= 1 # reducing first letter
        distance, path = Dijkstra_Prims_word(graph,L,letters,remaing,start)
        if distance < lowest_distance:
            lowest_distance = distance
            best_path = path

    if lowest_distance != float("inf"):
        return lowest_distance, best_path
    else: # doesnt found a path
        return -1


# A bit Greedy Algorithm doesnt not always correctly, for "koto" will return 6 [1,2,3,4], when 5 is correct answer [1,2,4,3]
L = ["k","k","o","o","t","t"]
E = [(0,2,2),(1,2,1),(1,4,3),(1,3,2),(2,4,5),(3,4,1),(3,5,3)]
G = (E,L)
W = "kto"
    
print(MST_word(G,"kto"))

