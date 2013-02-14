#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
44.
 Написать функцию,
  получающую в качестве аргумента натуральное число n
   и возвращающую список всех простых делителей n.
"""
n = 1000003
l1 = []

while n != 1:
    print(n)
    for i in range(2, n+1):
        if n % i == 0:
            l1.append(i)
            n = n // i
            print(n)
            break
print(l1)

