# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego

# skoczek szachowy porusza się L'ką -> (2 i, 1j), (1i, 2j)

from zad3 import two_dim_list

# gdy skoczek był na polu -> True, gdy go nie odwiedził -> False
def chess_jumper_moves(n=3, start=(0,0)):
    list_to_fill = [[False for _ in range(n)] for _ in range(n)] # utworzę listę False którą będę nadpisywał na True, jesli na tym polu był już skoczek
    # nie przyjmuję za argument listy tylko jest ona zewnętrzna, żeby nie mieć kolizji w środku
    def chess_jumper(actual_cord):
        i = actual_cord[0]
        j = actual_cord[1]

        #góra
        if i-2 >= 0:
            if j-1 >= 0 and list_to_fill[i-2][j-1] == False:
                list_to_fill[i-2][j-1] = True # kładę na niej skoczka
                chess_jumper((i-2,j-1))
            if j+1 < n and list_to_fill[i-2][j+1] == False:
                list_to_fill[i-2][j+1] = True
                chess_jumper((i-2,j+1))

        #dół
        if i+2 < n:
            if j-1 >= 0 and list_to_fill[i+2][j-1] == False:
                list_to_fill[i-2][j-1] = True # kładę na niej skoczka
                chess_jumper((i+2,j-1))
            if j+1 < n and list_to_fill[i+2][j+1] == False:
                list_to_fill[i+2][j+1] = True
                chess_jumper((i+2,j+1))
        
        #lewo
        if j-2 >= 0:
            if i-1 >= 0 and list_to_fill[i-1][j-2] == False:
                list_to_fill[i-1][j-2] = True # kładę na niej skoczka
                chess_jumper((i-1,j-2))
            if i+1 < n and list_to_fill[i+1][j-2] == False:
                list_to_fill[i+1][j-2] = True
                chess_jumper((i+1,j-2))

        #prawo
        if j+2 < n:
            if i-1 >= 0 and list_to_fill[i-1][j+2] == False:
                list_to_fill[i-1][j-2] = True # kładę na niej skoczka
                chess_jumper((i-1,j+2))
            if i+1 < n and list_to_fill[i+1][j+2] == False:
                list_to_fill[i+1][j+2] = True
                chess_jumper((i+1,j+2))


    chess_jumper(start)

    return list_to_fill
chess_jumper_moves()