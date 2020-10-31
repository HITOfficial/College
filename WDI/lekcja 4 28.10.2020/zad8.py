# Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
# Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

from random import randint

def zad8(n):
    list_of_n_elements = [randint(1, 1000) for _ in range(n)]
    # z list[k] -> [k+n]
    # sprawdzic czy list[k] <- czy liczba pierwsza 

    # nie rozumiem zadanie dokladnie 
