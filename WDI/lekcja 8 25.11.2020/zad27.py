# Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
# napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
# na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
from random import randint

n = 20
t= [(randint(1,70), randint(1,70), randint(1,70), randint(1,70)) for _ in range(40)]


def squares_area(squares, squares_index):
    area_sum = 0
    for square in squares_index:
        area_sum += abs(squares[square][0] - squares[square][1]) ** 2

    return area_sum


def colision(squares, squares_index, new_square_index):
    a1 = squares[new_square_index][0]
    a2 = squares[new_square_index][1]
    b1 = squares[new_square_index][2]
    b2 = squares[new_square_index][3]

    for i in squares_index:
        x1 = squares[i][0]
        x2 = squares[i][1]
        y1 = squares[i][2]
        y2 = squares[i][3]

        # kolizja osi OX
        if (x1 <= a1 and a1 <= x2) or (x1 <= a2 and a2 <= x2)\
            and (y1 <= b1 and b1 <= y2) or (y1 <= b2 and b2 <= y2): # kolizja osi OY
            return True

    return False


def different_squares(squares, starting_index=0, squares_index=[]):
    if len(squares_index) == 13:
        if squares_area(squares, squares_index) == 2012:
            print(True)
            exit()

        return False
    for i in range(starting_index, len(squares)):
        if not colision(squares, squares_index, i):
            different_squares(squares, i+1, [*squares_index, i])

print(different_squares(t))

