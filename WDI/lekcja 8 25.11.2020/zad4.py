# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego

# skoczek szachowy porusza się L'ką -> (2 i, 1j), (1i, 2j)

from zad3 import two_dim_list

# gdy skoczek był na polu -> True, gdy go nie odwiedził -> False
def chess_jumper_moves(n=3, start=(0,0)):
    list_to_fill = [[False for _ in range(n)] for _ in range(n)] # utworzę listę False którą będę nadpisywał na True, jesli na tym polu był już skoczek
    # nie przyjmuję za argument listy tylko jest ona zewnętrzna, żeby nie mieć kolizji w środku
    def chess_jumper(actual_cord):
        i = actual_cord[0]
        j = actual_cord[1]

        #góra
        if i-2 >= 0:
            if j-1 >= 0 and list_to_fill[i-2][j-1] == False:
                list_to_fill[i-2][j-1] = True # kładę na niej skoczka
                chess_jumper((i-2,j-1))
            if j+1 < n and list_to_fill[i-2][j+1] == False:
                list_to_fill[i-2][j+1] = True
                chess_jumper((i-2,j+1))

        #dół
        if i+2 < n:
            if j-1 >= 0 and list_to_fill[i+2][j-1] == False:
                list_to_fill[i-2][j-1] = True # kładę na niej skoczka
                chess_jumper((i+2,j-1))
            if j+1 < n and list_to_fill[i+2][j+1] == False:
                list_to_fill[i+2][j+1] = True
                chess_jumper((i+2,j+1))
        
        #lewo
        if j-2 >= 0:
            if i-1 >= 0 and list_to_fill[i-1][j-2] == False:
                list_to_fill[i-1][j-2] = True # kładę na niej skoczka
                chess_jumper((i-1,j-2))
            if i+1 < n and list_to_fill[i+1][j-2] == False:
                list_to_fill[i+1][j-2] = True
                chess_jumper((i+1,j-2))

        #prawo
        if j+2 < n:
            if i-1 >= 0 and list_to_fill[i-1][j+2] == False:
                list_to_fill[i-1][j-2] = True # kładę na niej skoczka
                chess_jumper((i-1,j+2))
            if i+1 < n and list_to_fill[i+1][j+2] == False:
                list_to_fill[i+1][j+2] = True
                chess_jumper((i+1,j+2))


    chess_jumper(start)

    return list_to_fill

    
n = 5
T = [[0 for _ in range(n)] for _ in range(n)]


# Z POKAZANIEM HISTORII SKOKÓW SKOCZKA
 

from copy import deepcopy

# musi lecieć jednocześnie tylko jedna rekurencja, aby nie nadpisywać już nieskończoność wykonanych ruchów
def chess_jumper_fill_moves(list_to_fill, count=1, actual_i=0, actual_j=0):
    list_to_fill[actual_i][actual_j] = count

    if len(list_to_fill)**2 == count:
        for row in list_to_fill:
            print(row)
        exit(0)

    moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)] # pozycje, o które może się przenieść skoczek
    for i,j in moves: # wypakowywwuję tupla i będę sprawdzał czy mogę postawić skoczka na nowym miejscu
        new_i = actual_i + i
        new_j = actual_j + j
        if new_i <= len(list_to_fill) -1 and new_i >= 0 and new_j <= len(list_to_fill) -1 and new_j >= 0: # dodatkowy warunek aby nie wyskoczyć poza tablicę oraz lista jest wymiarów NxN a więc spokojnie mogę sprawdzać czy nie wychodzi poza wiersz przy warunku z kolumn
            if list_to_fill[new_i][new_j] == 0: 
                chess_jumper_fill_moves(deepcopy(list_to_fill), count +1, new_i, new_j)
  
    
chess_jumper_fill_moves(T)
