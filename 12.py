__author__ = 'petro-ew'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
#__import__ (globals = sys)
"""
12.
Программа запрашивает натуральное число n.
 Вывести все тройки чисел a, b, c такие что a<=n, b<=n, c<=n и a**2 + b**2 равно c**2
"""

n = int(input())
print(n)
z = n
zz = n
k1 = []
#a**2 + b**2 = c**2
for i in range(1, n+1):
    a = i**2
    for j in range(1, z+1):
        b=j**2
        for k in range(1, zz+1):
            c=k**2
            if c == a+b:
                k1.append(i, j, k)
                print(k1)

