#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
__author__ = 'petro-ew'
"""
9.
В словаре d значениями являются целые числа. Вывести на экран все пары ключ:значение из d в порядке возрастания значений. Пример:
d = {'aaa':5, 'ddd':2, 'qqq':3}
Вывод программы:
'ddd':2
'qqq':3
'aaa':5
"""
d = {'aaa':5, 'ddd':2, 'qqq':3}
print(d)
l1 = []
l2 = []
for key, value in d.items():
    print("key, value= ", key, value)
    l1.append(key)
    l2.append(value)
print(l1,l2)
l2.sort() # sort() сортирует элементы списка по возрастанию.
d2 = dict([(x, y) for x y  in l1 l2])
#for i in range(len(l2))

print(l2, d2)
"""
dict([(x, x**2) for x in (2, 4, 6)])
items = [('name','sveta'),('age',20)]
>>> d = dict(items)
------------
def invert_dict_nonunique(d):
    newdict = {}
    for k, v in d.iteritems():
        newdict.setdefault(v, []).append(k)
    return newdict
d = {'child1': 'parent1','child2': 'parent1','child3': 'parent2','child4': 'parent2'}
print invert_dict_nonunique(d)
>>> {'parent2': ['child3', 'child4'], 'parent1': ['child1', 'child2']}
"""