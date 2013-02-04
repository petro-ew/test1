__author__ = 'petro-ew'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

"""
10
Программа запрашивает натуральное число n ( 1,2,3.... ).
 Выводит список всех простых чисел
   меньших либо равных n.
"""
n = int(input())
print(n)
l1 = []
if n>0:
    for i in range(1, n+1):
        print(i)
        if i%3 != 0 and i%2 != 0:
           l1.append(i)
print(l1)