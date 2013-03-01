#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
51. Написать функцию, получающую в качестве аргумента два целых числа a и b и возвращающую остаток от деления a на b.
Использовать только рекурсию, операции сложения и вычитания, присваивание,
операции сравнения (<, >, ==, <=, >=, !=) и условный оператор if.
"""

a = 11
b = 3

print(a, b)

def funcz(a, b):
   #print(a, b)
   ost = a - b

   if  ost < b:
       res = ost
       #print("res =", res)
       return res
   if ost > b:
       return funcz(ost, b)
   if ost == 0:
       return 0

   #return ost




print(funcz(a, b))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
51. Написать функцию, получающую в качестве аргумента два целых числа a и b и возвращающую остаток от деления a на b.
Использовать только рекурсию, операции сложения и вычитания, присваивание,
операции сравнения (<, >, ==, <=, >=, !=) и условный оператор if.
"""

a = 11
b = 3

print(a, b)

def funcz(a, b):
   #print(a, b)
   ost = a - b

   if  ost < b:
       res = ost
       #print("res =", res)
       return res
   if ost > b:
       return funcz(ost, b)
   if ost == 0:
       return 0

   #return ost




print(funcz(a, b))

