# liczby
# for i in range(1, 110+1):

#     print(i, end = ' ') #tworzy spacebar zamiast enter

#     if i % 3 == 0: 
#         print('Fizz', end = '')
#     if  i % 5 == 0: 
#         print('Buzz', end = '')
#     if  i % 7 == 0: 
#         print('Duzz', end = '')
#     print()

# szachownice

# n = 10
# for row in range(n):
#     for col in range(n):
#         if (row + col) % 2 == 0:
#             sign = 'x'
#         else:
#             sign = 'o'
#         print(sign)

#     print()

# binarka 

# binary = []

# while num > 0:
#     r = num % 2
#     num = num // 2
#     binary.append(str(r))

# print(''.join(binary[::-1]))

from random import randint

my_list = [randint(-5, 20) for _ in range(10)]

new_list = [
    element
    for element in my_list
    if element < 10
]

print(my_list)