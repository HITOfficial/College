# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

# Utworzę listę, do której będę wrzucał elementy z ciągu An = n ∗ n + n + 1

# def list_of_pattern_string(range_of_strings):
#     list_of_string = [] 
#     for n in range(range_of_strings):
#         list_of_string.append(n * n + n + 1)
#     return list_of_string # pierwszy sposób z tablicą i iterowanie po niej, a drugi będzie sprawdzanie na bierząco


def is_equal_to_pattern_number(number):
    n = 0
    number_from_pattern = 0
    while number_from_pattern <= number:
        number_from_pattern = n*n + n + 1
        if number_from_pattern == number:
            return True
        n+=1
    else:
        return False # do tego zadania będzie to szybszy sposób bo będzie liczył na bierząco


number_from_keyboard = int(input('enter a number: '))

print(is_equal_to_pattern_number(number_from_keyboard))

