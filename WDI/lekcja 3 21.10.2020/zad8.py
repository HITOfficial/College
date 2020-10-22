# Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9,14,15,17,22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
# następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.

# Utworze elementy ciągu fibonacciego z przedziału <1,1000> i dodam je do listy

def fibonacci_list(range_of_number):
    list_of_fib_number =[]
    fib1 = 1
    fib2 = 1
    while fib2 < range_of_number:
        list_of_fib_number.append(fib2)
        fib1, fib2 = fib1 + fib2, fib1 # tuple w linijce pythonowo zamiast uzywac dodatkowej zmiennej
    return list_of_fib_number

# Iteruję po 2 wymiarowej pętli, i sprawdzam czy kombinacja sumy 2 liczb fibb wynosi tej liczbie, jeśli nie to czy kombinacja n+1 również jeśli nie to printuje a jak nie to lece o 1 w górę, aż do skutku
# wrzucę dodatkową funckję do środka w której sprawdzę, jesli podany element, +1 mozna utworzyc z 2 elementów fibb to będę sobie pobierał 
def next_not_fibonacci_number(fib_list, number):
    for el1 in fib_list:
        for el2 in fib_list:
            if  number > el1 + el2:
                pass

print(fibonacci_list(1000))

def funct(fib1,fib2, number):
    if fib