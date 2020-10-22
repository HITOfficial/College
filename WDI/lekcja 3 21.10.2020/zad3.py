# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

number = int(input('Wprowadź liczbę: '))

def number_palindrom(number):
    if str(number) == reversed(str(number)):
        return True
    else:
        return False 

def number_as_binary(number_to_convert):
    number_as_binary_string = ''
    i = 0
    # oblecę sobie do 2^i <- gdzie będzie to największa możliwa potęga z dzielenia liczby przez 2 i potem bede dodawał 1 i 0 do stringa 
    while 2 ** (i+1) < number_to_convert: # zeby nie otrzymać liczby 2^i  która będzie wieksza niż nasza liczba do skonwertowania 
        i += 1
    
    if 2 ** (i+1) == number_to_convert: # gdy potęga dwójki jest równa tej liczbie powiększam i dodatkowo o 1 bo inaczej będzie się sypało później
            i+=1

    while i >= 0:
        if number_to_convert >= 2 ** i:
            number_as_binary_string += '1'
            number_to_convert -= 2 ** i
        else:
            number_as_binary_string += '0'
        i -= 1

    return number_as_binary_string

def number_as_palindorm(binary_number_string):
    print(binary_number_string)
    if binary_number_string == binary_number_string[::-1]:
        return True
    else:
        return False
        
print(f'Czy Palindrom w Systemie Dziesiętnym: {number_palindrom(number)}')
print(f'Czy Palindom w Systemie dwójkowym: {number_as_palindorm(number_as_binary(number))}')




# tak, jak na lekcji:
def is_palindrom(a):
    b = 0
    a_dodatkowe = a 
    while a > 0:
        c = a % 10
        a = a // 10
        b = b*10 + c

    if b == a:
        return True
    else:
        return False





# DRUGI SPOSÓB NA KONWERSJE DO BINARKI ze stacka:

def binary_second_method(number):
    binary_string = ''
    while number >=1:
        if number %2 == 0:
            binary_string += '0'
            number /=2
        else:
            binary_string += '1'
            number = (number-1)/2

    return binary_string[::-1]