# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.

# obskoczyć musi to rekurencyjnie
# koszt  poruszania się to wartość pod którą stoi król
# ilość ruchów przy każdym kolejnym się zwiększa o 1 i 7 wiersz w 7 ruchów, więc przy każdym kolejnym ruchu musi  iść i+1 a j: j-1, j, j+1 <- 3 wybory

# 
from random import randint

def two_dim_list(n=8):
    return [[randint(1,30) for _ in range(n)] for _ in range(n)]


# nie działa to idealnie, bo algorytm kalkuluje ruch tylko o 1 wprzód

def move_king(list_of_weight, actual_position, move_count, weight): # position as tuple (i,j), number of moves, weight of done moves
    i = actual_position[0] # row
    j = actual_position[1] # col
    
    moved = False
    if j-1 > 0 and list_of_weight[i][j] > list_of_weight[i][j-1]:
        moved = True
        j -= 1

    if moved and j+2 < len(list_of_weight) and list_of_weight[i][j] > list_of_weight[i][j+2]:
        j += 2 # bo gdy się cofnę o jeden, to wtedy 3 wybór, to muszę inkrementować o 2

    if moved == False and j+1 < len(list_of_weight) and list_of_weight[i][j] > list_of_weight[i][j+1]:
        j += 1 # gdy nie przemieściłem w lewo to teraz sprawdzam tylko o jedno w prawą stronę
    
    weight += list_of_weight[i][j]
    move_count += 1 # przygotowuję wartości do kolejnej rekurencji

    if move_count < 7:
        move_king(list_of_weight, (i+1,j), move_count, weight)
    else:
        return print(weight)

# print(move_king(two_dim_list(),(0,4), 0, 0))





# WSZYSTKIE MOŻLIWE RUCHY
def mv_king(list_to_use,j):
    
    list_of_weight = []

    def move_king_reccurence(list_to_use,j, i=0,weight=0): # list of weights, col, row, weight of used cords
        weight += list_to_use[i][j] # a inkrementuję na samym początku, bo mam włączyć wszystkie wagi
        if i < 7: # idę do 7 wiersza, i na nim kończę
            if j-1 > 0:
                move_king_reccurence(list_to_use, j-1, i+1, weight) # przechodzę tylko o 1 wiersz w dół
            if j+1 < len(list_to_use):
                move_king_reccurence(list_to_use, j+1, i+1, weight)

            move_king_reccurence(list_to_use, j, i+1) 
        else:
            list_of_weight.append(weight)


    move_king_reccurence(list_to_use,j)

    x = sorted(list_of_weight)
    print(x[0])

mv_king(two_dim_list(),5)