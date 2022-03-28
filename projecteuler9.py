# Условие
print('\nТройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство \n\na^2 + b^2 = c^2\n\nНапример, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.\n\nСуществует только одна тройка Пифагора, для которой a + b + c = 1000.\nНайдите произведение abc.\n')
input('Для получения ответа нажмите Enter.\n')

# Решение 2
from math import sqrt

def euler8():
    a = 1
    while True:
        b = 1
        while a+b+sqrt(a**2+b**2)<1000:
            b += 1
            if sqrt(a**2+b**2)%1==0:
                if a+b+sqrt(a**2+b**2)==1000:
                    print(a, ' * ', b, ' * ' , int(sqrt(a**2+b**2)), ' = ', a*b*int(sqrt(a**2+b**2)))
                    return
        a += 1
euler8()


# First answer

# a = 1
# b = 1
# x=0

# while x==0:
#     b = 1
#     while a+b+sqrt(a**2+b**2)<1000:
#         b += 1
#         # print(a,b, sqrt(a**2+b**2))
#         if sqrt(a**2+b**2)%1==0:
#             if a+b+sqrt(a**2+b**2)==1000:
#                 x=1
#                 # print(a,b, int(sqrt(a**2+b**2)))
#                 print(a, ' * ', b, ' * ' , int(sqrt(a**2+b**2)), ' = ', a*b*int(sqrt(a**2+b**2)))
#     a += 1
