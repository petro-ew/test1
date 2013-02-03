__author__ = 'petro-ew'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

"""
10
Программа запрашивает натуральное число n ( 1,2,3.... ).
 Выводит список всех простых чисел
  ( имеющее ровно два различных натуральных делителя: единицу и само себя ),
   меньших либо равных n.
"""
n = int(input())
print(n)
l1 = []
for i in range(1, n+1):
    if n % i ==0 and n % 1 ==0:
       l1.append(i)
print(l1)