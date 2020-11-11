from copy import deepcopy
from random import randint

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


# CHYBA DZIAŁA POPRAWNIE 
import copy # potrzebuję robić głębokie kopie bo, bo w listach zawieram kolejne listy, a więc mam obiekty mutable

def create_random_n_list(n=10): # do celów sprawdzenia utworzyłem generator list
    n_list = [[randint(10, 70) for _ in range(n)] for _ in range(n)]
    return n_list
    

def pows_of_number(n): 
    for i in range(1,1000): # sprawdzam od n żeby zaoszczędzic trochę liczenia do 1000
        for power in range(2,11): # sprawdza od 2 do 10 potęgi żeby nie mulić programu
            if i ** power > n:
                break
            elif i ** power == n:
                return True # jesli znajdzie taką potęge to kończy działanie

    return False # inaczej nie znalazło takiej potęgi


def count_finded_pows(list_to_search):
    count_all_elements = 0
    count_pows = 0

    for i in range(len(list_to_search)):
        for j in range(len(list_to_search[i])): # liczę czy dla każdej liczby z listy znalazło potęgę 
            count_all_elements += 1
            if pows_of_number(list_to_search[i][j]):
                count_pows += 1 

    if count_all_elements == count_pows:
        return True
        
    return False


# usunąć jeden wiersz i 2 kolumny
def able_to_remove(n_list):

    for i in range(len(n_list)):
        list_copy = copy.deepcopy(n_list) # dopiero deepcopy działa bez referencji
        del list_copy[i] # najpierw usuwam wiersz
        
        for col1 in range(len(list_copy)): # pierwszą kolumnę do wycięcia wybieram na n-1 sposobów 
            list_copy_col1 = copy.deepcopy(list_copy)
            for row in range(len(list_copy)):
                del list_copy_col1[row][col1] # tak usuwam pierwszą z kolumn

            for col2 in range(col1,len(list_copy_col1)): # żeby nie sprawdzać po dwa razy tych samych kolumn to: zaczynam szukanie drugiej do  od indexu pierwszej co usunąłem 01 02, 03 -> 12 13 -> 23 
                list_copy_col2 = copy.deepcopy(list_copy_col1) # robię kopię z usuniętą pierwszą kolumną
                for row in range(len(list_copy_col1)):
                    del list_copy_col2[row][col2]
                # for el in list_copy_col2:
                #     print(el)
                # teraz mam kandytatów w liście, żeby sprawdzić, czy spełniają warunki zadania
                if count_finded_pows(list_copy_col2): # to jest ta lista z powykreślanymi 2 kolumnami i jednym wierszem
                    return print(True) # jeśli znajdzie potęgę liczby dla każdego elementu z list to kończymy szukanie 


    return print(False) # jeśli przeleci po wszystkich
                
              
able_to_remove(create_random_n_list(4))



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

def create_random_number_list():
    random_number_list = [[randint(-5,6) for _ in range(8)] for _ in range(8)]
    return random_number_list

