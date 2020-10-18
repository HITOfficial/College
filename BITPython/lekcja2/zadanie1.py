import random

# Ćwiczenia 2 - wstęp do Pythona - zadania

# Uwaga: we wszystkich poniższych zadaniach zakładamy poprawne wejście od użytkownika, tj. poprawnie sformatowane i nie powodujące samo w sobie błędów.

# Zadanie 1
# Zamień wartościami 2 zmienne:
# ręcznie, używając 3 zmiennej
# bardziej Pythonowo

# Dla ambitnych: jak zamienić ze sobą 2 zmienne będące liczbami naturalnymi bez użycia trzeciej zmiennej?

if __name__ == "__main__":

    # a = 4
    # b = 5

    # b, a = (a, b) # za pomocą krotki

    # assert a == 5 and b == 4

# Zadanie 2
# Stwórz funkcję rand_dict(n), która dla danej liczby naturalnej n generuje słownik z n parami (klucz, wartość), gdzie klucze i wartości to losowe liczby naturalne z zakresu [0, 20].

# Dla ambitnych: zmodyfikować kod tak, aby zawsze generował dokładnie n par, jeżeli to jest tylko możliwe (tj. 0 <= n <= 21).

# Następnie napisz funkcję reverse_dict(dictionary), która odwraca odwzorowanie w słowniku, tj. stare klucze stają się wartościami, a stare wartości stają się kluczami. Jak zachowa się twoja funkcja, gdy odwzorowanie nie będzie bijekcją (dwustronnie unikatowe wartości), tj. będą 2 takie same wartości?

    # def rand_dict(n):
    #     dictionary = {}
    #     for _ in range (n+1):
    #         value = random.randint(0, 20)
    #         key = random.randint(0, 20)
    #         if key in dictionary:
    #             key = (key+1)%21
    #         dictionary[key] = value
    #     return dictionary

    # print(len(rand_dict(20)))


    # def reverse_dict(dictionary):
    #     dictionary_reversed = {}
    #     for key, val in dictionary.items():
    #         dictionary_reversed[val] = key
    #     return dictionary_reversed

    # print(len(reverse_dict(rand_dict(20))))



# Zadanie 3
# W analizie tekstu często kluczową sprawą są statystyki występowania danych słów. Przykładowo, można analizować, jak używanie konkretnych słów wpływa na popularność i liczbę followersów na Twitterze, Instagramie etc.

# Napisz funkcję, która dla przekazanego tekstu (stringa) znajduje k najpopularniejszych słów i zwraca je wraz z ich częstotliwością występowania, oraz liczbę słów w tekście ogółem.

# Wskazówki:
# listy posiadają metodę .sort(), która sortuje listę w miejscu: liczby niemalejąco, napisy w porządku leksykograficznym
# aby posortować nierosnąco, używamy argumentu reverse=True.
# listy ze strukturami złożonymi (lista krotek, lista list) są sortowane domyślnie po wartości pod indeksem 0; aby sortować po wartości pod i-tym indeksem:
# from operator import itemgetter
# data.sort(key=itemgetter(i))

    from collections import defaultdict

    zdanie = 'Ala ma kota.'

    def ile_razy_slowo(zdanie):
        lista_slow = zdanie.replace('.','').replace(',','').split(' ')
        wystapienia = {}
        # for slowo in lista_slow:
        #     if slowo in wystapienia:
        #         wystapienia[slowo] =+ 1
        #     else: 
        #         wystapienia[slowo] = 0
        for slowo in lista_slow:
            wystapienia[slowo] = wystapienia.get(slowo, 0) # skrócenie przez metodę get
        return dict(wystapienia)

    
    def najpopularniejsze(wystapienia, k):
        return wystapienia.items()

    d = ile_razy_slowo('Ala ma kota')
    print(d)

    ile_razy_slowo_dict = ile_razy_slowo('Ala ma Ala kota Ala kota')
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

