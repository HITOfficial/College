# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.

# skoczek (2,1), (1,2) <- o tyle się przemieszcza

from random import randint


def multiply_is_equal(number1, number2, multiply_value):
    if number1 * number2 == multiply_value:
        return True
    return False

def random_2_dimensions_list(n=10):
    random_list = [[randint(1,50) for _ in range(n)] for _ in range(n)]
    return random_list


def search_for_multiply_in_list(multiply_value,list_to_search):
    multiply_list = [] # <- do tej listy będę appendował tuple zawierające kordy dobrych wartości
    i_len = len(list_to_search)
    j_len = len(list_to_search[0]) # wymiary są kwadratami więc każdy rząd jest tej samej długości
    print(list_to_search[2][2])
    for i in range(i_len):
        for j in range(j_len):
            i_copy = i
            j_copy = j
            
            # Tworzę możliwe ruchy skoczka
            # LEWO PRAWO
            if j_copy + 2 < j_len-1: # bo indexowanie od 0 się zaczyna
                if i_copy - 1 >= 0:
                    if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy-1][j_copy+2], multiply_value):
                        multiply_list.append(((i,j),(i_copy-1,j_copy+2),(list_to_search[i][j],list_to_search[i_copy-1][j_copy+2]))) # zapisuję kordy oraz wartości które dały ten iloczyn
                if i_copy + 1 < i_len-1:
                    if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy+1][j_copy+2], multiply_value):
                        multiply_list.append(((i,j),(i_copy+1,j_copy+2),(list_to_search[i][j],list_to_search[i_copy+1][j_copy+2])))
            if j_copy - 2 >= 0:
                if i_copy - 1 >= 0:
                    if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy-1][j_copy-2], multiply_value):
                        multiply_list.append(((i,j),(i_copy-1,j_copy-2),(list_to_search[i][j],list_to_search[i_copy-1][j_copy-2])))
                if i_copy + 1 < i_len-1:
                    if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy+1][j_copy-2], multiply_value):
                        multiply_list.append(((i,j),(i_copy+1,j_copy-2),(list_to_search[i][j],list_to_search[i_copy+1][j_copy+2])))
                    
            # GÓRA DÓŁ 
            if i_copy + 2 < i_len-1:
                if j_copy - 1 >= 0:
                    if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy+2][j_copy-1], multiply_value):
                        multiply_list.append(((i,j),(i_copy+2,j_copy-1),(list_to_search[i][j],list_to_search[i_copy+2][j_copy-1])))
                if j_copy + 1 < j_len-1:
                     if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy+2][j_copy+1], multiply_value):
                            multiply_list.append(((i,j),(i_copy+2,j_copy+1),(list_to_search[i][j],list_to_search[i_copy+2][j_copy+1])))
            if i_copy - 2 >= 0:
                if j_copy - 1 >= 0:
                     if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy-2][j_copy-1], multiply_value):
                            multiply_list.append(((i,j),(i_copy-2,j_copy-1),(list_to_search[i][j],list_to_search[i_copy-2][j_copy-1])))
                if j_copy + 1 < j_len-1:
                     if multiply_is_equal(list_to_search[i][j],list_to_search[i_copy-2][j_copy+1], multiply_value):
                            multiply_list.append(((i,j),(i_copy-2,j_copy+1),(list_to_search[i][j],list_to_search[i_copy-2][j_copy+1])))
            
    return multiply_list    

print(search_for_multiply_in_list(15,random_2_dimensions_list()))