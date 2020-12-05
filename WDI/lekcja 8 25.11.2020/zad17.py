# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.

from sympy import isprime
from math import ceil, log10

def list_of_single_numbers(number):
    number_length = ceil(log10(number)) # długość cyfry w systemie dziesiętnym
    numbers_list = [0] * number_length # deklaruję ilość elementów w składzie liczby

    for i in range(number_length-1, -1, -1): # żeby nie korzystać z reversed, to nadpisuję od końca
        numbers_list[i] = number%10
        number //= 10
        
    return numbers_list


def combine_numbers_from_list(list_to_combine):
    power = 1
    combined_number = 0
    for i in range(len(list_to_combine)):
        combined_number += list_to_combine[i] * (10 ** (len(list_to_combine) - power)) # nie chcę odwróconej liczby dlatego, lecę na odwrót z potęgą
        power += 1 

    return combined_number


def primes_sum_of_consistent_substrings(number1, number2):
    count_primes = [0] # nw czy jest to dobre, ale global jedynie wiem jak pobrać wewnątrz funkcji, ewentualnie mutable elementy wykrywa więc w przetrzymuje w tablicy, a nie chcę tworzyć zmiennej globalnej
    number1_list = list_of_single_numbers(number1)
    number2_list = list_of_single_numbers(number2)

    def regular_combination_of_two_substrings(number1_list, number2_list, i1=-1, i2=-1, combination_numbers_list =[]): # pierwsza z liczb jako lista, druga, indexy użyte, kombinacja użytych liczb jako lista
        if i1 == len(number1_list)-1 and i2 == len(number2_list)-1:
            if isprime(combine_numbers_from_list(combination_numbers_list)):
                count_primes[0] += 1
                
        else:
            if i1 <= len(number1_list) -2: # warunek żeby nie wyskoczyć poza zasięg listy
                regular_combination_of_two_substrings(number1_list, number2_list, i1 +1, i2, [*combination_numbers_list, number1_list[i1+1]]) # dwie możliwości, albo dodaję liczbę z pierwszej, albo z drugiej
            if i2 <= len(number2_list) -2:
                regular_combination_of_two_substrings(number1_list, number2_list, i1, i2+1, [*combination_numbers_list, number2_list[i2+1]])

    regular_combination_of_two_substrings(number1_list, number2_list)

    return count_primes[0]


print(primes_sum_of_consistent_substrings(123,23))





