# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu geometrycznego.


# # modivicated exercise 10

# tylko dla q należących do  Naturalnych dodatnich

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


def zad11(n):
    n_list = [randint(1, 1000) for _ in range(1, n)]
    longest_array = 0
    for q in range(1,n):

        for i in range(len(n_list)):
            if longest_array < difference(n_list, longest_array, i, q):
                longest_array = difference(n_list, longest_array, i, q)

    print(longest_array)    
            
zad11(100)