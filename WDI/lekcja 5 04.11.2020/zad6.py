# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.


# Wygeneruje sobie listę I x J
from random import randint

def generate_list(n):
    # generuję listę posortowaną rosnącą w wierszach
    n_list = [sorted([randint(1,100) for _ in range(n)])
        for _ in range(n)]

    return n_list


def sigleton_list(list_to_convert):
    n = len(list_to_convert)
    converted_list = [[0 for _ in range(n)] for _ in range(n)] # wstępnie co ma być wypełniona zerami
    # print(converted_list)

    # utworzę dicta: dla którego którego dam cyfrę jako klucz, i będę zliczał te elementy

    n_as_dict = {} # w dict comp. nw czy łatwo można to obskoczyć, a więc zrobię to zwykle

    for row in list_to_convert:
        for col in row:
            n_as_dict[col] = n_as_dict.get(col, 0) + 1
    

    # n_as_dict_sorted = {key : value for key, value in sorted( n_as_dict.items(), key=lambda item: item[1])}
    # print(n_as_dict)
    # utworzę z dicta listę tupli
    n_as_dict_sorted = dict(sorted(
        [(key, val) for key, val in n_as_dict.items()],
         key = lambda single_tuple: single_tuple[1],
         reverse= True)) # lambda, to niema funkcja a tutaj sortuję listę elementów, konwertując dicta wewnątrz w listę tupli (key, val), sortując tą listę po tuplu[1] - czyli od wartości, i jutro nie będę wiedział jak to robiłem
    # mogłem zrobić to prosciej, i wydajniej ale chciałem obskoczyć to z lambda, i obczaić jak to działa na oko
    n_as_dict_sorted_with_single_element = n_as_dict_sorted.copy()
    
    for key, val in n_as_dict_sorted.items(): # lecę po orginalnym elemencie, a redukuję kopię, i w sumie przez przypadek wyszło wszystko git, bo inaczej pluło błędem, że zmienił długość dict w trakcie
        if val > 1:
            del n_as_dict_sorted_with_single_element[key]

    n_as_list_sorted_with_single_element = sorted(n_as_dict_sorted_with_single_element) # już nie potrzebuję dicta
    # i teraz tym jakoś popodmieniać elementy  w liscie 
    # myślałem to jakoś w zipie upakowac, ale nie widzę spoko pomysłu, ale za to znalazłem jakiegoś next(), więc bedę przypisywał element z listy pojedyńczych elementów
    index_of_single_el = 1
    break_first_for = False

    for i in range(len(converted_list)):
        if break_first_for: # nie wiem jak wyjść ładnie z 2 forów jednocześnie dlatego zrobiłem dodatkową zmienną, która zamyka tego zamyka tego fora
            break

        for j in range(len(converted_list)):
            converted_list[i][j] = n_as_list_sorted_with_single_element[index_of_single_el]
            index_of_single_el += 1
            
            if index_of_single_el == len(n_as_list_sorted_with_single_element):
                break_first_for = True
                break
        
    

    for el in converted_list:
        print(el)
    print(n_as_list_sorted_with_single_element)


sigleton_list(generate_list(10))

# jak będzie duża lista to jedynie może się wysypać ale już tego nie ruszałem