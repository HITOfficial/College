def silnia_liczby(n):
    wynik_z_silni = 1
    i = 1
    if n == 0:
        wynik_z_silni = 1
    while i <= n:
        wynik_z_silni *= i
        i += 1
    return wynik_z_silni

def liczba_e():
    licznik = 1
    silnia = 0
    e = 0
    while silnia < 100: # ustawilem 100 przejść, zeby w miare szybko i dokladnie wyliczylo przyblizenie
        e += licznik / silnia_liczby(silnia)
        silnia += 1
    print(e)

liczba_e()