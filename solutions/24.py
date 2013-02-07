#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
""""
24.
 Написать функцию,
  берущую в качестве аргумента строку из слов,
   разделенных пробелами,
    и возврашающую число слов в строке.
"""

s = "Дмитрий Вячеславович Платонов - Хороший человек"

def str1(s):
	s = s.split(" ")
	#s.reverse()
	#z = s[0] + " " +s[1]
	n = len(s)
	z = 0
	for i in range(len(s)):
		x = s[i]
		if x in {"|", ",", "-", "+"}:
			print("символ, а не слово! ('", x,"')")
			n -= 1
			z += 1	
	#print(s, n)
	return n, z
print(str1(s),"слов, символов") 
