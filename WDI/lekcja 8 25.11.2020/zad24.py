# Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru
from random import uniform
from math import sqrt

n = 2
t = [(uniform(1, 3), uniform(1,3)) for _ in range(n) for _ in range(n)]
print(t)

def gravity_center(list_of_cords):
    x = 0
    y = 0
    list_len = len(list_of_cords)
    for i, j in list_of_cords:
        x += i
        y += j
    return ((x / list_len), (y / list_len)) # zwracam sume elementow na danym wymiarze / ilosc elementow jako tupla

# zrobiłem zewnętrzną funkcję w której będę przetrzymywał najmniejszą wartość
def lowest_distance(list_of_cords):
    gravity_lowest_difference = [1000]  

    def take_cords(list_of_cords, i=-1, subset1=[], subset2=[]):
        if len(subset1) != 0  and len(subset2) != 0:
            gravity_1 = gravity_center(subset1)
            gravity_2 = gravity_center(subset2)
            gravity_difference = abs(sqrt(pow(gravity_1[0] - gravity_2[0],2) + pow(gravity_1[1] - gravity_2[1],2))) # sqrt(pow(x1-x2) + pow(y1-y2)) 
            gravity_lowest_difference[0] = min(gravity_lowest_difference[0], gravity_difference)

        if i < len(list_of_cords) -1:
            take_cords(list_of_cords, i+1, [*subset1, list_of_cords[i+1]], [*subset2]) # daje punkt do pierwszego
            take_cords(list_of_cords, i+1, [*subset1], [*subset2, list_of_cords[i+1]]) # drugiego
            take_cords(list_of_cords, i+1, [*subset1], [*subset2]) # pomijam aktualny punkt
    take_cords(list_of_cords)
     
    return gravity_lowest_difference[0]


print(lowest_distance(t))
