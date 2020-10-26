# Pewnych liczb nie można przedstawić jako sumy elementów spójnych 
# fragmentów ciągu Fibonacciego, np. 9,14,15,17,22. Proszę napisać program, 
# który wczytuje liczbę naturalną n, wylicza i wypisuje
# następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.

# Utworze elementy ciągu fibonacciego z przedziału <1,1000> i dodam je do listy


#NIEDOKOŃCZYŁEM BO SIĘ JUŻ GUBIŁEM W REKURENCJI

def fibonacci_list(fib_range): # zrobiłem listę ciagu fibonacciego
    fib_list = []
    fib1 = 1
    fib2 = 1
    
    for _ in range(fib_range):
        fib_list.append(fib2)
        fib1, fib2 = fib1+fib2, fib1
    
    return fib_list


    # mam oblecieć sobie tablice od el[1]-[n] cały czas sumując i sprawdzając czy ten ciąg da szukaną liczbę
          # nie zadziała to lecę od el[2]-[n]
                                #itd aż do n
    # zrobię rekurencje, i będę się odwoływał to tej samej funckji

def  is_a_sum_of_fib_seq(number, fib_list, start_index):   
    suma = 0

    for i in range(start_index, len(fib_list)):
        suma += fib_list[i]
        print(suma)
        
        if suma > number: 
            start_index += 1
            is_a_sum_of_fib_seq(number, fib_list, start_index)
            return False


        elif suma == number:
            number += 1
            print('suma jest równa')
            is_a_sum_of_fib_seq(number, fib_list, start_index)
            return False

    if suma != number:
        print(suma, number)


def zad8(number):
    fib_list = fibonacci_list(16) # do 16 elementu ciagu liczby są mniejsze od 1000
    is_a_sum_of_fib_seq(number, fib_list, 0)


print(zad8(18))

















 # TO Źle obrobiłem bo waliłem maskę bitową
def is_a_sum_of_fib_seq(number):
    fib_list = fibonacci_list(13)

    #spróbuję na masce bitowej obrobić zadanie
    # 1 długość maski = 2 ^ długość tablicy - zrobię wszystkie możliwe kombinacje z elementów tablicy

    for bit_mask in range(1, 2 ** len(fib_list)): # nie będe sprawdzal mozliwosci, kiedy jest 0 w masce
        fib_combination_sum = 0

        for el in fib_list:
            if bit_mask % 2 == 0:
                fib_combination_sum += el
            bit_mask //= 2
        if fib_combination_sum < 100:
            print(fib_combination_sum)

    # nie jest jakieś efektywne, bo się powtarzają liczby
# print(is_a_sum_of_fib_seq(13))



    


