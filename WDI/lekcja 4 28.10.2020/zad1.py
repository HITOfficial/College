# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16

# oblece sobie funkcję i będę robił: liczba mod 2^16 

number_to_convert = 43520994032590


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
