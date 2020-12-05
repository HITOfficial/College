# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby.
#  Można założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej. Przykład:
#  60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

from threading import local
from sympy import isprime


def primes(number):
    primes_set = set()
    i = 2
    
    while int(number**(1/2)) >= i:
        if isprime(i) and number%i == 0:
            primes_set.add(i) 
        if len(primes_set) == 20:
            return list(primes_set)
        i += 1

    return list(primes_set)


def prime_mul_combination(number):
    combination_sum = [0]

    def multiply_combination(list_of_el,i=0, used_el_mul = 1):
        if i == len(list_of_el):
            if used_el_mul != 1: # gdy zabierze jakiś element
                combination_sum[0] += used_el_mul

        else:
            multiply_combination(list_of_el, i+1, used_el_mul * list_of_el[i]) # biorę element
            multiply_combination(list_of_el, i+1, used_el_mul) # nie biorę elementu

    multiply_combination(primes(number))

    return combination_sum[0] if combination_sum[0] != 0 else number

print(prime_mul_combination(60))


