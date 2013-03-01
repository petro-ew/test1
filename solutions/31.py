#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
31. Написать функцию, которая получает в качетве аргумента строку,
 а возвращает список уникальных символов,
  отсортированный от наиболее часто встречающихся к наимее часто встречающимся.
Пример: "adbadiadaidbddica" -> ['d', 'a', 'i', 'b', 'c']
"""
s = "adbadiadaidbddica"
#s = "aabb"
def funcz(s):
	s = list(s)
	d1 = {}
	for x in s:
		if x not in d1:
			d1[x] = s.count(x)
	d2 = list(d1.items())	
	d2 = sorted(d2, key = lambda x: x[1], reverse = True)
	#for x in d2:
	#	l1.append(x[0])
	l1 = [x[0] for x in d2]
	return l1
print(funcz(s))#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
31. Написать функцию, которая получает в качетве аргумента строку,
 а возвращает список уникальных символов,
  отсортированный от наиболее часто встречающихся к наимее часто встречающимся.
Пример: "adbadiadaidbddica" -> ['d', 'a', 'i', 'b', 'c']
"""
s = "adbadiadaidbddica"
#s = "aabb"
def funcz(s):
	s = list(s)
	d1 = {}
	for x in s:
		if x not in d1:
			d1[x] = s.count(x)
	d2 = list(d1.items())	
	d2 = sorted(d2, key = lambda x: x[1], reverse = True)
	#for x in d2:
	#	l1.append(x[0])
	l1 = [x[0] for x in d2]
	return l1
print(funcz(s))