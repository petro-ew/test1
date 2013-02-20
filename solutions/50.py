#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
""""
50. Решить задачу №24, используя рекурсию, и не используя стандартных функций и методов.

24.
 Написать функцию,
  берущую в качестве аргумента строку из слов,
   разделенных пробелами,
    и возврашающую число слов в строке.
"""

s = "Д митрий Вячеславович Платонов, Хороший человек"

def funcz(s):

    s = list(s)
    print(s)
    p = 1
    for el in s:
        if el == " ":
            p = p + 1
    return p
#print(funcz(s))

def fuck(s, i):

    col = 0
    if s[i] == " ":
        col = col + 1
        return fuck(s, i+1)
        return col
    i += 1
    return fuck(s, i)

def funkk(s):
    print(s)
    i = 0
    return fuck(s, i)
    i = i + 1



print(funkk(s))