# Ćwiczenia 3 - wstęp do Pythona - zadania

# We wszystkich poniższych programach zakładamy poprawne wejście od użytkownika, tj. nie powodujące błędów, zgodne z treścią zadania.
# Zadbaj wszędzie o poprawny podział na funkcje i odpowiednią organizację kodu. Możesz korzystać z dowolnych wbudowanych funkcji i metod.

# Zadanie 1
# Operacja czytania pliku z dysku jest wolna, szczególnie na serwerach, gdzie mamy dyski HDD. Serwery mają natomiast sporo RAMu, więc korzystniej jest wczytać 1 trochę większy plik, niż np. 10 czy 20 małych plików, gdy są to pliki tekstowe.
import os
# Napisz program, który dokona takiej optymalizacji w następujący sposób:
# wybierze pliki tekstowe z aktualnego folderu (os.listdir()), tj. z rozszerzeniem .txt
# połączy treść każdych kolejnych 10 plików (w kolejności leksykograficznej) w jeden, gdzie treści kolejnych plików są rozdzielone linią "\n---EOF---\n" (EOF = End Of File)
# zapisze te dane jako nowy plik, którego nazwa będzie konkatenacją nazw plików, które go stworzyły (żeby było łatwo go potem wyszukać za pomocą in), nadal w kolejności leksykograficznej, rozdzielone podkreśleniami _
# usunie pojedyncze pliki, które zostały zmerge'owane (więc w folderze zostanie ~10 razy mniej plików)
if __name__ == "__main__":
    files_list = [file for file in os.listdir() if file.endswith(".txt")]
    print(files_list)

    data = []

    

    for file_name in files_list:
        with open(file_name) as file:
            data.append(file.read())


    for i in range(0, len(data), 10): # co 10 elementow
        if i + 10 < len(data):
            data_to_save = data[i : i+10] # co dziesiec elementow jesli sa pelne dziesiatki
            savefile_name = files_list[i : i + 10]
        else:
            data_to_save = data[i:] # inaczej pozostale elementy tzn mod 10 co pozostalo
            savefile_name = files_list[i:]


        savefile_name = "_".join(savefile_name)
        savefile_name += ".txt"
        savefile_name = "\n---EOF---\n".join(savefile_name)

        with open(savefile_name, "w") as file:
            file.write(data_to_save)

    for file in files_list:
        os.remove(file)

# Przykładowo:
# Folder zawiera pliki "article1.txt", "article2.txt" i "article3.txt":
# article1.txt:
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# article2.txt:
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# article3.txt:
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Wynik:
# W folderze jest tylko plik article1_article2_article3.txt:
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit.

# ---EOF---

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.

# ---EOF---

# Lorem ipsum dolor sit amet, consectetur adipiscing elit."



# Zadanie 2
# Napisz program, który realizuje funkcjonalność wyszukiwania pliku na serwerze, opisaną w poprzednim zadaniu. Należy zwrócić treść odpowiedniego pliku.

# Przykładowo:
# Użytkownik chce dostępu do artykułu article1. W związku z tym musimy wczytać plik agregacyjny, do którego trafił article1.txt (w przykładzie: article1_article2_article3.txt), a następnie znaleźć jego treść w tym pliku i ją zwrócić.

    wanted_file = input("Enter filename:")
    file_to_read = ""

    for file in os.listdir():
        if wanted_file in file and file.endswitch(".txt"):
            file_to_read = file
            break
    
    file_to_read = file_to_read.rstrip(".txt")
    # file_to_read = file_to_read[-4: ] # zeby bez ostatnich 4 - czyli .txt pobrac
    files = file_to_read.split("_")

    with open(file_to_read, "r") as file:
        data = file.read() # full file as a string

    data = data.split("\n---EOF---\n")
        
    i = files.index(wanted_file.rstrip(".txt")) # szuka pierwszego indexu elementu

    print(data[i])

# Zadanie 3
# Zadanie wzorowane na prawdziwym zadaniu rekrutacyjnym, które osoba prowadząca wtorkowy wykład miała niedawno.

# Strona social media chce nam sugerować nowe fanpage'e i ludzi do followania. Wymyśliłeś do tego celu metrykę (mierzalną wielkość) w postaci liczby wspólnie followowanych znajomych i fanpage'ów.
# Twoje dane mają postać pliku, w którym najpierw jest imię i nazwisko osoby / nazwa fanpage'a, a potem -> i zbiór jej followowanych znajomych / fanpage'ów, rozdzielonych przecinkami. Bycie followowanym jest asymetryczne, jak na Twitterze, tzn. można kogoś follować bez bycia followowanym. Przykładowo:
# Mark Twain -> Book Lovers, Old School Club, Lovecraft
# John Doe -> Nonexistents, Generic People, Jane Smith

# Napisz funkcję, która dla podanego pliku z danymi i stringa w identycznym formacie dla nowej osoby zasugeruje jej 5 nowych fanpage'y do followowania.
# Te 5 fanpage'y ma być najpopularniejsze wśród jej followowanych stron. Chcemy sugerować tylko te osoby / fanpage'e, których jeszcze nie followujemy.

