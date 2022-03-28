# Условие

print('\nСумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.\n\nНайдите сумму всех простых чисел меньше двух миллионов.')
print('\nВНИМАНИЕ! Решение не закончено. Работает только с маленькими числами.')
# input('\nНажмите Enter для продолжения')

# Решение

xmax = int(input('\nВведите число:'))

num = list(range(2,xmax))
num2 = list(range(2,xmax))
for j in num:
    for i in range (2, j):
        if j%i == 0:
            num2.remove(j)
            break

summa = num2[0]
for i in range(len(num2)-1):
    summa += num2[i+1]

# print(num2)
print(summa)





# xmax = 100
# num1 = 2

# num = list(range(2,xmax))
# while num1 < xmax:
#     for i in range (2, num1):
#         if num1%i == 0:
#             num.remove(num1)
#             break
#     num1 += 1
# print(num)
