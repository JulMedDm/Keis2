# -*- coding: cp1251 -*-
from math import factorial

n =int(input('������� ����� �����: '))

if  n == 0:
    print ("��������� ������� ����� ����� 1")
elif n<0:
    print("������. ������� ������������� �����")
else:
    print(factorial(n))

