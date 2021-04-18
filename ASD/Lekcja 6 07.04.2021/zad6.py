from math import *
# ZADANIE NIEDOKOŃCZONE -> NIE PRAWIDŁOWO ZWRACA ŚCIEZKĘ


# na samym początku nie wiem czy zaczną tworzyć ścieżkę idąc górą czy dołem, dlatego 1wszą część drogi zaznaczam jako 1 a drugą jako -1
# znadę element k <- koniec drugiej ścieżki, połączę ją z elementem ostatnim i zacznę odtwarzać ścieżkę od końca


# C = [["Wrocław", 1, 1], ["Gdańsk",4,2], ["Katowice",8,6], ["Jasło",10,4], ["Szczecin",14,1], ["Kraków",13,4], ["Warszawa",6,0], ["Śląsk",11,0],["Łódź",2,8]]
# C = [["Wrocław", 0, 2], ["Warszawa",4,3],["Gdańsk", 2,4], ["Kraków",3,1]]
C = [["A",0,0], ["H",5,5],["F",9,4],["E",8,2],["G",6,6],["B",2,0],["D",5,2],["C",4,0]]
# C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
#      ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
#      ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]


def print_path(P,C): # miasta posortowane po X, Ścieżka, długość, index
    count = 0
    i = 0
    n = len(C)
    while count < n:
        if P[i] != None:
            print("\"",C[P[i]][0],"\"")
            i = P[i]
        count+= 1
    return ""


def distance(a,b):
    vector_x = a[1]-b[1]
    vector_y = a[2]-b[2]
    return sqrt(vector_x**2+vector_y**2)


def traveling_salesman(traveling_distance, distances, paths, i, j):#Arr:uwzględniajaca wszystkie pomiędzy, bezpośrednia, ścieżki, indexy: miasto1, miasto2
    if traveling_distance[i][j] != float("inf"): # już była policzona drogą dzielaca miasto i oraz j przechodząc przez wszystkie miasta pomiędzy nimi
        return traveling_distance[i][j], j,i
    if i == j-1: # przed ostatni element
        lowest_distance, index_nearlesst = float("inf"), i
        for k in range(i):
            tmp_distance,_, tmp_index = traveling_salesman(traveling_distance, distances, paths, k, i)  # szuka bezpośredniego najbliższego miasta
            tmp_distance += distances[j][k] # zwracam tupla z rekurencji, więc po zwórceniu dodam aktualny odcinek
            if tmp_distance < lowest_distance: # dopinam miasto najbliższe, i szukam kolejnych
                lowest_distance = tmp_distance
                index_nearlesst = tmp_index
        if index_nearlesst != i: # i-te i j-te miasto znajdują się na innych ścieżkach
            paths[j] = 1 # pierwsza ścieżka
            paths[index_nearlesst] = 1
            paths[i] = -1 # druga ścieżka
        else: # ta sama ścieżka
            paths[j] = 1
            paths[i] = 1
        traveling_distance[i][j] = lowest_distance
    else: # i < j-1 -> cała drogia od i -> j, gdzie j-1 jest bezpośrednio przed j
        traveling_distance[i][j] = traveling_salesman(traveling_distance, distances, paths,i , j-1)[0] + distances[j-1][j]
    return traveling_distance[i][j], j,i


def bitonicTSP( C ): # miasta
    n = len(C) # dodatkowo uwzględniam że odległość miasta między samym sobą jest nieskończona
    C.sort(key = lambda x: x[1]) # sortuje po drugiej wartości -> (wartość X'owa)
    distances = [[distance(C[i],C[j]) if j != i else float("inf") for j in range(n)] for i in range(n)] # bezpośrednie odległości pomiędzy dwoma miastami
    paths = [None]* n # w tej tablicy będę przetrzymywał ścieżkę
    traveling_distance = [[float("inf")]*n for _ in range(n)] # najkrótsza ścieżka idąca od miasta a->b przechodząc przez wszystkie miasta pomiędzy
    traveling_distance[0][1] = distances[0][1] # wrzucam odległość 1wszego miasta na drodze od początkowego
    # ponieważ nie znam k, które stanowiło by początek drugiej ścieżki, musi ją foor loop samo poszukać -> dodatkowowa złożoność obliczeniowa stanowi O(1)* rekursja ogonowa
    minimum_distance, index_k = float("inf"), 0 # najmniejszy dystans komiwojażera, index 
    for i in range(n-1):
        tmp_distance,_, tmp_index = traveling_salesman(traveling_distance,distances,paths,i,n-1)
        tmp_distance += distances[i][n-1]
        if tmp_distance < minimum_distance:
            minimum_distance, index_k = tmp_distance, tmp_index # znalazło lepsze K

    paths[index_k] = -1
    print(index_k,"to")
    print(C)
    for i in range(n):
        if paths[i]== 1:
            print(C[i][0])
    for i in range(n-1,-1,-1):
        if paths[i]== -1:
            print(C[i][0])
    print(C[0][0])
    print(paths)
    # print_path(paths, C)
    return minimum_distance


print(bitonicTSP(C))
