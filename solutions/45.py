#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import copy
"""
45.
 Написать функцию,
  получающую в качестве аргумента список целых чисел l
   длиной k
    и возвращающую список всех списков,
     которые можно получить из l
      удалением от 1 до k элементов.
Пример: [1, 2, 3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3]]
"""
l = [1, 2, 3, 6]
def fuckt(l):
    k = len(l)
    print(l)
    l2 = []
    j = 1
    x = 1
    #функция вычисляющая факториал
    for x in l:
        x *= j
        l2.append(x)
        j = x
    x=x+1 # + пустой элемент для конкретной задачи
    print(x)
    return x
#print(fuckt(l))


def funct(l):
    """

    :param l:
    """
    l3 = []
    for i in range(len(l)):
        t = 0

    #    print(l)
    n = len(l)
    a = l
    if t == n:
        for i in range(len(l)):
            x = l[i]
            return x
    else:
        for j in range(t+1, n):
            t = t + 1
            z = a[t+1]
            zz = a[j]
            a[t+1] = a[j]
            a[j] = z
            fuckt(l)
            t = t - 1
            z = a[t+1]
            zz = a[j]
            a[t+1] = a[j]
            a[j] = z

print(funct(l))

