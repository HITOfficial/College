# Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę napisać funkcję,
#  która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie jego elementów 
# każdy czynniki pierwszy występuje co najwyżej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5

from random import randint
from math import log10, ceil # bo przy okazji będę zaokrąglać w górę logarytm z liczby aby sprawdzić jak długa ona jest w systemie DEC

def zad20(n):
    n_list = [randint(1,1000) for _ in range(n)]
    print(n_list)
    # interuję po wszystkich elementach listy, i w środku dodatkowo lecę log(liczba, 10) żeby sprawdzić ile cyfr ma liczba, a potem w srodku daje dodatkową zmienną, która trzyma ilosc nieparzystych cyfr juz w tej liczbie

    for el in n_list:
        odd_counter = 0 # zmienna która mi powie, czy liczba jest parzysta

        for _ in range(ceil(log10(el))):
            if (el % 10) % 2 == 1:
                odd_counter += 1
            print(el % 10)
            el //= 10



zad20(5)
