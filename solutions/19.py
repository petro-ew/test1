#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
"""
19.
 Написать функцию, берущую в качестве параметра список уникальных строк,
 и возвращающую список всех пар строк (в виде кортежа), таких,
  что первая строка пары представляет собой вторую строку, записанную задом наперед.
Пример: ['ab', 'bac', 'sss', 'cab', 'ex', 'ba'] -> [('ab', 'ba'), ('bac', 'cab')]
"""
l1 = ['ab', 'bac', 'sss', 'cab', 'ex', 'ba']
"""
def funck(l1):
	l2=[]
	print(l1)
	l3 = []
	k2 = []
	for i in range(len(l1)):
		k1 = ()
		zz = l1[i]
		#print(zz)
		zz = zz[::-1]
		#zz2 = zz.reverse()
		#print(zz)
		k1 += (l1[i], zz)
		k2.append(k1)	
	return k2
print(funck(l1))
"""
"""
def funck(l1):
	l2=[]
	print(l1)
	l3 = []
	k2 = []
	for i in range(len(l1)):
		k1 = ()
		zz = l1[i]
		#print(zz)
		zz2 = zz[::-1]
		#zz2 = zz.reverse()
		#print(zz, zz2)
		if zz2 in l1:
			#if zz != zz2:
			if zz not in l3:
				l3.append(zz2)
				k1 += (zz, zz2)
				k2.append(k1)
		#print(l3)			
		#k1 += (l1[i], zz)
		#k2.append(k1)	
	return k2
print(funck(l1))
"""
def funck(l1):
	l = []
	for i in range(len(l1)):
		for j in range(i+1, len(l1)):
			if l1[i] == l1[j][::-1]:
				l.append((l1[i], l1[j]))
	return l

#print(funck(l1))

def funck2(l1):
	l = []
	i = 0
	while i < len(l1):
		j = i + 1
		while j < len(l1):
			if l1[i] == l1[j][::-1]:
				l.append((l1[i], l1[j]))
			j += 1
		i += 1
	return l				
print(funck2(l1))