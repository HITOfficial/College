# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu rosnącego.
from random import randint


def list_to_check(start_index, n_list, longest_array):
    long_of_actual_array = 0
    
    for i in range(start_index, len(n_list)):
        if n_list[i] > n_list[i-1]:
            long_of_actual_array += 1            
        else:
            break

    if long_of_actual_array > longest_array:
        return long_of_actual_array
    else:
         return 0

def zad9(n):
    n_list = [randint(1,n) for _ in range(n)]
    longest_array = 0

    for i in range(1,len(n_list)): # lece od drugiego elementu, bo porownuje z poprzednim elementem w funckji
        if longest_array < list_to_check(i, n_list, longest_array):
            longest_array = list_to_check(i, n_list, longest_array)

    print(f'najdluzszy podciag rosnacy wynosi: {longest_array}')

zad9(1000)

