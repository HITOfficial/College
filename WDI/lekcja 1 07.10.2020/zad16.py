# zrobie slownik a w nim element - ilosc przejść
import time

def an_plus_1(a):
    a = (a % 2) * (3 * a + 1) + (1 - a % 2) * (a / 2)
    return a


def wyszukanie_najwiekszej_ilosci_operacji(dictionary):
    list_of_dictionary_val = [dictionary[el] for el in dictionary] # wrzucam wartości z dict'a do listy
    list_of_dictionary_val.sort(reverse=True) # sortuje malejaco elementy z listy
    najwieksza = list_of_dictionary_val[0] # pobieram tylko pierwszy element z listy (czyli ten najwiekszy)

    for key, val in dictionary.items(): # lece po dict po kluczu i val
        if(najwieksza == dictionary[key]):
            print(f'Dla liczby {key} wykonano {val} przejść!')


def zad16():
    dictionary = {el : 0 for el in range (2, 10000)} # tworze słownik do którego będę przypisywał ilosc iteracji zanim warunek zostanie wykonany
    a = 2
    for el in dictionary: # lece po wszystkich elementach słownika
        a = el 
        while a != 1: # na każdej wartosci klucza ze słownika wywołuję funkcję, i dopóki nie zwróci 1 to będzie się wykonywać, oraz zwiekszać licznik przejść o 1
            a = an_plus_1(a)
            dictionary[el] += 1 # powiekszam wartość klucza o 1 - bo wykonałem o 1 wiecej iteracji

    wyszukanie_najwiekszej_ilosci_operacji(dictionary)
    






zad16()
