# Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
# położenie hetmanów

# chetmany się szachują gdy i1 == i2 <- w tym samym wierszu
#                           j1 == j2 <- w tej samej kolumnie
#                           i1 == i2 + x and j1 == j2 -x <- wspólna przekątna

# chyba dobrze liczy, nie mam tylko ograniczeń z wyjście poza index listy przy X'ie, ale w tym zadaniu to bez różnicy, to nie działam na rzeczywistej liście

from random import randint

def generate_random_tuple_list(n=8):
    return[(randint(1,99), randint(1,99)) for _ in range(n)] 


def check_if_is_abe_to_insert_hetmans(hetmans):
    print(hetmans)
    # wydaje mi się, że na 2 pętlach to będę wstanie oblecieć:
    for h1_index in range(len(hetmans)-1): # bo pobieram pierwszego hetmana do przed ostatniego
        for h2_index in range(h1_index + 1, len(hetmans)): # <- porównuję tak: a1 z a2... an -> a2 z a3 ... an ... -> an-1 z an
            i1, j1 = hetmans[h1_index] # ponieważ tuple są imutable, a dane będę modyfikował robię sobie dodatkowe zmienne
            i2, j2 = hetmans[h2_index]
            if i1 == i2 or j1 == j2: # gdy znajdzie dwa hetmany w tej samej kolumnie lub wierszu
                return False 
            for x in range(len(hetmans)): # sprawdzam czy po przekątnych się szachują z wzroku 7 linijka
                if i1 == i2 + x and j1 == j2 - x:
                    return False
                if i1 == i2 - x and j1 == j2 + x:
                    return False

    return True


print(check_if_is_abe_to_insert_hetmans(generate_random_tuple_list()))