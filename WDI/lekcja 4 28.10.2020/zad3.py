# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa

# zrobie tablice z wszystkim elementami <2,N)
# z warunku % 2 lub 3 lub 5, lub 7 != 0

def prime_number_list(n):
    prime_list = [el for el in range(2, n)
                      if el % 2 != 0
                      and el % 3 != 0
                      and el % 5 != 0
                      and el % 7 != 0
                      or el == 2
                      or el == 3
                      or el == 5
                      or el == 7]
                      
    return prime_list

# print(prime_number_list(200))






# FROM College

from math import sqrt, ceil

# n = int(input('> '))

def erastotenes(n=25):
    erastotenes_list =[True for _ in range(n+1)]
    erastotenes_list[0] = erastotenes_list[1] = False

    for i in range(2, ceil(int(sqrt(n))) + 1):
        if erastotenes_list[i]:
            for a in range(i*i,n+1, i):
                erastotenes_list[a] = False

    for i in range(n+1):
        if erastotenes_list[i]:
            print(i)

erastotenes()
