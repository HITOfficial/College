# Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
# oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.

def min_max(T):
    min_el = max_el = T[len(T)-1] # defaultowo ostatni el z tablicy, bo przy nieparzystych foor loop nie obejmnie
    for i in range(1,len(T),2): # T[i] -> wiekszy, T[i-1] mniejszy
        if(T[i-1] > T[i]):
            T[i], T[i-1] = T[i-1], T[i]
        if T[i] > max_el:
            max_el = T[i]
        if T[i-1] < min_el:
            min_el = T[i]
    return min_el, max_el
