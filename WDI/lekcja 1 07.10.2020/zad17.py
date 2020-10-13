def ciag_fib(liczba1, liczba2):
    a = liczba1
    b = liczba2
    iloraz_ciagu = 0
    print(1) # żeby dwókrotnie mieć 1
    while a < 1_000_000:
        print(a)
        iloraz_ciagu = b / a
        print(f'wyrazy ciagu {b} , {a} a ich iloraz {iloraz_ciagu}')
        tmp = a 
        a = a + b
        b = tmp
ciag_fib(5,8)