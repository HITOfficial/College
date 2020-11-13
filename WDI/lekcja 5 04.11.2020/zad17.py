# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.

# całkiem spoko naplutych if'ów tylko będzie
#  

from random import randint

def random_2_dimensions_list(n=10):
    random_list = [[randint(1,50) for _ in range(n)] for _ in range(n)]
    return random_list


def bigest_sum_numbers_next_to(list_to_search):
    bigest_sum = ((0,0), 0) # tworze tupla z indexem wokół którego będę sumował
    i_len = len(list_to_search)
    j_len = len(list_to_search[0]) # tablica jest tych samych wymiarów

    for i in range(i_len):
        for j in range(j_len):
            actual_sum = 0 # el neutralny dodawania

            # elementy nad
            if i-1 >= 0:
                if j-1 >= 0: # lewa góra skosu
                    actual_sum += list_to_search[i-1][j-1]
                if j+1 < j_len-1: # prawa góra skosu
                    actual_sum += list_to_search[i-1][j+1]
                actual_sum += list_to_search[i-1][j] # element ten sam index w wierszu powyżej
            #elementy pod
            if i+1 < i_len -1:
                if j-1 >= 0: # lewa góra skosu
                    actual_sum += list_to_search[i+1][j-1]
                if j+1 < j_len-1: # prawa góra skosu
                    actual_sum += list_to_search[i-1][j+1]
                actual_sum += list_to_search[i-1][j]
            # lewo prawo ten sam wiersz
            if j-1 >= 0:
                actual_sum += list_to_search[i][j-1]
            if j+1 < j_len-1:
                actual_sum += list_to_search[i][j+1]
            # po zsumowaniu wszystkich najbliższych elementów, jesli ich suma będzie większa od tej która była dotychczas to je podmieniam
            if actual_sum > bigest_sum[1]:
                bigest_sum = ((i, j), actual_sum) # tworzymy nowego największa tupla

    return print(bigest_sum)


if __name__ == '__main__':
    bigest_sum_numbers_next_to(random_2_dimensions_list())

    