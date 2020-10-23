# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
# różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
# dla 2315 będą to 21, 35, 231, 315.


    # na podstawie WDI i dyskretnej:
    # wiem że każdą liczbę pojedyńczą (1-9) mogę zapisać na 4 bitach 0000 - 1001 // ale tutaj tego nie uzyję


    # ilość zbiorów utworzonych z liczny jest równy 2^n, gdzie n jest równa len(number)
    # dlatego zrobiłem maski bitowe, nie ogarniam doładnie ich ale na oko wyszło

def zad5():
    number = 2315
    tmp_number = number

    #długość liczby
    number_length = 0
    while tmp_number > 0:
        tmp_number //= 10
        number_length += 1

    for bit_mask in range(1, 2**number_length): # bo nie będę sprawdzał liczby równej 0000
        bit_mask_tmp = bit_mask
        tmp_number = number
        created_number = 0
        up_to = 0
        for _ in range(number_length):
            if bit_mask_tmp %2 == 1:
                created_number = 10**up_to *(tmp_number % 10) + created_number # bo normalnie bym wypisał w odwrotnym ułożeniu liczby, dlatego tutaj co wejscie w warunek dodaje cyfrę z lewej strony
                up_to += 1 
            tmp_number //= 10
            bit_mask_tmp //= 2

        if created_number % 7 == 0:
                print(created_number)
    




print(zad5())
