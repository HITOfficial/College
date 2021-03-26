# prosze zaproponować algo który stwierdzi czy dana liczba występuje w ciągu >n/2 razy

# jesli istnieje >n/2 razy to algo O(n)
from random import randint


def half_series(Arr):
    dominating_number = Arr[0]
    dominations = 1
    for i in range(1,len(Arr)):
        if Arr[i] == dominating_number:
            dominations += 1
        else:
            Arr[i] != dominating_number
            dominations -= 1
            if dominations < 0:
                dominating_number = Arr[i]
    if dominations >= 0:
        c = 0
        for el in Arr:
            if el == dominating_number:
                c += 1
        if c/len(Arr) > 0.5:
            return dominating_number
    else:
        return False

Arr = [randint(1,2) for _ in range(10)]

print(half_series(Arr))