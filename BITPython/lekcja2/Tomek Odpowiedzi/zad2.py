# Zadanie 2
# Stwórz funkcję rand_dict(n), która dla danej liczby naturalnej n generuje słownik z n parami (klucz, wartość),
# gdzie klucze i wartości to losowe liczby naturalne z zakresu [0, 20].

# Dla ambitnych: zmodyfikować kod tak, aby zawsze generował dokładnie n par, jeżeli to jest tylko możliwe (tj. 0 <= n <= 21).

# Następnie napisz funkcję reverse_dict(dictionary), która odwraca odwzorowanie w słowniku, tj. stare klucze stają się wartościami,
# a stare wartości stają się kluczami. Jak zachowa się twoja funkcja, gdy odwzorowanie nie będzie bijekcją (dwustronnie unikatowe wartości), tj. będą 2 takie same wartości?

d = {
    'Kr': False,
    'Xd': True,
    'Ab': 42,
}

# d = dict([
#     ('Kr', False),
#     ('Xd', False),
#     ('Xd', True),
# ])
# print(d)

# dictionary_reversed = {
#     False: 'Kr',
#     True: 'Xd',
# }

# dictionary_reversed = {
#     v: k
#     for k, v in d.items()
# }

# dictionary_reversed = dict(map(reversed, d.items()))

# print(dictionary_reversed)

# print(dictionary_reversed)