# Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
# posiadał nieparzystą liczbę jedynek.
# Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
# funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
# nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
# figury była równa zero.
# Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.
# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy był wielokrotnością
# (co najmniej dwukrotnością) kwadratu dowolnej liczby naturalne większej od 1.

# Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
# funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego hetmana szachowego aby żaden hetman nie
# zagrażał hetmanowi z sąsiedniego wiersza. Dodatkowo, suma wartości pól zajmowanych przez wszystkie figury była
# równa zero. 

from random import randint

# Hetman = 1
# Pola bite = -1

def create_chess_table():
    chess_table = [[0 for _ in range(8)] for _ in range(8)]
    return chess_table

def Hetman_problem(chess_table):
    length = len(chess_table)
    cord_of_hetman = []
    for i in range(length):
        for j in range(length): # za pomocą i i j szukam wolnego miejsca na tablicy wymiarowej
            if i == 0 and j == 1:
                chess_table[i][j] = True
                cord_of_hetman.append((i,j))
                # poziom
                for back_of_i in range(i-1,0-1,-1):
                    chess_table[back_of_i][j] = -1
                for forward_of_i in range(i+1,length,1):
                    chess_table[forward_of_i][j] = -1
                #pion
                for back_of_j in range(i-1,0-1,-1):
                    chess_table[i][back_of_j] = -1
                for forward_of_j in range(i+1,length,1):
                    chess_table[i][forward_of_j] = -1
                #ukos w prawy dół
                for horizontal, vertical in zip(range(i+1,length,1), range(j+1,length,1)):
                    chess_table[horizontal][vertical] = -1
                # # #ukos w lewą górę
                for horizontal, vertical in zip(range(i-1,0-1,-1), range(j-1,0-1,-1)):
                    print(horizontal, vertical)
                    chess_table[horizontal][vertical] = -1
                # #ukos prawą w górę
                for horizontal, vertical in zip(range(i-1,0-1,-1), range(j+1,length,1)):
                    chess_table[horizontal][vertical] = -1
                # # #ukos w lewy dół
                for horizontal, vertical in zip(range(i+1,length,1), range(j-1,0-1,-1)):
                    chess_table[horizontal][vertical] = -1

                for _ in  chess_table:
                        print(_)
                

    

Hetman_problem(create_chess_table())