# Zadanie 5
# Z kumplami organizujecie dużą imprezę. Macie różne preferencje co do napojów i musicie ich sporo kupić, ale problem jest taki, że nie każdy sklep ma każdy napój. Na szczęście każdy z was mieszka obok sklepu i wraz z kumplami zrobiliście listę, jakich napojów potrzebujecie i kto ma jakie napoje w sklepie obok. Informacje zapisaliście w pliku data.txt:
# pepsi, cola, fanta, tomato juice, apple cider

# pepsi, raspberry juice, coconut milk
# tomato juice, grapefruit juice
# almond milk, tomato juice

# W pierwszej linii jest lista napojów, które trzeba kupić, potem pusta linia, a potem w każdej linii asortyment kolejnego sklepu.

# Napisz program, który sprawdzi, czy w tych sklepach kupicie wszystko, czego potrzebujecie. Jeżeli tak, to wypisz "ok", jeżeli nie, to wpisz nazwy tych napojów, których nie dacie rady kupić. Zadbaj o prawidłowy podział programu na funkcje.

# Zadanie 6
# Poniższy kod wczytuje kolorowy obraz i zapisuje go w skali szarości. Brakuje w nim jednak implementacji funkcji, która dokonuje konwersji kolorów - uzupełnij jej implementację. W razie potrzeby stwórz funkcje pomocnicze.
# Zgodnie z https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm dodaj do swojej funkcji argument average z wartością domyślną False:
# jeżeli average=True, to bierzemy średnią z 3 kanałów RGB
# jeżeli average=False, to bierzemy średnią ważoną z 3 kanałów RGB, tj. (0.3 * R) + (0.59 * G) + (0.11 * B)

# Uwaga: przed pisaniem kodu w terminalu użyj komendy pip install PIL, albo w PyCharmie użyj Alt+Enter na błędzie przy "from PIL import Image" i kliknij instalację biblioteki pillow.

# from PIL import Image


# def load_image(filename):
#     image = Image.open(filename)
#     width, height = image.size
#     pixels = list(image.getdata())
#     image = [pixels[i:i + width] for i in range(0, len(pixels), width)]
#     return image


# def save_image(filename, image):
#     flat_image = [item for sublist in image for item in sublist]
#     height, width = len(image), len(image[0])
#     image_out = Image.new("L", (width, height))
#     image_out.putdata(flat_image)
#     image_out.save(filename)


# def color_to_grey(image):
#     pass  # implement me!
#     # for 2D list (matrix): outer loop - rows, inner loop - columns


# if __name__ == "__main__":
#     in_file = ""  # fill in your image file name
#     out_file = ""  # fill in file name of grayscale image
#     image = load_image(in_file)
#     image = color_to_grey(image)
#     save_image(out_file, image)














# Zadanie 7
# Pliki w formacie CSV (Comma Separated Values) są bardzo popularne np. w uczeniu maszynowym i analizie danych, bo jest to prosty i czytelny format, wykorzystywany łatwo przez wiele programów (np. Excel, inne programy obliczeniowe, języki programowania). Przykładowy plik:
# name,age,role,pay
# Steve,22,programmer,10000
# Karen,35,manager,5000
# John,30,analyst,7000

# Pliki w formacie JSON (JavaScript Object Notation) są bardzo popularne w wymianie danych pomiędzy językami programowania i jako sposób podawania konfiguracji programów, bo są proste i czytelne dla człowieka, stanowią też de facto tekstowy zapis słowników. Powyższy plik CSV w postaci JSON:
# [
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
# ]

# Napisz program, który wczytuje plik o nazwie podanej przez użytkownika w formacie .csv i zapisuje obok ten plik przekonwertowany do formatu .json.

# Przyda ci się moduł Pythona json, który potrafi automatycznie zapisać obiekty (np. słowniki) do formatu json, oraz wczytywać takie pliki. Przykładowe wykorzystanie:
# import json

# with open("file.json", "w") as file:
#     json.dump(dictionary, file)

# with open("file.json") as file:
#     dictionary = json.load(file)
