from random import randint

# if __name__ == "__main__":

# Ćwiczenia 2 - wstęp do Pythona - zadania

# Uwaga: we wszystkich poniższych zadaniach zakładamy poprawne wejście od użytkownika, tj. poprawnie sformatowane i nie powodujące samo w sobie błędów.

# Zadanie 1
# Zamień wartościami 2 zmienne:
# ręcznie, używając 3 zmiennej
# bardziej Pythonowo

# Dla ambitnych: jak zamienić ze sobą 2 zmienne będące liczbami naturalnymi bez użycia trzeciej zmiennej?


    # val1 = 3

    # val2 = 4

    # val3 = val2
    # val2 = val1
    # val1 = val3

    # print(val1)



# Zadanie 2
# Stwórz funkcję rand_dict(n), która dla danej liczby naturalnej n generuje słownik z n parami (klucz, wartość), gdzie klucze i wartości to losowe liczby naturalne z zakresu [0, 20].

# Następnie napisz funkcję reverse_dict(dictionary), która odwraca odwzorowanie w słowniku, tj. stare klucze stają się wartościami, a stare wartości stają się kluczami. Jak zachowa się twoja funkcja, gdy odwzorowanie nie będzie bijekcją (dwustronnie unikatowe wartości), tj. będą 2 takie same wartości?



    #  n = 20

    # result = {}      # tworzy pusty słownik

    # def rand_dict(n):
    #     for i in range(n):
    #         d[randint(0, n+1)] = randint(0, n+1)
    #     return result
    

    # def reverse_dict(result):
    #     rev_dict = {}
    #     for key, value in result.items():
    #         rev_dict[value] = key
    #     return rev_dict


    # rand_dict(5)
    # reverse_dict()

    # print(dictionary)

        


# Zadanie 3
# W analizie tekstu często kluczową sprawą są statystyki występowania danych słów. Przykładowo, można analizować, jak używanie konkretnych słów wpływa na popularność i liczbę followersów na Twitterze, Instagramie etc.

# Napisz funkcję, która dla przekazanego tekstu (stringa) znajduje k najpopularniejszych słów i zwraca je wraz z ich częstotliwością występowania, oraz liczbę słów w tekście ogółem.

# Wskazówki:
# listy posiadają metodę .sort(), która sortuje listę w miejscu: liczby niemalejąco, napisy w porządku leksykograficznym
# aby posortować nierosnąco, używamy argumentu reverse=True.
# listy ze strukturami złożonymi (lista krotek, lista list) są sortowane domyślnie po wartości pod indeksem 0; aby sortować po wartości pod i-tym indeksem:
# from operator import itemgetter
# data.sort(key=itemgetter(i))









# Zadanie 4
# W internecie działają color pickery, które dla wybranego koloru poza wartościami RGB czy hex podają też ich nazwę. Potrzebują one odwzorowania RGB -> nazwa koloru.

# Ściągnij plik colors.txt: https://www.dropbox.com/s/pjojinz35fg3d7s/colors.txt?dl=0. Zawiera on listę nazw kolorów wraz z ich kodami RGB, przykładowo:
# Ecru:240 234 218
# Snow White:255 255 255
# White:252 251 248
# Dusty Rose Ult Vy Dk:171 2 73

# Napisz program, który na podstawie takiego pliku stworzy strukturę danych do sprawdzania nazwy koloru na podstawie podanych wartości RGB. Dla celów testowych użytkownik podaje w jednej linii 3 wartości RGB, a nazwa koloru jest wypisywana na konsolę, np.:
# > 240 234 218
# Color name: Ecru

# Jeżeli kolor z danym kodem RGB nie istnieje, to powinien zamiast tego zostać wyświetlony napis "Color not found". Zadbaj o prawidłowy podział programu na funkcje.

    # text_to_open = open("./lekcja2/colors.txt")
    # dictionary = {}
    # for line in text_to_open:
    #     color_name, rgb_code = line.split(':')
    #     rgb_code = rgb_code[:-1]
    #     dictionary[rgb_code] = color_name
    
    # somethink = input("pass an RGB")

    # print(dictionary[somethink])




