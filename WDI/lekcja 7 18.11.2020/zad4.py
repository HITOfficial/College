# Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
# zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.

from random import randint
from zad1 import  *




def create_random_irrational_number_list(n=100):
    return[(randint(1,100), randint(1,100)) for _ in range(n)]



    #q  = an+1/an
    #r = an+1 - an

    # zrobię to w ten sposób:
    #                        znajduję 2 liczby, sprawdzam ich r i q
    #                        następnie porównuję an+1 / an =? q lub analogicznie r

def check_LA_LG(list_to_check=create_random_irrational_number_list()):
    lg = 0
    la = 0
    for i in range(len(list_to_check)-2): # na 3 pętlach będę to leciał
        for j in range(i+1, len(list_to_check)-1): # zakładam że nie wracam się już w pętli
            actual_la = 2
            actual_lg = 2

            r = difference_irrational(list_to_check[j], list_to_check[i]) # an+1 - an
            q = divide_irrational(list_to_check[j], list_to_check[i]) # an+1 / an
            for k in range(j+1, len(list_to_check)):
                if difference_irrational(list_to_check[k], list_to_check[i]) == r:
                    actual_la += 1
                    j = k # ustawiam jako an <- an+1
                if divide_irrational(list_to_check[k], list_to_check[i]) == q:
                    actual_lg += 1
                    j = k # ustawiam jako an <- an+1
            
            if actual_la > 2:
                la += 1
            if actual_lg > 2:
                lg += 1

    if la > lg:
        return 1
    elif la == lg:
        return 0
    else:
        return -1 


print(check_LA_LG())