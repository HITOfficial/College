# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16

# oblece sobie funkcję i będę robił: liczba mod 2^16 

number_to_convert = 435209


def convert_oct(number):
    number_oct = 0
    power = 0
    while number > 0:
        # number_oct = number_oct + number % 2**3 * 10 ** power
        number_oct = number_oct + (number % 2**16) * 10 ** power # pluło jadem bo kolejność w potęgowaniu
        number  //= 2**16
        power += 1

    return number_oct

print(convert_oct(number_to_convert))




# FROM College

import math

def convert(number, base):
    hex = '0123456789ABCDEF'
    list_of_vals = [0 for el in range(math.ceil(math.log(number, base))) +1] # declaration pokaże nam długość cyfry
    i = 0   # spoko tip z log(liczba, podstawa)

    while number > 0:
        list_of_vals[i] = number % base
        number //= base
        i += 1 

    for j in list_of_vals[::-1]: # bo jest odwrócone
        print(hex[j], end ='')



convert(255432235,16)
