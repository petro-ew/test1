#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import itertools
""""
46.
 Написать функцию,
  получающую в качестве агрумента список,
   элементами которого являются либо целые числа,
    либо списки,
     которые, в свою очередь,
      имеют аналогичную структуру.
       Вернуть количество целых чисел во всех списках.
Пример: [[[], 1, [2]], [3, 4, [5, 6]], 7, 8] -> 8
"""
l1 = [[[], 1, [2]], [3, 4, [5, 6]], 7, 8]



def funcz(l1):
    l2 = []
    for x in l1:
        l2 += funcz(x) if isinstance(x, list) else [x]
    return l2

def funcz2(l1):
    l2 = []
    a=0
    for x in l1:
        if isinstance(x, list):

            a=a+1
            l2.append(x)
    print( z)

print(funcz2(l1))

#print(funcz(l1))

