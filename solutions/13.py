__author__ = 'petro-ew'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
"""
zadacha number 13.
Написать функцию, возвращающую сумму квадратов элемента списка.
"""

def quadl1 ():
    l1 = [1, 2, 3, 4, 5]
    l1 = [x ** 2 for x in l1]
    print(l1)
    summ = 0
    for i in range(len(l1)):
        summ = summ +  l1[i]
    print(summ)
    return []
quadl1()