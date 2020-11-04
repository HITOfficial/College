# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę
# kolejnymi liczbami naturalnymi po spirali.

# in scholl

def spiral(t):
    n = len(n_list)
    k = 1 # zaczynamy od 1
    a = 0 # wiersz
    b = n-1 # kolumna
    c = n-1 # kolumna
    d = 0 # wiersz

    while k <= n*n: # squre list
        for i in range(n):
            if t[a][i] == 0:
                t[a][i] = k
                k += 1

        a+=1

        for j in range(n): # ostatnia kolumna
            if t[j][b] == 0:
                t[j][b] = k
                k += 1

        b -= 1
        g = n-1

        for m in range(n-1, -1, -1):
            if t[c][m] == 0:
                t[c][m] = k
                k += 1
        
        c -= 1

        for p in range(n-1, 1, -1):
            if t[p][d] == 0:
                t[p][d] = k
                k += 1
        
        d -= 1


def spiral2(t):
    n = len()
    k = 1 # zaczynamy od 1
    a = 0 # wiersz
    b = n-1 # kolumna

    while a < b: # squre list
        for i in range(a, b+1):
            t[a][i] = k
            k += 1

        for i in range(a+1, b):
            t[i][b] = k
            k += 1

        for i in range(b, a, -1):
            t[b][1] = k
            k += 1
        
        for i in range(b, a, -1):
            t[i][a] = k
            k += 1

        a += 1
        b -= 1