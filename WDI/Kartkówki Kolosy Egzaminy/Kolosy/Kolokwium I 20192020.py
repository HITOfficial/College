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

def hetman_problem1(chess_table):
    length = len(chess_table)
    cord_of_hetman = []
    for i in range(length):
        for j in range(length): # za pomocą i i j szukam wolnego miejsca na tablicy wymiarowej
            if chess_table[i][j] == 0:
                chess_table[i][j] = True
                cord_of_hetman.append((i,j))
                # poziom
                for back_of_i in range(i-1,0-1,-1):
                    chess_table[back_of_i][j] = -1
                for forward_of_i in range(i+1,length,1):
                    chess_table[forward_of_i][j] = -1
                #pion
                for back_of_j in range(j-1,0-1,-1):
                    chess_table[i][back_of_j] = -1
                for forward_of_j in range(j+1,length,1):
                    chess_table[i][forward_of_j] = -1
                #ukos w prawy dół
                for horizontal, vertical in zip(range(i+1,length,1), range(j+1,length,1)):
                    chess_table[horizontal][vertical] = -1
                # # # #ukos w lewą górę
                for horizontal, vertical in zip(range(i-1,0-1,-1), range(j-1,0-1,-1)):
                    chess_table[horizontal][vertical] = -1
                # # #ukos prawą w górę
                for horizontal, vertical in zip(range(i-1,0-1,-1), range(j+1,length,1)):
                    chess_table[horizontal][vertical] = -1
                # # # #ukos w lewy dół
                for horizontal, vertical in zip(range(i+1,length,1), range(j-1,0-1,-1)):
                    chess_table[horizontal][vertical] = -1
    print(len(cord_of_hetman))
    # print(cord_of_hetman)
    
    for single_row in  chess_table:
        print(single_row)
                
# hetman_problem1(create_chess_table())








def change_table(i,j, length, chess_table):
    chess_table[i][j] = True
    # poziom
    for back_of_i in range(i-1,0-1,-1):
        chess_table[back_of_i][j] = -1
    for forward_of_i in range(i+1,length,1):
        chess_table[forward_of_i][j] = -1
    #pion
    for back_of_j in range(j-1,0-1,-1):
        chess_table[i][back_of_j] = -1
    for forward_of_j in range(j+1,length,1):
        chess_table[i][forward_of_j] = -1
    #ukos w prawy dół
    for horizontal, vertical in zip(range(i+1,length,1), range(j+1,length,1)):
        chess_table[horizontal][vertical] = -1
    # # # #ukos w lewą górę
    for horizontal, vertical in zip(range(i-1,0-1,-1), range(j-1,0-1,-1)):
        chess_table[horizontal][vertical] = -1
    # # #ukos prawą w górę
    for horizontal, vertical in zip(range(i-1,0-1,-1), range(j+1,length,1)):
        chess_table[horizontal][vertical] = -1
    # # # #ukos w lewy dół
    for horizontal, vertical in zip(range(i+1,length,1), range(j-1,0-1,-1)):
        chess_table[horizontal][vertical] = -1

    return chess_table # ma mi pomodyfikować i zwrócić tą tablicę


def find_hetman(length, hetman_cord, begin_i, begin_j):
    print(f'rozpoczęto! {begin_i, begin_j}')

    chess_table = create_chess_table() # za każdym razem tworzę pustą szachownicę 
    for i,j in hetman_cord: # uzupełniam szachownicę ustawionymi hetmanami, oraz ustawiam punkty skucia przez nich 
        chess_table = change_table(i,j, length, chess_table)
    
    for i in range(begin_i, length):
        hetman_in_row = False # za pomocą tego warunku będę sprawdzał, czy znalazłem w danym rzędzie nowego hetmana
        for j in range(begin_j, length):
            if chess_table[i][j] == 0:
                print(f'tutaj wstawiam  {i, j}')
                chess_table[i][j] = True # jeśli znajdzię puste miejsce na hetmana, to sobie już je nadpisuje
                hetman_cord.append((i,j)) # wrzucamy nowego hetmana do znalezionych
                chess_table = change_table(i,j, length, chess_table) # oraz modyfikujemy naszą szachownicę
                hetman_in_row = True # zaznaczamy, że znaleźliśmy nowego hetmana!

        if not hetman_in_row: # jeśli nie znajdziemy nowego hetmana w rzędzie to usuwamy ostatniego i tworzymy rekurencje 
            begin_i, begin_j = hetman_cord.pop() # algorytm polega na tym, że się usuwamy ostatniego hetmana, pobieramy jego kordy
            print(f' tego usuwam {begin_i, begin_j}')
            find_hetman(length, hetman_cord, begin_i , begin_j+1) # i w następnej rekurencji, cofamy się o 1 rząd i zaczynamy przeszukiwanie od następnej kolumny XD a się jebałem z tym że wiersz dodatkowo cofałem jeszcze raz 
            break # tej już nie będę potrzebował
        begin_j = 0 # potrzebowałem do jednej iteracji znalezienia kolumny wiekszej, takto lecę normalnie, jeśli za pierwszym razem znalazło wolne miejsce na hetmana       
    
    # for el in chess_table:
    #     print(el)
    return hetman_cord




def hetman_problem():
    length = 8 
    hetman_cord = [] # bedę ustawiał w niej tuple cordów nowych hetmanów

    # muszę obskoczyć wstawianie hetmanów rekurencyjnie

    hetman_cord = list(find_hetman(length, hetman_cord,0 ,0))
    print(hetman_cord)
hetman_problem()
    
