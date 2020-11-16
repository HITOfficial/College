# Napisz klasę Pipeline która pozwala na wykonanie serii operacji przekształcających dane.
# Klasa powinna mieć metodę then(f) która przyjmuje obiekty implementujące interfejs Applicable, oraz sama być Applicable.
# Interfejs Applicable definiuje jedną metodę: apply(A) -> B
# Metody klasy Pipeline powinny móc być chainowane.

class Applicable:
    def apply(self):
        pass


class Pipeline(Applicable):
    def __init__(self, function=None):
        self.pipe = []
        self.operation = function

    def then(self, obj):
        self.pipe.append(obj)
        return self

    def apply(self, number):
        for op in self.pipe:
            number = op.operation(number)
        return number


wynik = Pipeline()\
    .then(Pipeline(lambda x: x*2))\
    .then(Pipeline(lambda x: x+3))\
    .then(Pipeline(lambda x: x+3))\
    .then(Pipeline(lambda x: str(x)))\
    .apply(10)

print(wynik)