# Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający
# czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste

from random import randint
# na WDI ostatnio mowili o sprawdzanie dlugosci liczby w danym systemie poprzez log(liczba, podstawa)
from math import log, ceil # przez ceil zaookragle sobie w gore


def zad7():
    odd_list = [randint(1, 1001) for _ in range(1000)]
    print(odd_list)
    odd_counter = 0
    for el in odd_list:
        number_count = ceil(log(el, 10))
        odd_numbers = 0
        el_tmp = el

        # obleciec sobie po przystkich elementach z danej liczby i sprawdzic czy kazda jest parzysta
        for _ in range(number_count):
            if (el_tmp % 10) % 2 == 1: # dziele od konca tak jak na lekcach i sprawdzam czy ostatnia cyfra jest nieparzysta
                odd_numbers += 1 
            el_tmp //= 10
        if odd_numbers == number_count and odd_numbers != 0: # sprawdzam czy liczba cyfr niaprzystych w liczbie jest rowna dlugosci liczby
            odd_counter += 1
    
    return f'ilosc cyfr nieparzystych wynosi: {odd_counter}'

print(zad7())



