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

print(prime_number_list(200))

