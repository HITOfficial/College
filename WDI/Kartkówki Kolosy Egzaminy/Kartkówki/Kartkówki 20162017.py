# Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
# A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
# możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
# Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
# napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
# są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
# znalezionych par.



def NWD(a, b):
    while b != 0:
        b, a = a % b, b
    return a     

def two_subset_combination(N, A=0, B=0, power_A =0, power_B =0):
    count = 0
    if N == 0:
        if A !=0 and B !=0:
            if NWD(A, B) == 1:
                print(A, B)
                return 1
    else:
        count += two_subset_combination(N//10, A +  N%10 * (10**power_A), B, power_A +1, power_B)
        count += two_subset_combination(N//10, A, B + N%10 * (10**power_B) , power_A, power_B+1)
    return count


# print(two_subset_combination(75984))


# Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
# funkcja powinna zwrócić położenie wież.

from copy import deepcopy

from random import randint, seed
seed(69)
t = [[randint(1,10) for _ in range(3)] for _ in range(3)]


def false_list(t):
    return [[False for _ in range(len(t))] for _ in range(len(t))]


def checked_sum_by_rook(t, i, j, checked_list):
    checked_sum = 0

    for k in range(len(t)):
        if checked_list[i][k] == False and k != j:
            checked_sum += t[i][k]
            checked_list[i][k] = True

        if checked_list[k][j] == False and k != i:
            checked_sum += t[k][j]
            checked_list[k][j] = True

    return checked_sum


def biggest_2_rooks_sum(t):
    rook1 = (0,0) # pozycja wierzy 1
    rook2 = (0,0) # pozycja wierzy 1
    rook_biggest_sum = 0
    
    for i in range(len(t)):
        for j in range(len(t)):
            rook1_checked = false_list(t)
            rook1_sum = checked_sum_by_rook(t, i, j, rook1_checked)
        
            for k in range(len(t)):
                for l in range(len(t)):
                    rook2_checked= deepcopy(rook1_checked)
                    rook2_sum = checked_sum_by_rook(t,k, l, rook2_checked)

                    if rook_biggest_sum < rook1_sum + rook2_sum and i != k and j != l:
                        rook1 = (i,j)
                        rook2 = (k,l)
                        rook_biggest_sum = rook1_sum + rook2_sum

    return rook1, rook2, rook_biggest_sum

# print(biggest_2_rooks_sum(t))