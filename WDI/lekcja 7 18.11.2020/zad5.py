# Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
# [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.

# 1. prosta ma być równoległa do osi współrzędnych
#                      współczynnik kierunkowy (a) = (y2-y1/x2-x1), albo prościej y1 == y2 <- wtedy leżą na tej samej wysokości
# 2. będę znajdował dwa punkty o współczynniku kierunkowym == 0
#    nastepnie wyliczę długość odcinka 
from random import randint


def create_random_rational_number_list(n=100):
    return[(randint(1,20), randint(1,20)) for _ in range(n)]


def cords_between(c1, c2, list_of_cords):
    if c1[0] > c2[0]:
        c1, c2 = c2, c1 # ustawiam sobie kord drugi jako zawsze ten większy
    for cord_between in range(len(list_of_cords)):
                    if list_of_cords[cord_between] != c1 and list_of_cords[cord_between] != c2: # pierwsze sprawdzenie, czy nie jest to czasem ten sam kord
                        if list_of_cords[cord_between][0] > c1[0] and list_of_cords[cord_between][0] < c2[0]: # drugie, czy znajduje się pomiędzy
                            return True # gdy znajdę kord pomiędzy to, zaczynam szukanie od kolejnego
    return False


def second_segment(list_of_cords, cord1, cord2):
    if len(list_of_cords) > 1: # gdy znajdzie przynajmniej 2 kordy bo tyle potrzeba do odcinka            
        cord3 = None
        cord4 = None
        for id in range(len(list_of_cords)):
            if list_of_cords[id][0] == cord1[0]:
                cord3 = list_of_cords[id]
            if list_of_cords[id][0] == cord2[0]:
                cord4 = list_of_cords[id]
        
        if cord3 != None and cord4 != None: # gdy znajdzie kordy drugiego odcnika to przelecę i sprawdzę czy znajduje się jakiś odcinek pomiędzy
            if cords_between(cord3, cord4, list_of_cords):
                return False # gdy znajdzie jakiś kord pomiędzy nimi to dobieram następny kord c2
            else:
                return cord3, cord4

    return False



def square_on_cartesian_chart(list_of_cords):
    for c1 in range(len(list_of_cords)-1):
        cord1 = list_of_cords[c1]

        filtered_cords1 = list(filter(lambda cord: cord[1] == cord1[1] and cord[0] != cord1[0], list_of_cords)) # będę szukał po przefiltrowaniu, i znalezieniu wspólnej drugiej współżędnej, na tej samej prostej
        for c2 in range(len(filtered_cords1)):
            cord2 = filtered_cords1[c2]
            segment1_len = abs(cord2[0]-cord1[0]) # tworzę sobie długość odcinka
            if cords_between(cord1, cord2, filtered_cords1):
                continue # gdy znajdzie jakiś kord pomiędzy nimi to dobieram następny kord c2
            
            segment_up_cords = list(filter(lambda x: (x[1] - cord2[1]) == segment1_len, list_of_cords)) # filtruję listę, od razu tak, żeby znaleźć punkty leżące powyżej, odległe względem Y o długość pierwszego odcinka
            segment_down_cords = list(filter(lambda x: (cord2[1] - x[1]) == segment1_len, list_of_cords)) # filtruję listę, od razu tak, żeby znaleźć punkty leżące poniżej, odległe względem Y o długość pierwszego odcinka

            if second_segment(segment_up_cords, cord1, cord2) != False:
                return (cord1, cord2, second_segment(segment_up_cords, cord1, cord2))
            
            if second_segment(segment_down_cords, cord1, cord2) != False:
                return (cord1, cord2, second_segment(segment_down_cords, cord1, cord2))


    return False


print(square_on_cartesian_chart(create_random_rational_number_list()))