#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
__author__ = 'petro-ew'

"""
12.
Программа запрашивает натуральное число n.
 Вывести все тройки чисел a, b, c такие что a<=n, b<=n, c<=n и a**2 + b**2 равно c**2
"""

n = int(input())
print(n)
z = n
zz = n
k1 = ()
#a**2 + b**2 = c**2
for i in range(1, n+1):
    a2 = i**2
    a=i
    for j in range(1, z+1):
        b2=j**2
        b=j
        for k in range(1, zz+1):
            c2=k**2
            c=k
            if c2 == a2+b2:
                k1 = (i, j, k)
                print(k1)
           # else:
           #     print("решений нет!")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
__author__ = 'petro-ew'

"""
12.
Программа запрашивает натуральное число n.
 Вывести все тройки чисел a, b, c такие что a<=n, b<=n, c<=n и a**2 + b**2 равно c**2
"""

n = int(input())
print(n)
z = n
zz = n
k1 = ()
#a**2 + b**2 = c**2
for i in range(1, n+1):
    a2 = i**2
    a=i
    for j in range(1, z+1):
        b2=j**2
        b=j
        for k in range(1, zz+1):
            c2=k**2
            c=k
            if c2 == a2+b2:
                k1 = (i, j, k)
                print(k1)
           # else:
           #     print("решений нет!")


