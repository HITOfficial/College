# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.

def count_numbers(n=120):
    counter = 0
    for i in range(1,n+2):
        i_before_dividing = i
        #oblecę sobie po wszystkich możliwych dwójkach, trójkach i piątkach w liczbie, i jeśli po wszystkich działaniach liczba będzie wynosiła 1 - to ją wypiszę jako tą 2/3/5
        while i % 2 == 0:
            i /= 2
            counter +=1
        while i % 3 == 0:
            i /= 3
            counter +=1
        while i % 5 == 0:
            i /= 5
            counter +=1
        if i == 1:
            counter +=1
    return counter

print(count_numbers())

# na lekcji:

def count_numbers1():
    n = int(input('>>'))

    # liczby dwu trzy piątkowe
    count = 0
    a2 = 1
    while a2 <=n:
        a3 = a2
        while a3 <= n:
            a5 = a3
            while a5 <= n:
                count += 1
                a5 *= 5
            a3 *= 3
        a2 *= 2

    print(count)    


    

