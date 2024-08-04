# -*- coding: cp1251 -*-
from math import factorial

n =int(input('Введите целое число: '))

if  n == 0:
    print ("факториал данного числа равен 1")
elif n<0:
    print("ошибка. введите положительное число")
else:
    print(factorial(n))

