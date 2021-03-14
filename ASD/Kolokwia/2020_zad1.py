# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

from random import randint
from math import log10, ceil


def number_to_list(number):
    number_as_list = [None] * ceil(log10(number))
    for i in range(len(number_as_list)-1,-1,-1): # wypełniam liczbę od końca
        number_as_list[i] = number%10
        number //= 10
    return number_as_list


def count_repeats(number_as_list):
    # trochę nie efektywne ale nie będę naruszał wymiarów tablicy, będę tylko markował pola które użyłem z powrotem na None
    digit_repeats_sum = 0
    for i in range(len(number_as_list)-1):
        digit_repeats = 1
        for j in range(i+1, len(number_as_list)):
            if j is None:
                continue
            elif number_as_list[i] is number_as_list[j]:
                digit_repeats += 1
                number_as_list[j] = None # nadpisuje wartość, żeby juz jej więcej nigdzie nie uwzględniać
        if digit_repeats > 1:
            digit_repeats_sum += digit_repeats
    return digit_repeats_sum


def quick_sort_tuple(T,start=0, end=None):
    if end is None:
        end = len(T)-1
    left = start
    right = end
    element_in_half = T[(start+end)//2][0]
    while left <= right:
        while T[left][0] < element_in_half:
            left += 1
        while T[right][0] > element_in_half:
            right -= 1
        if left <= right:
            T[left], T[right] = T[right], T[left]
            left += 1
            right -= 1
    if left < end:
        quick_sort_tuple(T, left, end)
    if right > start:
        quick_sort_tuple(T, start, right)
    return T


def pretty_sort(T): # sortuje liczby przez piękność malejąco
    for i in range(len(T)):
        number= number_to_list(T[i])
        T[i] = (count_repeats(number), T[i]) # przerobiona tablica na wartość, oraz ilość powtórzeń
    
    quick_sort_tuple(T) # sortuje tuple rosnąco

    for i in range((len(T)//2)): # dodaję +1 bo inaczej gdy lista będzie nieparzysta, środkowy element pominę i pozostanie nadal tuplem 
        T[i], T[len(T)-1-i] = T[len(T)-1-i][1], T[i][1]
    if len(T)%2 == 1:
        T[len(T)//2] = T[len(T)//2][1] # środkowy el dla nieparzystych zmieniam ręcznie bo inaczej algo się posypie
    return T



# drugi sposób używając countsort:

def points(number): # cyfry 0-9
    T = [0]*10
    while number != 0:
        T[number%10] += 1
        number //= 10
    points = 0
    for el in T:
        if el > 1:
            points -= (el+10)
        else:
            points += el
    return points


def table_with_points(T):
    T_with_points = [(points(T[i]),i) for i in range(len(T))] # punkty, index pod którym stoi
    return T_with_points


def min_max_table_tuple(T):
    min_el = T[0][0] # biorę 1wszy el
    max_el = T[0][0]
    for el,_ in T: # o 1 wiecej el w loopie
        if el < min_el:
            min_el = el
        elif el > max_el:
            max_el = el
    return min_el, max_el


def sort_wonder_table(T):
    T_points_id = table_with_points(T)
    min_el, max_el = min_max_table_tuple(T_points_id)

    T_count = [0] * (max_el-min_el+1) # +1 bo zaczynaja sie indexy od 0
    for el,_ in T_points_id: # markuje elementy ktore dodalem
        T_count[el-min_el] += 1
    for i in range(1,len(T_count)): # sumuje z poprzednim
        T_count[i] += T_count[i-1]

    T_sorted = [None]*len(T) # tablica posortowana od najmniej do najpiękniejszych
    for i in range(len(T)):
        T_sorted[T_count[T_points_id[i][0] - min_el]-1] = T[i] # indexy w tablicy od 0 dlatego -1
        T_count[T_points_id[i][0] - min_el] -= 1
    return list(reversed(T_sorted))

