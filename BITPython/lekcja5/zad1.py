class Usos:
    pass


class Students:
    def __init__(self,imie, nazwisko, adres, nr_legitymacji):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.nr_legitymacji = nr_legitymacji
        self.zbior_kursow = set()


class Workers:
    def __init__(self,imie, nazwisko, adres, nr_id):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.nr_legitymacji = nr_legitymacji
        self.zbior_kursow = set()


class Course:
    def __init__(self,imie, nazwisko, adres, nr_legitymacji):
    self.imie = imie
    self.nazwisko = nazwisko
    self.adres = adres
    self.nr_legitymacji = nr_legitymacji
    self.zbior_kursow = set()