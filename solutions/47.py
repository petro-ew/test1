#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
47. Написать функцию, получающую в качестве аргумента список чисел, и возвращающую сумму элементов списка.
 Использвать рекурсию.
"""

l = [4, 2, 1, 1]

def funczz(l):
    print(l)
    x = 0
    for el in l:
        x = x + el
    return x


def funcz(l, i):
    el = l[i]
    if i > len(l):
        return funcz(l, i+1) + el

    return funcz(l, i+1) + el


print(funcz(l, 0))