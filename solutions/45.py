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
l = [1, 2, 3]
def funkz(l):
    k = len(l)

    print(l)
    l2 = []
    l3 = copy.deepcopy(l)
    #j = 1
    #x = 1
    #for i in range(len(l)):
    #функция вычисляющая факториал
    #for x in l:
    #    x *= j
    #    #l2.append(x)
    #    j = x
    #    x=x+1 # + пустой элемент для конкретной задачи
    for i in range(len(l)):
        x = l[i]
        l3.remove(x)
        l2 = l2 + l3
        print(x, l3, l2)
    print(l2)

    return l2
print(funkz(l))