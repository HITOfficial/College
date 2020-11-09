# Zadanie 1.
# Dwie liczby naturalne s¡ ró»nocyfrowe, je»eli nie posiadaj¡ »adnej wspólnej cyfry. Prosz¦ napisa¢ program,
# który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie 2-16), w którym
# liczby s¡ ró»nocyfrowe. Program powinien wypisa¢ znalezion¡ podstaw¦; je»eli podstawa taka nie istnieje,
# nale»y wypisa¢ komunikat o jej braku.
# Na przykªad: dla liczb 123 i 522 odpowiedzi¡ jest podstawa 11, bo 123(10) = 102(11) i 522(10) = 435(11)

from math import log, ceil

def convert_number(number, system):
    len_in_system = ceil(log(number, system)) # konwersja na system
    number_in_system = len_in_system * [0] 
    
    for i in range(len_in_system):
         number_in_system[i] = number % system
         number //= system

    return number_in_system[::-1]

def zad1(number1, number2):
    for i in range(2,17): # wszystkie elementy się mają różnić
        number1_converted = convert_number(number1, i)
        for j in range(2,17):
            number2_converted = convert_number(number2, j)
            numbers_equal = False

            for el1 in number1_converted:
                if numbers_equal: 
                    break

                for el2 in number2_converted:
                    if el1 == el2:
                        numbers_equal = True
                        break

            if not numbers_equal:
                return print(f'{number1} ({i}), {number2} ({j}) ')
    return print('takie liczby nie istnieją')

zad1(123, 501)


# Zadanie 2. Dane s¡ deklaracje:
# const int N=1000;
# int tab[N];
# Tablica tab jest wypeªniona liczbami naturalnymi. Prosz¦ napisa¢ funkcj¦, która zwraca dªugo±¢ najdªu»szego
# spójnego podci¡gu rosn¡cego, dla którego suma jego elementów jest równa sumie indeksów tych elementów.
# Do funkcji nale»y przekaza¢ tablic¦, funkcja powinna zwróci¢ dªugo±¢ znalezionego podci¡gu, lub warto±¢ 0,
# je»eli taki podci¡g nie istnieje.

from random import randint

def generate_list():
    random_number_list = [randint(1,1000) for _ in range(1000)]
    return random_number_list
    
    
def longest_part(tuple_with_data, start, list_to_use):
    #najdłuższy spójny podciąg
    index_sum = 0
    if start+1 < len(list_to_use):
        for i in range(start+1,len(list_to_use)): # bo porównuje z poprzednim to muszę zaczynać od id-1
            if list_to_use[i-1] < list_to_use[i] and i == list_to_use[i]: # jezeli poprzedni mniejszy od następnego i wartość pod indexem i jest równa temu indexowi
                index_sum += i
                if index_sum > tuple_with_data[2]:
                    tuple_with_data = (start,i,index_sum)
            else:
                longest_part(tuple_with_data, start+1, list_to_use)        
    else: 
        return tuple_with_data


def growing_part_of_list(list_to_use):    
    actual_the_best_tuple = (0,0,0) # tuple(start,end,sum) on jest dodatkowo, aby w razie nowego lepszego wyniku 
    if(actual_the_best_tuple <= longest_part(actual_the_best_tuple,0, list_to_use):
        actual_the_best_tuple = longest_part(actual_the_best_tuple,0, list_to_use)
        return print(list_to_use[[actual_the_best_tuple[0]:[actual_the_best_tuple[1]])
    else:
        return print('nie znaleziono takiego podciągu')









