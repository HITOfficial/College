from copy import deepcopy
from random import randint
# 
def create_random_n_list(n=10): 
    n_list = [[randint(10, 70) for _ in range(n)] for _ in range(n)]
    return n_list

# Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.

# wydaje mi się że czegoś brakuje



def create_random_1_dimension_list(n=25):
    return [randint(1,600) for _ in range(n)]


def check_list(list1=create_random_1_dimension_list(), list2=create_random_1_dimension_list()):
    l1_len = len(list1)
    l2_len = len(list2)
    for i1 in range(l1_len):
        for j1 in range(i1,l1_len):
            actual_part_of_list1 = list1[i1:j1+1]
            for i2 in range(l2_len):
                for j2 in range(i2, l2_len):
                    actual_part_of_list2 = list2[i2:j2+1]
                    if len(actual_part_of_list1) + len(actual_part_of_list2) == 24 or len(list1) + len(list2) < 24: # drugi wariant, gdy obydwie list z argumentów są za krótkie 
                        sum_of_2_parts = sum(actual_part_of_list1) + sum(actual_part_of_list2)
                        number_to_pow = 2
                        pow_number = 2

                        while True: # zrobiłem zewnętrzną pętle while, żeby w jednej podnosić sobie podstawę, a w drugiej wykładnik
                            print(number_to_pow ** pow_number, sum_of_2_parts)
                            while number_to_pow ** pow_number < sum_of_2_parts: # kiedy znajdzie już taką liczbę której kwadrat jest większy od sumu to kończy szukanie kolejnych
                                if number_to_pow ** pow_number == sum_of_2_parts:
                                    return True
                                elif number_to_pow ** pow_number < sum_of_2_parts:
                                    pow_number += 1
                            else:
                                number_to_pow += 1 # else z while, do podnoszenia podstawy wykładnika
            
                            if number_to_pow ** 2 > sum_of_2_parts:
                                break
    return False

# print(check_list())


# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
# posiadał nieparzystą liczbę jedynek.

# wychodzi na to że działa

from copy import deepcopy

def count_one_in_decimal(el):
    count = 0
    while el //2 > 0:
        if el % 2:
            count += 1
        el //= 2
        
    return count


def count_odd(list_to_check):
    count_odds = 0
    count_all_numbers = 0
    for row in list_to_check:
        for single_el in row:
            if single_el % 2:
                count_odds += 1
            count_all_numbers += 1

    if count_all_numbers == count_odds:
        return True
    else:
        False


def list_with_only_odd_in_decimal(list_to_use=create_random_n_list()):
    list_as_count_one_in_binary = [[count_one_in_decimal(col) for col in row] for row in list_to_use] # konwertuję sobie na listę skonwertowane jedynki z binarki
    for el in list_as_count_one_in_binary:
        print(el)
        
    row_len = len(list_as_count_one_in_binary)
    for i in range(row_len):
        list_copy_to_row = deepcopy(list_as_count_one_in_binary) # będę operował na kopii listy, bo jest dwu wymiarowa, a listy są mutable, więc deepcopy będzie potrzebne
        del list_copy_to_row[i] # będę usuwał pierwsze rząd potem oblecę kolumny
        for col1 in range(len(list_copy_to_row)-1): # pierwsza kolumna będzie usuwana od 0 do n-1
            list_copy_to_col1 = deepcopy(list_copy_to_row) # kopia przed usunięciem pierwszej kolumny
            for row1 in range(len(list_copy_to_row)):
                del list_copy_to_col1[row1][col1]

            for col2 in range(col1, len(list_copy_to_col1)): # analogicznie postępuję z drugą kolumną
                list_copy_to_col2 = deepcopy(list_copy_to_col1)
                for row2 in range(len(list_copy_to_row)):
                    del list_copy_to_col1[row2][col1]

                if count_odd(list_copy_to_col2):
                    return True
                else:
                     continue

    return False



print(list_with_only_odd_in_decimal())

# Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
# funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
# nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
# figury była równa zero.
# Zad. 1. Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.



# Zrobiłem filtrowanie liczb pierwszych sitem Erastotenesa
def sieve_Erastotenes(list_to_filtr):
    filtr_to = len(list_to_filtr)
    for n in [2,3,5,7]:
        i = 2
        while n*i <= filtr_to: # lecę do ostatniego elementu, czyli długości tablicy do przefiltrowania
            if n*i in list_to_filtr:
                list_to_filtr[list_to_filtr.index(n*i)] = False
            i+=1
    list_to_filtr = list(filter(lambda odd: odd, list_to_filtr)) # Filtruje tylko nieparzyste

    return list_to_filtr    


def odd_numbers_to_n(n= 100):
    odd_numbers = sorted([number for number in range(2,n)])
    return sieve_Erastotenes(odd_numbers)


def are_a_multiply_of_two_odds(number_to_check_multiply_of_odds):
    odds = odd_numbers_to_n(50)
    for el1 in odds:
        for el2 in odds:
            if el1 * el2 == number_to_check_multiply_of_odds:
                return True

def create_random_n_list_one_dimension(n=10): 
    n_list = [randint(10, 160) for _ in range(n)]
    return n_list

# maską bitową objechać kombinacje: wyobry z pierwszej listy
# i pobrać dodatkową wartość z ilości elementów które są w danej kombinacji
# i potem w drugiej wybrać kombinacje maską bitową, z dodatkowym warunkiem, czy elementów wybranych z kombinacji jest tyle co w pierwszym
def parts_of_list(list1, list2):
    for maskbit1 in range(1, 2**len(list1)): # bitowo idzie od końca -> (0001),(0010)... ale u mnie będzie to szło od pierwszego el z indexu do ostatniego
        count_used_numbers1 = 0
        sum_used_numbers1 = 0
        for el1 in list1:
            if maskbit1 %2:
                sum_used_numbers1 += el1
                count_used_numbers1 += 1
            maskbit1 //= 2
        # mam potworzone kombinację sum wszystkich liczb z pierwszej listy
        for maskbit2 in range(1, 2**len(list2)):
            count_used_numbers2 = 0
            sum_used_numbers2 = 0
            for el2 in list2:
                if maskbit2 %2:
                    sum_used_numbers2 += el2
                    count_used_numbers2 += 1
                maskbit2 //= 2
                if count_used_numbers2 == count_used_numbers1: # mają być takiej samej długości podzbiory
                    sum_used_numbers = sum_used_numbers1 + sum_used_numbers2
                    if are_a_multiply_of_two_odds(sum_used_numbers): # jeśli znajdzie kombinację dwóch liczb pierwszych tworzącą tą sumę to mamy wynik do zadania
                        return True 
    return False
        

# print(parts_of_list(create_random_n_list_one_dimension(), create_random_n_list_one_dimension()))


# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy był wielokrotnością
# (co najmniej dwukrotnością) kwadratu dowolnej liczby naturalne większej od 1.


# CHYBA DZIAŁA POPRAWNIE 
import copy # potrzebuję robić głębokie kopie bo, bo w listach zawieram kolejne listy


    

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
        
        for col1 in range(len(list_copy)): # kombinacje z usunięcia pierwszej kolumny
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
                
              
# able_to_remove(create_random_n_list(4))



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

# hetman_problem()
    











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

