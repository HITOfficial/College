# Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeªniona liczbami naturalnymi. Na szachownicy
# znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
# zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
# poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
# Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi.

from random import randint, seed
import re
from sympy import isprime

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

# print(is_posible_to_move_rooks(t, (1,1), (2,3)))


# Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
# 1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
# 2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
# Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
# który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.

# bez powrotów

def condition1(t):
    for i in range(1,len(t)):
        if t[i] + t[i-1] >= 2:
            continue
        else:
            return False
            
    return True


def condition2(t):
    for i in range(1,len(t)):
        if isprime(t[i]) and isprime(t[i-1]):
            return False

    return True


t=9*[0]
t[0] = 1
def find_list(t,index=1):
    if index == len(t):
        if condition1(t) and condition2(t):
            print(t)
    else:
        for i in range(len(t)):
            t.copy()
            t[index] = i+1
            find_list(t,index+1)

# find_list(t)

def c1(number1, number2):
    return True if abs(number1 + number2) >=2 else False


def c2(number1, number2):
    return True if isprime(number1) and isprime(number2) else False


def main_find_elements():
    t= 9*[0]
    t[0] = 1

    def find_list(last_val=3, index=0):
        if index == 8:
            print(t)
            return

        elif index >= 1 and not (c1(last_val, t[index]) and not c2(last_val, t[index])): # bramka not, i gdy mam przynajmniej 2 elementami wypełnione, wtedy sprawdzam warunki
            return False

        else:
            for i in range(1, len(t)+1):
                t[index+1] = i
                find_list(i, index+1)

        t[index] = 0
        return False

    find_list()


main_find_elements()


# Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
# funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
# suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
# funkcja powinna zwróci¢ warto±¢ typu bool

t = [[randint(1,10) for _ in range(8)] for _ in range(8)]

def check_chess_jumpers(t): # table
    chess_jumper_moves = [(-1,2),(1,2),(2,1),(2,-1),(1,-2)] # idę w dół żeby nie robić powtórek
    for i in range(len(t)):
        for j in range(len(t)):
            for x,y in chess_jumper_moves:
                if i+x >= 0 and i+x < len(t) and j+y >= 0 and j+y < len(t):
                    if isprime(t[i][j] + t[i+x][j+y]):
                        return True
    return False


# print(check_chess_jumpers(t))