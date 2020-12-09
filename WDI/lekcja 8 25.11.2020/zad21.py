# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool
from random import randint
n= 4
t = [[randint(1,30) for _ in range(n)] for _ in range(n)] # tablica testowa


def different_rows_columns(used_list):
    for i1 in range(len(used_list)-1):
        for i2 in range(i1+1, len(used_list)):
            if used_list[i1][0] == used_list[i2][0] or used_list[i1][1] == used_list[i2][1]:
                return False
    return True


def check_if_make_sum(list_of_elements ,sum_to_find, i=-1, actual_sum=0, used_list=[]):
    if different_rows_columns(used_list) and sum_to_find == actual_sum:
        print(used_list)
        return True
    for new_i in range(i+1, len(list_of_elements)):
        for new_j in range(len(list_of_elements)):
            x = check_if_make_sum(list_of_elements, sum_to_find, new_i, actual_sum + list_of_elements[new_i][new_j], [*used_list, (new_i, new_j)])
            if x:
                return True

    return False


print(check_if_make_sum(t, 30))