# Ja -> A, B, Adam
# Adam -> On, C, Q
# On -> A, B, H


    from operator import itemgetter

    def get_suggestions(filename, username):

        data = {}

        with open (filename, "r") as file:
            for line in file:
                (user, liked_pages) = line.split("->") # Ja -> A, B, Adam
                user.strip() # "Ja"
                liked_pages = [page.strip() for page in liked_pages.split(",")] # liked_pages = ["A", "B", "Adam"]
                data[user] = liked_pages # dict w ktorym key = Ja       val = ["A","B","Adam"]

        sugestions = dict()

        already_followed = set(data[username]) # tworzy set {}
        for friend in data[username]:
            for page in data[friend]:
                if page not in already_followed:
                    sugestions[page] = sugestions.get(page, 0) + 1
                    
        # sorted_sugestions = sugestions.items() 
        # sorted_sugestions.sort(key=itemgetter(1))       # {"strona": 3} (key, val) itemgetter(1) sortuje po wartosci           
        sorted_sug = dict(sorted(sugestions.items(), reverse=True, key=itemgetter(1))) # tablica klotek[(key1, val1), (key2, val2)]
        
        return sorted_sug.keys()[0:5] # pierwsze 5 el 



    filename = input("Enter filename: ")
    user = input("User name: ")

    print(get_suggestions(filename,user))

# Zadanie 4
# Ważnym zastosowaniem Pythona jest sztuczna inteligencja oraz jej najpopularniejsza poddziedzina, czyli uczenie maszynowe (Machine Learning, ML).
# Kiedy chcemy przetwarzać teksty w ML (np. silniki wyszukiwarek, klasyfikacja tematyczna tekstów, identyfikacja autorów), musimy je przetworzyć do postaci numerycznej - komputery rozumieją liczby, nie słowa.
# Popularną reprezentacją tekstów jest Bag-Of-Words. Budujemy w niej "worek" słów, zakładając, że ich kolejność nie ma aż tak dużego znaczenia (zaskakująco częste!).
# Kroki potrzebne do zbudowania Bag-Of-Words (BoW):
# zamiana całego tekstu na lowercase
# pocięcie tekstu na poszczególne zdania, zgodnie z regułami gramatyki
# pocięcie tekstu na poszczególne słowa, zgodnie z regułami gramatyki
# wyrzucenie tzw. stop words, czyli popularnych i mało ważnych słów, np. a, an, the, he, she, is, am
# usunięcie interpunkcji z listy
# stemming, czyli zamiana słów na ich tematy (słowa się odmieniają, nas interesuje sam "stem" słowa, czyli temat)
# usunięcie zbyt krótkich (długość < 3) słów - mogą powstać, gdy liczymy tematy bardzo krótkich słów, ale wtedy dużo różnych słów może mieć ten sam temat
# zliczenie wystąpień poszczególnych słów
# Napisz funkcję, która dla przekazanego tekstu stworzy dla niego reprezentację Bag-of-Words, tj. wykona powyższe kroki na tekście i zwróci słownik mapujący słowa na liczbę wystąpień.
# Nie pozbywaj się tego programu - można się tym pochwalić np. na Githubie (razem z innymi większymi zadaniami z BIT Python).

# Podpowiedź: użyj list comprehension. Dużo, dużo list comprehension. Innych struktur danych też, jeżeli tylko będzie trzeba.


# Przydatne elementy:
# moduł nltk (pip install nltk, lub podpowiedź PyCharma), Natural Language ToolKit, do przetwarzania języka naturalnego:
# otrzymanie listy stop words dla języka angielskiego:
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')  # first time, then comment out / remove
# english_stop_words = stopwords.words('english')

# pocięcie tekstu na zdania oraz słowa to odpowiednio funkcje sent_tokenize (od sentence), word_tokenize:
# from nltk.tokenize import sent_tokenize, word_tokenize

# nltk.download("punkt")  # first time, then comment out / remove

# words = word_tokenize("Ala has a cat, not a dog")
# # ["Ala", "has", "a", "cat", "not", "a", "dog"]
# stemming:
# from nltk.stem.porter import PorterStemmer

# stemmer = PorterStemmer()
# word_stem = stemmer.stem("realization")  # "realiz"

# moduł string zawiera zmienną punctuation będącą stringiem z różnymi znakami interpunkcyjnymi (uwaga - wielokropek "..." trzeba dodać samemu!):
# import string

# # string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'







# moduł collections zawiera wyspecjalizowany słownik do zliczania obiektów, czyli Counter, który np. potrafi automatycznie ogarnąć zliczenie obiektów z dowolnego obiektu iterowalnego (poza tym działa identycznie jak słownik):
# from collections import Counter

# word_list = "I have a cat and a dog and a second cat".split()
# cat_num = Counter(word_list)
# # Counter({'a': 3, 'cat': 2, 'and': 2, 'I': 1, … })
