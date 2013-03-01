#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
28.
 Написать функцию,
  которая считает попугаев.
  В качестве аргумента она получает число от 1 до 99, а возвращает строку с числом попугаев.
Примеры:
42 -> "42 попугая"
1 -> "1 попугай"
13 -> "13 попугаев"
"""
#n = 1
#n = 13
#n = 42
#n = 48
#n = 48
#n = 64
n = 65
def funcz(n):
    """
    :param n:
    :return:
    """
    global res
    n2 = n
    #print("ввели число: ", n)
    n2 = str(n2)
    n2 = list(n2)
    ln = len(n2)
    if ln == 2:
        n21 = int(n2[0])
        n22 = int(n2[1])
        #print("n21 = ", n21, "n22 = ", n22)
    #print(n2, ln)
    d3 = {11:"попугаев"}
    d1 = {1:"попугай", 2:"попугая", 3:"попугая", 4:"попугая", 5:"попугаев", 6:"попугаев", 7:"попугаев", 8:"попугаев", 9:"попугаев"}
    if n%10 == 0:
        res = "попугаев"
    if n in d3:
        res = d3[n]
    if ln == 1:
        res = d1[n]
    if ln == 2 and n21 == 1:
        res = "попугаев"
    elif ln == 2 and n22 == 1 and n != 11:
        res = "попугай"
    elif ln == 2 and n22 in range(2, 5):
        res = "попугая"
    elif ln == 2 and n22 in range(5, 10):
        res = "попугаев"
    return res
print(n, funcz(n))
"""
for i in range (1, 100):
    n = i
    print(n, funcz(n))
"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
28.
 Написать функцию,
  которая считает попугаев.
  В качестве аргумента она получает число от 1 до 99, а возвращает строку с числом попугаев.
Примеры:
42 -> "42 попугая"
1 -> "1 попугай"
13 -> "13 попугаев"
"""
#n = 1
#n = 13
#n = 42
#n = 48
#n = 48
#n = 64
n = 65
def funcz(n):
    """
    :param n:
    :return:
    """
    global res
    n2 = n
    #print("ввели число: ", n)
    n2 = str(n2)
    n2 = list(n2)
    ln = len(n2)
    if ln == 2:
        n21 = int(n2[0])
        n22 = int(n2[1])
        #print("n21 = ", n21, "n22 = ", n22)
    #print(n2, ln)
    d3 = {11:"попугаев"}
    d1 = {1:"попугай", 2:"попугая", 3:"попугая", 4:"попугая", 5:"попугаев", 6:"попугаев", 7:"попугаев", 8:"попугаев", 9:"попугаев"}
    if n%10 == 0:
        res = "попугаев"
    if n in d3:
        res = d3[n]
    if ln == 1:
        res = d1[n]
    if ln == 2 and n21 == 1:
        res = "попугаев"
    elif ln == 2 and n22 == 1 and n != 11:
        res = "попугай"
    elif ln == 2 and n22 in range(2, 5):
        res = "попугая"
    elif ln == 2 and n22 in range(5, 10):
        res = "попугаев"
    return res
print(n, funcz(n))
"""
for i in range (1, 100):
    n = i
    print(n, funcz(n))
"""