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

s = "Дмитрий Вячеславович Платонов, Хороший человек"
#s = " Д м т"

def funcz(s):

    s = list(s)
    print(s)
    p = 1
    for el in s:
        if el == " ":
            p = p + 1
    return p
#print(funcz(s))


print(s)
def fun(s):
    if s == "":
        return 0
    elif s[0] != " ":
        return 0 + fun(s[1:])
    else:
        return 1 + fun(s[1:])
print(fun(s)+1)