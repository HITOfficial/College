# Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
# współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
# która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n<k oraz n jest wielokrotnością liczby
# 3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
# należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
# wartość typu bool.

from random import uniform

n = 10
t = [(uniform(0.2,3),uniform(0.2,3)) for _ in range(n)]


def gravity_center(tuple_list):
    x_sum  = sum(map(lambda x: x[0], tuple_list)) # suma wartości x
    y_sum  = sum(map(lambda y: y[1], tuple_list)) # suma wartości y
    t_len = len(tuple_list)

    return x_sum / t_len + y_sum / t_len # x_sum / n + y_sum / n, n ilość składników


def is_subset(t, r, k, i=0, used_cords=[]): # tablica, promień, ograniczenie, index_elementu zabranego, k
    if len(used_cords) < k and i < len(t):
        if len(used_cords) > 0 and r >= gravity_center(used_cords):
            return True 
        return (
            is_subset(t, r, k, i+1, [*used_cords, t[i]]) or
            is_subset(t, r, k, i+1, [*used_cords, t[i]])
            )
    return False


def is_right_subset(t, r, k):
    if len(t) < k: # zabezpieczenie na zakrótki podzbiór
        return 'za krótki podzbiór'
    else:
        return is_subset(t, r, k) # 

print(is_right_subset(t, 3, 5))
