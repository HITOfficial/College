# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

from zad1 import is_primary


# mam zrobić 3 podzbiory
# np 0 <- nie ma czynników pierwszych, powinnien to być pewniak 
#    1 <- 1 el pierwszy w rozkładzie
#    2 <- przykładowo

# 64 -> 2 * 32, i tylko raz można uwzględnić dany czynnik
# 30 -> 2 * 15, 3 * 10, 5 * 6
# na to wychodzi że ten czynnik pierwszy może być maxymalnie równy (1/2)n

def count_primary(number): # <- brzydki sposób
    count = 0
    for i in range(2,(number//2)+1):
        if is_primary(i) and number %i == 0:
            count += 1
    return count # tutaj zliczam l pierwsze w czynnikach


list_use = [1,432,354,476,324,312]

# seta zrobię który będzie przechowywał różne wagi
def weight_of_elements(list_to_use):
    set_of_weight = set()
    for el in list_to_use: # set sobie będzie nadpisywał elementy o tej samej wadze, ale to w sumie dobrze, bo liczy się tylko, czy po iteracji po wszystkich el czy będzie set nadal długości 3
        set_of_weight.add(count_primary(el))

    return True if len(set_of_weight) == 3 else False

print(weight_of_elements(list_use))


