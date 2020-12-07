# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników


def first_digit(number):
    single_digit = 0
    while number > 0:
        single_digit = number % 10
        number //= 10
    return single_digit


def move_king(list_of_fields, w, k, actual_val):
    if w < len(list_of_fields) and w >= 0 and k < len(list_of_fields) and k >= 0:
        last_digit_actual = actual_val % 10
        if first_digit(list_of_fields[w][k]) > last_digit_actual: # pierwsza cyfra z nowej większa od ostatniej z dotychczasowej
            return True
    else:
        False


def move_king_recursion(list_of_fields, w=0, k=0, end_w=4, end_k=4): # tablica do przejscia, miejsce rozpoczęcia króla, miejsce do którego ma dojść król
    king_moves_to_exercise =[(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    if w == end_w and k == end_k:
        return True
    
    for i, j in king_moves_to_exercise:
        new_w = i + w
        new_k = j + k
        # warunek, aby się zbliżać do miejsca końcowego
        if (abs(end_w - new_w) + abs(end_k - new_k)) <= abs(end_w - w) + abs(end_k - k) and \
            move_king(list_of_fields, new_w, new_k, list_of_fields[w][k]):
            return move_king_recursion(list_of_fields, new_w, new_k, end_w, end_k)


T = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
    ]

print(move_king_recursion(T,4,0,0,4))