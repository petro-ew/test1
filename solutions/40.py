#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
40. Написать функцию,
 получающую в качестве аргументов две строки a и b,
  и возвращающую строку,
   в которой сначала идет первая буква из a,
    потом первая буква из b и т.д.
     Если одна из строк длинее другой,
      но "непарные" символы просто добавить в конец возвращаемого значения.
Пример:
"abcdef", "xyz" -> "axbyczdef"
"""
a = "abcdef"
b = "qyzgfg"
#a = "xyz"
"""
def func(x1, x2):
    return x1+x2
def funcz(a, b):
    print(a, b)
    s = ""
    if len(a) == len(b):
        s = (list((map(func, a, b))))
        s = "".join(s)
    elif len(a) > len(b):
        lenn = len(a)-len(b)
        print(lenn)
        a2 = a[len(b):]
        print(a2)
        s = (list((map(func, a, b))))
        s.append(a2)
        s = "".join(s)
    else:
        lenn = len(b)-len(a)
        print(lenn)
        a2 = b[len(a):]
        s = (list((map(func, a, b))))
        s.append(a2)
        s = "".join(s)

    return s
print(funcz(a, b))
"""
def func(x1, x2):
    return x1+x2
def funcz(a, b):
    print(a, b)
    s = ""
    if len(a) > len(b):
        a2 = a[len(b):]
    else:
        a2 = b[len(a):]
    s = list(map(func, a, b))
    s.append(a2)
    s = "".join(s)
    return s
print(funcz(a, b))
