#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
29.
 Написать функцию,
  которая получает в качестве аргумента число от 1 до 99, а возвращает его строковое представление.
Пример: 56 -> "пятьдесят шесть"

"""
#n = 56 #пять десят шесть
#n = 22 #пять
#n = 20 #два дцать
#n = 30 #три дцать
#n = 81 #восемь десят один
#n = 91 #девяносто один
n = 11
def funcz(n):
    """
    функция получает в качестве аргумента число от 1 до 99, а возвращает его строковое представление.
    Пример: 56 -> "пятьдесят шесть"
    :param n:
    :return:
    """
    n2 = n
    print("ввели число: ", n)
    n2 = str(n2)
    n2 = list(n2)
    ln = len(n2)
    if ln == 2:
        n21 = int(n2[0])
        n22 = int(n2[1])
    #print("n21 = ", n21, "n22 = ", n22)
    #print(n2, ln)
    d1 = {10 :"десять", 20 :"двадцать ", 30 :"тридцать ", 40:"сорок ", 50:"пятьдесят ", 60:"шестьдесят ", 70:"семьдесят ", 80:"восемьдесят ", 90:"девяносто "}
    d2 = {1:"один", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять"}
    d3 = {1:"один", 2:"двe", 3:"три", 4:"четыр", 5:"пят", 6:"шест", 7:"сем", 8:"восем", 9:"девят"}
    if n in d1:
        #print("URA!")
        res = d1[n]
    elif ln == 2 and n21 == 1:
        res = d3[n22] + "надцать"
    elif ln == 1:
        res = d2[n]
    elif ln == 2 and n21 == 2:
        res = d1[20] + d2[n22]
    elif ln == 2 and n21 == 3:
        res = d1[30] + d2[n22]
    elif ln == 2 and n21 == 4:
        res = d1[40] + d2[n22]
    elif ln == 2 and n21 == 5:
        res = d1[50] + d2[n22]
    elif ln == 2 and n21 == 6:
        res = d1[60] + d2[n22]
    elif ln == 2 and n21 == 7:
        res = d1[70] + d2[n22]
    elif ln == 2 and n21 == 8:
        res = d1[80] + d2[n22]
    elif ln == 2 and n21 == 9:
        res = "девяносто " + d2[n22]
    return res
print(funcz(n))

"""
for i in range(10, 11+1):
    n = i
    print(funcz(n))
"""