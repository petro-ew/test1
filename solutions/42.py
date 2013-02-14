#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
42. Написать функцию,
 получающую в качестве аргумента список целых чисел,
  и возвращающую список из всех пар взаимно простых чисел из этого списка.
   Взаимно простые числа это числа, у которых нет общих делителей, кроме 1.

Пример: [2, 6, 7, 12] -> [(2, 7), (6,7), (7, 12)]
"""
l1 = [2, 6, 7, 12, 5]
def nodab(a,b):
    """
    :param a: chislo 1
    :param b: chislo 2
    :return:
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    if a > 1:
        return True
    else: return False

def funcz(l1):
    print(l1)
    res = []
    for i in range(len(l1)):
        x = l1[i]
        for y in l1:
            if nodab(x, y) == False:
                zz = (x, y)
                if (y, x) not in res:
                    res.append(zz)

    return res
print(funcz(l1))