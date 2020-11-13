# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
# będących liczbami pierwszymi?
from math import sqrt, log10, ceil
from random import randint


def random_2_dimensions_list(n=2):
    random_list = [[randint(2,50) for _ in range(n)] for _ in range(n)]
    return random_list
    

def is_primary(n): # poprawnie zdefiniowana funkcja sprawdzająca, czy liczba jest pierwsza
    if n == 2 or n == 3:
        return True
    elif n <= 1 or  n%2 == 0 or n%3 == 0:
        return False

    j = 5 
    while j <= sqrt(n):
        if n % j == 0:
            return False
        j += 2
        if n%j == 0:
            return False
        j += 4

    return True


def every_row_has_primary_col(list_to_search):
    for i in range(len(list_to_search)):
        for j in range(len(list_to_search[i])):
            count_primary_numbers = 0
            number_copy = list_to_search[i][j]
            while number_copy > 0:
                if is_primary(number_copy%10):
                    count_primary_numbers += 1
                number_copy //= 10

            if count_primary_numbers == ceil(log10(list_to_search[i][j])):
                return True

    return False


print(every_row_has_primary_col(random_2_dimensions_list()))

    