def sum_of_values(list_of_index, list_to_take_data):
    sum_of_elements = 0
    for row, col in list_of_index:
        sum_of_elements += list_to_take_data[row][col]
    
    return sum_of_elements


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
    # print(f'rozpoczęto! {begin_i, begin_j}')

    chess_table = create_chess_table() # za każdym razem tworzę pustą szachownicę 
    for i,j in hetman_cord: # uzupełniam szachownicę ustawionymi hetmanami, oraz ustawiam punkty skucia przez nich 
        chess_table = change_table(i,j, length, chess_table)
    
    for i in range(begin_i, length):
        hetman_in_row = False # za pomocą tego warunku będę sprawdzał, czy znalazłem w danym rzędzie nowego hetmana
        for j in range(begin_j, length):
            if chess_table[i][j] == 0:
                # print(f'tutaj wstawiam  {i, j}')
                chess_table[i][j] = True # jeśli znajdzię puste miejsce na hetmana, to sobie już je nadpisuje
                hetman_cord.append((i,j)) # wrzucamy nowego hetmana do znalezionych
                chess_table = change_table(i,j, length, chess_table) # oraz modyfikujemy naszą szachownicę
                hetman_in_row = True # zaznaczamy, że znaleźliśmy nowego hetmana!

        if not hetman_in_row: # jeśli nie znajdziemy nowego hetmana w rzędzie to usuwamy ostatniego i tworzymy rekurencje 
            begin_i, begin_j = hetman_cord.pop() # algorytm polega na tym, że się usuwamy ostatniego hetmana, pobieramy jego kordy
            # print(f' tego usuwam {begin_i, begin_j}')
            find_hetman(length, hetman_cord, begin_i , begin_j+1) # i w następnej rekurencji, cofamy się o 1 rząd i zaczynamy przeszukiwanie od następnej kolumny, a się jebałem z tym że wiersz dodatkowo cofałem jeszcze raz 
            break # tej już nie będę potrzebował
        begin_j = 0 # potrzebowałem do jednej iteracji znalezienia kolumny wiekszej, takto lecę normalnie, jeśli za pierwszym razem znalazło wolne miejsce na hetmana       
    
    return hetman_cord


# potrzebowałem sobie zrobić dodatkową funkcję specjalnie na rekurencje do niej samej żeby nie resetować wartości z tablicy którą będę sumował
def hetman_problem_sum_of_cords(length, list_of_data, hetman_cord=[], begin_i=0, begin_j=0): # w hetman_cord będę trzymał kordy jako tuple ustawionych już hetmanów 
    hetman_cord = list(find_hetman(length, hetman_cord, begin_i , begin_j)) # ustawiłem i, j jako warto w parametrach bo do rekurencji będę potrzebował ich aby poprawnie działała
    if not sum_of_values(hetman_cord, list_of_data): # jeśli suma będzie równa 0 to zakończony wkońcu algorytm
        print(f'Znaleziono zgodnego ułożenia do sumy 0 dla hetmanów:{hetman_cord}')
    elif hetman_cord[0][0] == 0 and hetman_cord[0][1] == length-1: # jeśli dojdę do ostatniej kolumny pierwszego wiersza: wtedy już nie znajdę kolejnego ułożenia hetmanów
        return print('Nie znaleziono zgodnego ułożenia do sumy 0')
    else:
        hetman_problem_sum_of_cords(length, list_of_data, [(hetman_cord[0][0], hetman_cord[0][1]+1)], 1, 0) # <- ten dziwoląg to utworzyłem nowego hetman_corda ze starego biorąc wartości z pierwszego ułożonego hetmana, z kolumną powiększoną o 1, i chyba tak musiałem zrobić, bo tuple jest nie mutowalny
                                                                                                      #tutaj przeskakuję już od razu do drugiego wiersza, i od niego zaczynam szukanie nowego hetmana

def hetman_problem():
    length = 8 
    list_of_data = create_random_number_list() # z niej będę wyciągał elementy
    hetman_problem_sum_of_cords(length, list_of_data)
    # muszę obskoczyć wstawianie hetmanów rekurencyjnie
    
    # gdy znajdę tych ośmiu hetmanów, muszę oblecieć i posprawdzać czy suma wartości z tablicy pod ich kordami wynosi 0 
    # if not sum_of_values(hetman_cord, list_of_data): 
    #     # jeśli nie będzie równa 0 , to będę szukał nowego ustawienia hetmanów, a pierwszym w tym ustawieniu będzie pierwszy ze starego ustawienia z inkrementowaną kolumną o 1
    #     hetman_cord = [0]
    #     hetman_cord = list(find_hetman(length, hetman_cord[0], hetman_cord[0][0] ,hetman_cord[0][1]+1))# <- dwa ostatnie parametry to wartości wiersza, i kolumny z pierwszego hetmana

hetman_problem()
    











# SEARCH FOR FIRST's Hetmans in chess table without recursion <-- MY FIRST IDEA
def hetman_problem1(chess_table, cord_of_hetman):
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
                
# hetman_problem1(create_chess_table(),[])

