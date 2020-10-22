# Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
# ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

# TODO:

# pobieram 3 liczby jako inputy

# number1 = int(input("podaj liczbę a: "))
# number2 = int(input("podaj liczbę b: "))
# n_correctly = int(input("podaj dokładność: "))

# dzielić a / b i wyciagać resztę z dzielenia pobierać i dodawać do stringa (zrobić dzielenie pod kreską)

# 1,66666
# -----
# 5:3

import math 


def division(a, b, n):
    a_on_start = a
    division_as_string = ''

    #Z OKAZJI ŻE MI WYLECIAŁ BUG  REFACTORING:
    # na początku sprawdzam ile przed przecinkiem ma być liczb w ilorazie:
    if a >= b:
        division_as_string += str(a // b) + ","
        a -= (a // b) * b 
    else:
        division_as_string += '0,'

    while n >= len(division_as_string) - division_as_string.index(','): # chyba to działa dobrze a sprawdzam  n jest większe od róznicy długości stringa od jego przecinka
        if a < b: # sprawdzam czy a jest wieksze od b
            a = int(str(a)+str(0)) # za pomocą tego tworzę resztę dziesiętną z dzielenia dodając 0 na jej końcu i potem zamieniajać spowrotem na int'a
        else:
            division_as_string += str(a // b)
            a -= (a // b) * b  

    return division_as_string

# print(division(7,286,100))

# powyżej wersja ostateczna, i chyba szybsza od wersji alfa


# wersja z lekcji:

def division2(a,b,n):
    print(a // b, end='.')
    r = (a % b)
    for _ in range(n):
        r *= 10 # bo dodajemy 0
        print(r // b, end='') # wypisujemy  całkowitą część z liczby
        r = r % b # a reszta pozostaje resztą z modulo b

print(division2(532,6,16))


# WERSJA alfa, nie działająca dla ilorazu przed przecinkiem wiekszego lub równego 10

# def division(a, b, n):
#     a_on_start = a
#     division_as_string = ''
#     while len(division_as_string) <= n + 1:
#         if a // b < 1: # dziele podane liczby, do całkowitej w kierunku zera
#             if len(division_as_string) < 1:
#                 division_as_string += '0.' # jesli liczba a jest mniejsza od b na wejsciu to dodajemy 0 na poczatku stringa
#             elif True:
#                 division_as_string += '' # jak przy dzieleniu pod kreską dodaję 10 do liczby, a wyniku dodaje zero
#             a = int(str(a)+str(0)) # za pomocą tego tworzę resztę dziesiętną z dzielenia dodając 0 na jej końcu i potem zamieniajać spowrotem na int'a
#         elif len(division_as_string) < 1:
#             division_as_string += str(a // b) + '.'
#             a -= (a // b) * b # a
#         else:
#             division_as_string += str(a // b)
#             a -= (a // b) * b # a 

#     return division_as_string


# print(division(,3,3))
