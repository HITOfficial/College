# Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane
# są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), zwracającą
# długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku gdy
# w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
# Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.


# trzeba przedzielić przez NWD do testów bo inaczej nie przejdzie ich
def NWD(a, b):
    while b != 0:
        b, a = a % b, b
    return a  


# zakładam, że nigdy nie pojawi się mianownik równy 0
def longest(T):
    longest_subset = 0
    for i in range(len(T)-2):
        # dzielenie -> mnożenie przez odwrotność, na tej podstawie spójnych podciągów
        
        next_by_prev = (T[i][1]*T[i+1][0], T[i][0]*T[i+1][1]) # tuple i/i+1
        next_by_prev = (next_by_prev[0] // NWD(next_by_prev[0], next_by_prev[1]), next_by_prev[1] // NWD(next_by_prev[0], next_by_prev[1])) # sprowadzam ułamek do najprostszej postaci
        prev_by_next = (T[i][0]*T[i+1][1], T[i][1]*T[i+1][0]) # tuple i+1/i
        prev_by_next = (prev_by_next[0] // NWD(prev_by_next[0], prev_by_next[1]), prev_by_next[1] // NWD(prev_by_next[0], prev_by_next[1]))
        next_by_prev_count = 2
        prev_by_next_count = 2
        for j in range(i+2,len(T)): # żeby nie robić o n-1 operaci więcej, zaczynam od i+2 tworzenie kolejnych elementów
            j_by_j_prev = (T[j-1][1]*T[j][0], T[j-1][0]*T[j][1])
            j_by_j_prev = (j_by_j_prev[0] // NWD(j_by_j_prev[0], j_by_j_prev[1]), j_by_j_prev[1] // NWD(j_by_j_prev[0], j_by_j_prev[1]))
            j_prev_by_j = (T[j-1][0]*T[j][1], T[j-1][1]*T[j][0])
            j_prev_by_j = (j_prev_by_j[0] // NWD(j_prev_by_j[0], j_prev_by_j[1]), j_prev_by_j[1] // NWD(j_prev_by_j[0], j_prev_by_j[1]))
            
            if j_by_j_prev == next_by_prev:
                next_by_prev_count += 1 
            if j_prev_by_j == prev_by_next:
                prev_by_next_count += 1

        longest_subset = max(longest_subset, next_by_prev_count, prev_by_next_count)

    if longest_subset <= 2:
        return  0
    else:
        return longest_subset



print(longest([(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)])) # wypisze 3
print(longest( [(1,2),(2,2),(4,2),(4,1),(5,1)] )) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] )) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] )) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] )) # wypisze 0
