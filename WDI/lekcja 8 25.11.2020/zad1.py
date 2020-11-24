# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry
from math import ceil, log10

def is_primary(number):
    if number == 2 or number == 3:
        return True
    elif number <= 1 or number %2 == 0 or number %3 == 0:
        return False

    i = 5
    while i <= number**(1/2):
        if number %i == 0:
            return False
        i += 2
        if number %i ==0:
            return False
        i+= 4

    return True

# sposób bez rekurencji
def part_is_primary(number):
    number_len = ceil(log10(number))

    for i in range(1,2**number_len-1): # zeby nie otrzymać maski 1111 <- kombinacja z wszystkich liczb
        number_copy = number
        power = 0
        part_of_number = 0

        while i > 0:
            if i%2:
                part_of_number += (10 ** power) * (number_copy %10)
                power +=1 
            number_copy //= 10
            i //= 2

        if part_of_number >= 10 and is_primary(part_of_number):
            print(part_of_number)

print(part_is_primary(516732))


# zrobię maską bitową wycinanie kawałków liczby, oraz dorzucę dodatkowy warunek który będzie sprawdzał, czy wycięty kawałem jest liczbą przynajmniej 2 cyfrową
