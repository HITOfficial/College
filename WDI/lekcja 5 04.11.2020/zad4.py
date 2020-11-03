# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

# sum(col) // sum(row) <- a wiec obskoczę po i(rząd) j(kolumna)
                        # a więc największa kolumna // najmniejszy rząd

from random import randint
from math import ceil, log10


def zad3(i,j,n_range):
    #   utworzę klotkę w której będę przypisywał ('index', 'suma elementów')
    row_tuple = (0, 999) 
    col_tuple = (0, 0)
    square_list =[
        [randint(1, n_range) for _ in range(j)] 
        for _ in range(i)] # wygenerowałem sobie listę 2 wymiarową

    for el in square_list:
        print(el)

    row_tuple = (1, sum(square_list[0])) # <- Tworzę wzorzec z którym potem będę przyrównywał kolejne wiersze
    
    for i in range(1, len(square_list)): # i zaczynam od wiersza z indeksem 1
        if sum(square_list[i]) < row_tuple[1]:
            row_tuple = (i, sum(square_list[i]))

    col_tuple = (0, 0) # <- analogicznie tworzę wzorzec kolumn Tylko że różnica jest brana na podstawie: (kolumna - wiersz) więc wartosci 0,0 w klotce są ok, i zaoszczędzam linijek kodu
    
    for j in range(0, len(square_list)): # nie wysypie się na równej ilości wierzy i kolumn
        col_sum = 0

        for i in range(0, len(square_list)):
            col_sum += square_list[i][j]

        if col_sum > col_tuple[1]:
            col_tuple = (j, col_sum)

    return (col_tuple[0], row_tuple[0], col_tuple[1] - row_tuple[1])

print(zad3(5,5,9))


# tup = (2, 5, 'mon', False)
# list_tup = list(tup)
# list_tup[0] += 2
# tup = tuple(list_tup)

# print(tup[0])
