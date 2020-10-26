# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba zakończona jest unikalną cyfrą.

# oblece zadanko dictem do którego będę wrzucał ile razy sie pojawiła sie dana cyfra

number_keyboard = int(input('Insert a number: '))

def zad13(number):
        
    # numbers_dict ={i: 0 for i in range(10)} # zrobiłem dicta z wartosciami 0 i sobie bede do nicz dodawal to jest spoko pomysł ale metodą na dicta .get(key, default_val) bedzie szybszy przy małych dictach

    numbers_dict = {}

    last_number = number % 10
    
    for actual_number in str(number):
        numbers_dict[int(actual_number)] = numbers_dict.get(int(actual_number), 0) + 1 # metodą get, pierwszy raz uzywalem ustawiam wartosc domyslna 0 i inkrementuje wartosc poprzednia o 1 

    return True if numbers_dict[last_number] == 1 else False


print(zad13(number_keyboard))
