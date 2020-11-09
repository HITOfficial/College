# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi

# myslałem że zadanie jest jakieś weird, ale wychodzi na to że jest luz
from random import randint


def chess_table():
    chess_list = [[randint(1, 100) for _ in range(8)] for _ in range(8)]
    return chess_list


def longest_row_col(chess_list):
    # wstępnie zsumuję sobie każdy wiersz, i kolumnę i przypiszę je do tupla w liście (row,0,20) - (row/col, index, suma)
    # print(chess_list)

    sum_of_row_col = 16 * [0] # żeby sobie wczesniej zadeklarować długość listy, bo tak 3ba na zajęęciach to -> 0-7 rzędy, 8-15 kolumny

    for i in range(len(chess_list)): # i - wiersz, j kolumna  
        sum_of_column = 0
        sum_of_row = 0
        
        for j in range(len(chess_list)):
            sum_of_row += chess_list[i][j] # sumuje wiersze
            sum_of_column += chess_list[j][i] # sumuje kolumny

        sum_of_row_col[i] = ('ROW',i ,sum_of_row) # 0-7 będą sumy wierwszy
        sum_of_row_col[8+i] = ('COL',i ,sum_of_column) # 8-15 sumy kolumn


    sum_of_row_col.sort(key=lambda tup: tup[2], reverse=True)

    print(sum_of_row_col[0:3])

    # nie jest zrobione dokładnie bo jest łacznie z polem na którym stoi

longest_row_col(chess_table())


