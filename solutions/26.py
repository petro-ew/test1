#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
26.
 Написать функцию,
  берущую в качестве аргумента три целых числа (день, месяяц, год),
   и возвращающую строку даты с разделителем "/".
    Решить двумя вариантами - с использованием оператора "%" и метода format.
Пример: 7, 2, 2013 -> "07/02/2013"
"""
n1 = 10
n2 = 12
n3 = 2013
def funcz(n1, n2, n3):
    """

    :param n1:
    :param n2:
    :param n3:
    """
    #print(n1, n2, n3)
    #n = str(n1) + "/" + str(n2) + "/" + str(n3)

    if n1 < 10:
        n1 ='0'+str(n1)
    if n2 < 10:
        n2 = '0'+str(n2)
    str(n1)
    str(n2)
    n = '%s/%s/%d' % (n1, n2, n3)
    n2 = '{day}/{month}/{year}'.format(day = n1, month = n2, year = n3)
    print("n2 = " , n2)
    #print(n)
    #print(str(n1), "/", str(n2), "/", str(n3))
    return n
print(funcz(n1, n2, n3))