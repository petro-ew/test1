#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math

__author__ = 'petro-ew'
#zadacha number 1
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1=[]
x=0
while x < n:
    x=x+1
    l1.append(x)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1=[]
for x in range(1,n+1):
    l1.append(x)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1 = range(1,n+1)
l1 = list(l1)
print(l1)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
print([x ** 2 for x in list(range(1,n+1))])
"""

#список квадратов чисел от 1 до 10
n = int(input())
print("n=", n)
l2 = [x ** 2 for x in range(1, n + 1)]
print(l2)
