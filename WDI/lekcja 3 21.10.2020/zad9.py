# Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
# do k, metodą prostokątów.


#  zwizualizować sobie wykres y = 1/x z przedziału od 1-k

#  lecieć sobie pokolei dla x => <1,2>,<2,3>...<k-1,k> i rysować sobie prostokąty gdzie bok a u x aktualny(a w sumie x zawsze przyjmę jako 1) i y = 1/x aktualne

k = 100


# pole bedzie w postaci zmienno przecinkowej(float)
def zad9(k):
    area = 0
    for x in range(1, k): # bo lecę od 1 do k <- i na końcu k ma być prawym bokiem kwadracika, więc nie robie k+1
        area += 1/x

    return f'Pole wynosi: {area} jednostek^2'

print(zad9(10))