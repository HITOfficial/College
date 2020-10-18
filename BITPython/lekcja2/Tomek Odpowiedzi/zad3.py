# Zadanie 3
# W analizie tekstu często kluczową sprawą są statystyki występowania danych słów.
# Przykładowo, można analizować, jak używanie konkretnych słów wpływa na popularność
# i liczbę followersów na Twitterze, Instagramie etc.

# Napisz funkcję, która dla przekazanego tekstu (stringa) znajduje k najpopularniejszych słów i zwraca je wraz z ich częstotliwością występowania, oraz liczbę słów w tekście ogółem.

# Wskazówki:
# listy posiadają metodę .sort(), która sortuje listę w miejscu: liczby niemalejąco, napisy w porządku leksykograficznym
# aby posortować nierosnąco, używamy argumentu reverse=True.
# listy ze strukturami złożonymi (lista krotek, lista list) są sortowane domyślnie po wartości pod indeksem 0; aby sortować po wartości pod i-tym indeksem:
# from operator import itemgetter
# data.sort(key=itemgetter(i))

from collections import defaultdict
from operator import itemgetter

def zwroc_ile_razy_slowo_wystepuje(zdanie):
    slowa = zdanie.replace('.', '').replace(',', '').split(' ')
    wystapienia = defaultdict(lambda: 0)
    for slowo in slowa:
        # if len(slowo) == 1:
        #     continue
        wystapienia[slowo] = wystapienia[slowo] + 1
    return dict(wystapienia)
    # sum(wystapienia.values())

def zwroc_najpopularniejsze(wystapienia, k):
    lista = list(wystapienia.items())
    lista2 = sorted(lista, key=itemgetter(1), reverse=True)
    return dict(lista2[:k])

zdanie = 'Oprócz kota, o imieniu Ala, Ala ma kota Ala. Ala ma też psa.'
wystapienia = zwroc_ile_razy_slowo_wystepuje(zdanie)
najpopularniejsze = zwroc_najpopularniejsze(wystapienia, 4)

print(wystapienia)
print(najpopularniejsze)
