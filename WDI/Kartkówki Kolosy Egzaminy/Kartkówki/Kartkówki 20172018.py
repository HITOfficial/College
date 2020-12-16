# Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeªniona liczbami naturalnymi. Na szachownicy
# znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
# zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
# poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
# Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi.

from random import randint

t = [[randint(1,10) for _ in range(8)] for _ in range(8)]


# szachuje pola bez tego na którym stoi

def checked_list_sum(t, i, j, actualy_checked_list): # lista, wiersz i kolumna na której stoi wieża 
    checked_sum = 0

    for k in range(len(t)):
        if actualy_checked_list[i][k] == False and j != k :
            checked_sum += t[i][k]
            actualy_checked_list[i][k] = True

        if actualy_checked_list[k][j] == False and i != k:
            checked_sum += t[k][j]
            actualy_checked_list[k][j] = True

    return checked_sum


def false_list(t):
    return [[False for _ in range(len(t))] for _ in range(len(t))]


def is_posible_to_move_rooks(t,r1, r2): # list of fields, rook1(x,y), rook2(x,y)
    checked_list = false_list(t)
    rook_checked_sum =  checked_list_sum(t, r1[0], r1[1], checked_list) + checked_list_sum(t, r2[0], r2[1], checked_list) # referencja na tablicy, więc jej nie muszę zwracać

    for i in range(len(t)):
        for j in range(len(t)):
            rook1_checked = false_list(t)
            rook1_checked_sum = checked_list_sum(t, i, j, rook1_checked) # ustawiam pierwszą wierzę 
            for k in range(len(t)):
                for l in range(len(t)):
                    rook2_checked = rook1_checked.copy() # robię kopię szachowanych pól przez pierwszą wierzę
                    rook2_checked_sum = checked_list_sum(t, k, l, rook2_checked)

                    if rook1_checked_sum + rook2_checked_sum > rook_checked_sum:
                        return True

    return False

print(is_posible_to_move_rooks(t, (1,1), (2,3)))
