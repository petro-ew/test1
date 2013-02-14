#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
"""
20. 
 Написать функцию,
 берущую в качестве параметра натуральное число n,
  и возвращающую список из n первых чисел Фибоначчи.
"""

n=20

"""
def fibgen(max):  # генератор, а не функция, т.к. оператор return заменён на yield
    a, b = 0, 1
    while a < max:
        l1.append(a)
        yield a # return a, + запоминаем место рестарта для следующего вызова
        a, b = b, a + b # параллельное присваивание, которое выполняется одновременно и параллельно
max = n
def fib(n):
    for n in fibgen(max): # используем генератор fibgen() как итератор
        #print(n), # печатаем все числа Фибоначчи меньшие 100 через пробел
        print(l1)
"""
def fib(n):
	l1=[0, 1]
	for i in range(2, n):
		x = l1[-1]+l1[-2]
		l1.append(x)
	return l1
print(fib(n))


