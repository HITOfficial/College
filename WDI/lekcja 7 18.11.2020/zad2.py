# Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
# o 2 niewiadomych.


from zad1 import *

# na pierwszy rzut oka przychodzi mi metoda wyznaczników a dokładniej metoda Cramera

# mniej więcej coś takiego
#  x y  w
# |1 5 7| 
# |2 3 8|

def w(list_to_use):
    return (
        list_to_use[0][0][0] * list_to_use[1][1][0] - list_to_use[0][1][0] * list_to_use[1][0][0],\
        list_to_use[0][0][1] * list_to_use[1][1][1] - list_to_use[0][1][1] * list_to_use[1][0][1]
        )


def wx(list_to_use):
    return (
        list_to_use[0][1][0] * list_to_use[1][2][0] - list_to_use[0][2][0] * list_to_use[1][1][0],\
        list_to_use[0][1][1] * list_to_use[1][2][1] - list_to_use[0][2][1] * list_to_use[1][1][1]
    )


def wy(list_to_use):
    return (
        list_to_use[0][0][0] * list_to_use[1][2][0] - list_to_use[0][2][0] * list_to_use[1][0][0],\
        list_to_use[0][0][0] * list_to_use[1][2][0] - list_to_use[0][2][0] * list_to_use[1][0][0]
    )


data_list = [
    [(1,2),(2,3),(1,10)],
    [(5,4),(7,3),(1,4)]
]


print (f'x = {divide_irrational(wx(data_list),w(data_list))}')
print (f'y = {divide_irrational(wy(data_list),w(data_list))}')
