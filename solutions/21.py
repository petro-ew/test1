#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
"""
21.
 Написать функцию,
 берущую в качестве параметра натуральное число n и кортеж из трех натуральных чисел k = (k1, k2, k3).
  Функция возвращает True, если n можно представить в виде суммы от одного до трех чисел из k,
   и False в противном случае.
Пример:
n = 5 k = (5, 10, 100) -> True (5 == 5)
n = 3 k = (1, 1, 1) -> True (1 + 1 + 1 == 3)
n = 10 k = (8, 2, 1) -> True (8 + 2 == 10)
n = 7  k = (3, 2, 3) -> False
"""
"""
#n = int(10)
#k1 = (8, 2, 1)
#n = int(7)
#k1 = (3, 2, 3)
#n = int(5)
#k1 = (5, 10, 100)
n = 3
k1 = (1, 1, 1)
def funz(n, k1):
	print("n= ", n)
	l1=[]
	set()
	print(l1)
	if n in l1:
		return True
	else:
		return False
print(n, k1 ,funz(n, k1))
"""
"""
def funz(n, k1):
	print("n= ", n)
	l1=[]
	l1.append(k1[0])
	l1.append(k1[1])
	l1.append(k1[2])
	z = sum(k1)
	l1.append(z)
	print(z)
	z1 = (k1[0] + k1[1])
	l1.append(z1)
	print(z1)
	z2 = (k1[1] + k1[2])
	l1.append(z2)
	print(z2)
	z3 = (k1[2] + k1[0])
	l1.append(z3)
	print(z3)
	print(l1)
	if n in l1:
		return True
	else:
		return False
print(n, k1 ,funz(n, k1))
"""