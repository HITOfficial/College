# Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.

from sympy import isprime


t = [243, 81, 27, 9]

def jump_to_next(t, i=0, steps =0):
    if i == len(t)-1:
        return steps
    for k in range(i+1,len(t)):
        if t[i] % k == 0 and isprime(k) and t[i] > k:
            x = jump_to_next(t, k , steps +1) # tworzę zmienną, która przytrzyma wartość z rekurencji
            if x != -1:
                return x
    return -1

print(jump_to_next(t))
    