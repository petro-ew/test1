#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
39.
 Написать функцию,
 получающую в качестве аргумента список,
  элементами которого также являются списки.
   Вернуть список,
    состоящий из элементов первого подстписка, затем второго, третьего и т.д.
Пример:
[[1, 2, 3, 4], [5, 6], [7, 8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
l1 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
def funcz(l1):
    l2 = []
    print(l1)
    for x in l1:
        l2 += x
    return(l2)
print(funcz(l1))#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
39.
 Написать функцию,
 получающую в качестве аргумента список,
  элементами которого также являются списки.
   Вернуть список,
    состоящий из элементов первого подстписка, затем второго, третьего и т.д.
Пример:
[[1, 2, 3, 4], [5, 6], [7, 8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
l1 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
def funcz(l1):
    l2 = []
    print(l1)
    for x in l1:
        l2 += x
    return(l2)
print(funcz(l1))