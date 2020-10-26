# Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
# zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

# zrobię dicta, do którego będę wkładał cyfry z któych są zbudowane liczby
def dict_number(number):
    number_dict = {}
    # wrzucę stringa i obskocze po elementach
    for actual_number in str(number):
        number_dict[int(actual_number)] = number_dict.get(int(actual_number),0) + 1
    
    return number_dict


def zad2(number1, number2):
    number1_as_dict = dict_number(number1)
    number2_as_dict = dict_number(number2)
    
    return True if number1_as_dict == number2_as_dict else False

print(zad2(221, 132))