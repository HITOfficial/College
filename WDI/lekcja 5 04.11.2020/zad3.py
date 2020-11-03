# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.

# na podstawie zad2 

from random import randint
from math import ceil, log10


# r- row, c- column
def zad3(r,c,n_range):
    square_list =[
        [randint(1, n_range) for _ in range(c)] 
        for _ in range(r)] 

    print(square_list)

    for r_list in square_list:
        cell_with_odd_number = 0 # liczbę ilość komórek w których pojawi się jakaś liczba parzysta

        for cell in r_list:
            number_len = ceil(log10(cell))

            for _ in range(number_len):
                if not cell % 2:
                    cell_with_odd_number += 1
                    break # szukam pierwszą parzystą a potem przechodzę odrazu do kolejnej komórki
                cell //= 10
                
        if cell_with_odd_number == len(r_list): # a tutaj sprawdzam czy ilość komórek z liczbą parzystą jest długości wiersza w którym znajdują się te komórki
            return True
    
    return False



print(zad3(15, 3, 3))