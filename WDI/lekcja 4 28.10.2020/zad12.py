# Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę 
# pomiędzy długością najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy,
# a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu,
# że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.

from random import randint


def difference(n_list, longest_array, starting_index, q):
    count_array = 1 
    number_to_use = n_list[starting_index]
    for i in range(starting_index, len(n_list)):
        if number_to_use * q == n_list[i]: 
            count_array += 1
            number_to_use = n_list[i]

    if count_array > longest_array:
        return count_array
    else: 
        return longest_array


def zad12(n):
    n_list = [randint(1,99) for _ in range(n)]
    # na podstawie zad 10 gdzie zrobiłem ciąg aryt rosnacy zmodyfikuje i powinno być git
    # jedyna modyfikacja to tak naprawdę na raz będę leciał po dodatnim i ujemnym r 
    longest_plus_array = 0
    longest_minus_array = 0

    for r in range(1,99): # bo maksymalne r wynosić może 98

        for i in range(len(n_list)):
            if longest_plus_array < difference(n_list, longest_plus_array, i, r): # po dodatnich
                longest_plus_array = difference(n_list, longest_plus_array, i, r)

            if longest_plus_array < difference(n_list, longest_plus_array, i, -r): # po ujemnych więc tylko dorzucam minus przed zmienną
                longest_plus_array = difference(n_list, longest_plus_array, i, -r)


    return abs(longest_plus_array - longest_minus_array) # wrzucam w abs   bo ujemnych moze byc wiecej niz dodatnich

print(zad12(100))