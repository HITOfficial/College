# . W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika


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


def move_king_recursion(list_of_fields, w=0, k=0):
    king_moves_to_exercise =[(0,1), (1,1), (1,0), (1,-1)]
    if w == len(list_of_fields) -1 and k == len(list_of_fields) -1:
        print('True')
    
    for i, j in king_moves_to_exercise:
        new_w = i + w
        new_k = j + k
        if move_king(list_of_fields, new_w, new_k, list_of_fields[w][k]):
            move_king_recursion(list_of_fields, new_w, new_k)


T = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
    ]

print(move_king_recursion(T))