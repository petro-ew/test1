#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
__author__ = 'petro-ew'
"""
15.
 Написать функцию,
  принимающую в качестве аргумента список и возвращающую список такой же длины, построенный по следующему принципу:
Первый элемент списка = первый элемент аргумента
Второй элемент списка = последний элемент аргумента
Третий элемент списка = второй элемент списка
Четвертый элемент списка = предпоследний элемент списка
и так далее
Пример к 15-й задаче:
Аргумент: [1,2,3,4,5]
Результат: [1,5,2,4,3]
"""
#a = [1, 2, 3 ,4, 5, 6]
a = list(input())

print(a)
def ll1(a=[]):
    lst = a
    l1 = []
    #print(lst)
    lenn = int(len(lst))
    if lenn % 2 == 0:
        print("Длина четная")
        lenn = int(lenn/2)
        for i in range(0, lenn):
            l1.append(lst[i])
            lst.reverse()
            l1.append(lst[i])
            lst.reverse()
            print(l1)
        return l1
    else:
        print("len =", lenn)
        lenn = int((lenn-1)/2)
        print("len =", lenn)
        print("Длина нечетная")
        for i in range(0, lenn):
            l1.append(lst[i])
            lst.reverse()
            l1.append(lst[i])
            lst.reverse()
            print(l1)
        l1.append(lst[lenn])
        return l1

print("l1=", ll1(a))

"""
Пример работы
1234455
['1', '2', '3', '4', '4', '5', '5']
len = 7
len = 3
Длина нечетная
['1', '5']
['1', '5', '2', '5']
['1', '5', '2', '5', '3', '4']
l1= ['1', '5', '2', '5', '3', '4', '4']
"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
__author__ = 'petro-ew'
"""
15.
 Написать функцию,
  принимающую в качестве аргумента список и возвращающую список такой же длины, построенный по следующему принципу:
Первый элемент списка = первый элемент аргумента
Второй элемент списка = последний элемент аргумента
Третий элемент списка = второй элемент списка
Четвертый элемент списка = предпоследний элемент списка
и так далее
Пример к 15-й задаче:
Аргумент: [1,2,3,4,5]
Результат: [1,5,2,4,3]
"""
#a = [1, 2, 3 ,4, 5, 6]
a = list(input())

print(a)
def ll1(a=[]):
    lst = a
    l1 = []
    #print(lst)
    lenn = int(len(lst))
    if lenn % 2 == 0:
        print("Длина четная")
        lenn = int(lenn/2)
        for i in range(0, lenn):
            l1.append(lst[i])
            lst.reverse()
            l1.append(lst[i])
            lst.reverse()
            print(l1)
        return l1
    else:
        print("len =", lenn)
        lenn = int((lenn-1)/2)
        print("len =", lenn)
        print("Длина нечетная")
        for i in range(0, lenn):
            l1.append(lst[i])
            lst.reverse()
            l1.append(lst[i])
            lst.reverse()
            print(l1)
        l1.append(lst[lenn])
        return l1

print("l1=", ll1(a))

"""
Пример работы
1234455
['1', '2', '3', '4', '4', '5', '5']
len = 7
len = 3
Длина нечетная
['1', '5']
['1', '5', '2', '5']
['1', '5', '2', '5', '3', '4']
l1= ['1', '5', '2', '5', '3', '4', '4']
"""