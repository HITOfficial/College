# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
# Proszę napisać funkcję, która odpowiada na pytanie, czy w każdym wierszu
# tablicy występuje co najmniej jedna liczba złożona wyłącznie z nieparzystych cyfr.

from random import randint
from math import ceil, log10


# r- row, c- column
def zad2(r,c,n_range):
    square_list =[
        [randint(1, n_range) for _ in range(c)] 
        for _ in range(r)] # utworzyłem tutaj sobie 2 wymiarową tablicę odrazu wypełnioną elementami

    print(square_list)

    for r_list in square_list:
        only_odd_num_cell = False
        
        for cell in r_list:
            odd_count = 0
            number_len = ceil(log10(cell)) # sprawdzam jakiej długości jest dana liczba

            for _ in range(number_len): # oblatuje po kolejnych pojedyńczych cyfrach z liczby i sprawdzam czy są nieparzyste, następnie je zliczam i sprawdzam, czy ilość tych liczb nieparzystych jest równa długości liczby jeśli tak to wskakuje do kolejnego wiersza, a jeśli nie, to zwracał Fałsz
                if cell % 2 == 1:
                    odd_count += 1
                cell //= 10
            
            if number_len == odd_count:
                only_odd_num_cell = True
                break
                
        if only_odd_num_cell == False: 
            return False
    
    return True



print(zad2(15, 17, 2))