# Zadanie 5
# Z kumplami organizujecie dużą imprezę. Macie różne preferencje co do napojów i musicie ich sporo kupić, ale problem jest taki, że nie każdy sklep ma każdy napój. Na szczęście każdy z was mieszka obok sklepu i wraz z kumplami zrobiliście listę, jakich napojów potrzebujecie i kto ma jakie napoje w sklepie obok. Informacje zapisaliście w pliku data.txt:
# pepsi, cola, fanta, tomato juice, apple cider

# pepsi, raspberry juice, coconut milk
# tomato juice, grapefruit juice
# almond milk, tomato juice

# W pierwszej linii jest lista napojów, które trzeba kupić, potem pusta linia, a potem w każdej linii asortyment kolejnego sklepu.

# Napisz program, który sprawdzi, czy w tych sklepach kupicie wszystko, czego potrzebujecie. Jeżeli tak, to wypisz "ok", jeżeli nie, to wpisz nazwy tych napojów, których nie dacie rady kupić. Zadbaj o prawidłowy podział programu na funkcje.

    # with open('./lekcja2/shop.txt') as f:
    #     lines = f.readlines()
    #     target = lines[0]
    #     sources = lines[2:]
    #     dictionary = {element: False for element in target.strip().split(', ')}
        
    #     for source in sources:
    #         for drink in source. strip().split(', '):
    #             if drink in dictionary:
    #                 dictionary[drink] = True

    #     if all(dictionary.values()):
    #         print('OK')
    #     else:
    #         print('not ok') 



# Zadanie 6
# Poniższy kod wczytuje kolorowy obraz i zapisuje go w skali szarości. Brakuje w nim jednak implementacji funkcji, która dokonuje konwersji kolorów - uzupełnij jej implementację. W razie potrzeby stwórz funkcje pomocnicze.
# Zgodnie z https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm dodaj do swojej funkcji argument average z wartością domyślną False:
# jeżeli average=True, to bierzemy średnią z 3 kanałów RGB
# jeżeli average=False, to bierzemy średnią ważoną z 3 kanałów RGB, tj. (0.3 * R) + (0.59 * G) + (0.11 * B)

# Uwaga: przed pisaniem kodu w terminalu użyj komendy pip install PIL, albo w PyCharmie użyj Alt+Enter na błędzie przy "from PIL import Image" i kliknij instalację biblioteki pillow.

# from PIL import Image














# Zadanie 7
# Pliki w formacie CSV (Comma Separated Values) są bardzo popularne np. w uczeniu maszynowym i analizie danych, bo jest to prosty i czytelny format, wykorzystywany łatwo przez wiele programów (np. Excel, inne programy obliczeniowe, języki programowania). Przykładowy plik:
# name,age,role,pay
# Steve,22,programmer,10000
# Karen,35,manager,5000
# John,30,analyst,7000

# Pliki w formacie JSON (JavaScript Object Notation) są bardzo popularne w wymianie danych pomiędzy językami programowania i jako sposób podawania konfiguracji programów, bo są proste i czytelne dla człowieka, stanowią też de facto tekstowy zapis słowników. Powyższy plik CSV w postaci JSON:
# {
#   {
#     "name": Steve,
#     "age": 22,
#     "role": programmer,
#     "pay": 10000
#   },
#   {
#     "name": Karen,
#     "age": 35,
#     "role": manager,
#     "pay": 5000
#   },
#   {
#     "name": John,
#     "age": 30,
#     "role": analyst,
#     "pay": 7000
#   }
# }

# Napisz program, który wczytuje plik o nazwie podanej przez użytkownika w formacie .csv i zapisuje obok ten plik przekonwertowany do formatu .json.

# Przyda ci się moduł Pythona json, który potrafi automatycznie zapisać obiekty (np. słowniki) do formatu json, oraz wczytywać takie pliki. Przykładowe wykorzystanie:
# import json

# with open("file.json", "w") as file:
#     json.dump(dictionary, file)

# with open("file.json") as file:
#     dictionary = json.load(file)
