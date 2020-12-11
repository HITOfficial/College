# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)


# A -> ilość cyfr 1
# B -> ilość cyfr 0

def bin_to_dec(number):
    dec_number = 0
    i = 0
    while number > 0:
        dec_number += ((number %10) * (2 ** i))
        i += 1 
        number //= 10
    return dec_number


def is_primary(number):
    if number == 2 or number == 3:
        return True
    if number %2 == 0 or number %3 == 0:
        return False
    i = 5
    while number **1/2 >= i:
        if number %i == 0:
            return False
        i += 2 
        if number %i ==0:
            return False
        i+= 4
        
    return True


def build_bin_number(a, b, digit_number=None, created_number=0, flag= False): # jedynki, zera, nowa dodawana liczba, lista dodawanych liczb
    if flag == False: # flaga będzie warunkiem żeby rozpoczynać od 1 
        flag = True
        a -= 1
        build_bin_number(a,b, 1, created_number, flag)
    else:

        created_number = created_number * 10 + digit_number # pierwsze tworzę aktualne złożenie

        if a == 0 and b == 0:
            if is_primary(bin_to_dec(created_number)):
                print(created_number)
            return

        if a > 0:
            build_bin_number(a-1, b, 1, created_number, flag)
        if b > 0:
            build_bin_number(a, b-1, 0, created_number, flag)


build_bin_number(4,4)
