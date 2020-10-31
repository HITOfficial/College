# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami
# naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

from random import randint

# zrobilem na same dodatnie, bo dla ujemnych wystarczy podmienic
def difference(n_list, longest_array, starting_index, r):
    count_array = 1 # bo sam z soba element tez jest ciagiem
    number_to_use = n_list[starting_index]
    for i in range(starting_index, len(n_list)):
        # porownuje pierwszy z kazdym kolejnym elementem w liscie, tzn nie cofam sie do tylu juz
        if number_to_use + r == n_list[i]: # gdy znajdzie kolejny o podanej roznicy 
            count_array += 1
            number_to_use = n_list[i] # element z ktorym beda przyrownywane liczby nadpisuje na kolejny z ciagu arytmentycznego

    if count_array > longest_array:
        return count_array
    else: 
        return longest_array


def zad10(n):
    n_list = [randint(1, 1000) for _ in range(1, n)]
    # na pierwszy rzut oka bedzie bardzo nie wydajna
    # biore elemement pierwszy z listy i bede lecial pierw nadluzszy podciag rosnacy potem malejacy
    # na poczatek ten pierwszy element dodaje 2, 3 ... az do n wstepnie i sprawdzam czy jest rowny innemu elementowi z tablicy
    # a2 = a1 + r
    # an = a1 +(n-1)*r 
    longest_array = 0 # bo sam z soba element tez jest ciagiem
    # i nie moge sie cofac w ciagu (tak zakladam)
    for r in range(1,n): # jest idealnie roznica na caly zasieg liczb

        for i in range(len(n_list)):
            if longest_array < difference(n_list, longest_array, i, r):
                longest_array = difference(n_list, longest_array, i, r)

    print(longest_array)    
            
zad10(100)
