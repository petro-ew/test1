#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
36.
 Написать функцию,
  получающую в качестве аргумента два числа x и y (причем x>y),
   и выводящую на экран, насколько x больше y в процентах.
    Вывод осуществлять с одним знаком после запятой, корректно проводить округление.
Примеры:
аргументы: 10, 5
вывод:
x больше y на 100.0%
аргументы: 20009, 10000
вывод:
x больше y на 100.1%
"""
x = 20009
y = 10000

def funcz(x, y):
    z = (x / y) *100 - 100
    print(z)
    #s = '\'{0} больше {1} на {2:3.1f}%\''.format(x, y, z)
    s = "{0} больше {1} на {2:3.1f}%".format(x, y, z)
    return s
print(funcz(x, y))