# Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
# klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
# szachownicy, że:
# - oba klocki są prostopadle do siebie,
# - w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
# - największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.


# klocki zawsze kolejne bedą prostopadłe do siebie

def NWD(number1, number2):
    number1, number2 = abs(number1), abs(number2)
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


print(NWD(121,2))


# 2 wariant -> | __

# ustawiamy tylko dwa klocki w sumie

# 4 możliwości:
# -> __ [0][0] [0][1]
# -> || [1][0] [2][0] or [1][1][2][1]

# -> |  [0][0] [1][0]
# -> __ [0][0] [0][1] or jesli nie dotyka krawedzi lewej


def insert_domino(chess_list):
    list_len = len(chess_list)

    # poziom pion
    for i in range(list_len-2): # bo musze zrobić 2 miejsca w pionie dla drugiego domina
        for j in range(list_len-1): # bo będę kład poziomego
            domino1 = (chess_list[i][j], chess_list[i][j+1])
            domino2 = (chess_list[i+1][j], chess_list[i+2][j]) # jeden wariant
            domino3 = (chess_list[i+1][j+1], chess_list[i+2][j+2]) # drugi wariant
            if NWD(NWD(domino1[0], domino1[1]), NWD(domino2[0], domino2[1])) == 1 or NWD(NWD(domino1[0], domino1[1]), NWD(domino3[0], domino3[1])) == 1:
                return True

    for i in range(list_len-1): # zostawiam jedno miejsce na poziomego
        for j in range(list_len): # bo będę kład poziomego
            domino1 = (chess_list[i][j], chess_list[i+1][j])

            if j-1 > 0: # pierwsza część klocka z lewej strony
                domino2 = (chess_list[i+1][j-1], chess_list[i+1][j])
                if NWD(NWD(domino1[0], domino1[1]), NWD(domino2[0], domino2[1])) == 1:
                    return True
            
            if j+1 > list_len -1: # druga część klocka z prawej strony
                domino2 = (chess_list[i+1][j], chess_list[i+1][j+1])
                if NWD(NWD(domino1[0], domino1[1]), NWD(domino2[0], domino2[1])) == 1:
                    return True
                    
    return False


