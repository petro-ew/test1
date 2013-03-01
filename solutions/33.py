#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import hashlib
import random
"""
33.
 Написать функцию,
  получающую в качестве аргумента строку,
   и возвращающую ту же строку, 
   в которой в каждом слове символы переставлены в случайном порядке.
"""
s = "Движенья нет сказал мудрец брадатый и 5 раз дал по шапке внуку"
h = hashlib.md5(b"password")
p = h.hexdigest()
print(p)
h2 = hashlib.md5(b"password")
# Пароль, введенный nользователем
if p == h2.hexdigest():
	print("Пароль nравильный")
def funcz(s):
	
	s = s.split()
	s1 = []
	for x in s:
		z = list(x)
		random.shuffle(z)
		z = "".join(z)
		s1.append(z)
	return " ".join(s1)

print(funcz(s))#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import hashlib
import random
"""
33.
 Написать функцию,
  получающую в качестве аргумента строку,
   и возвращающую ту же строку, 
   в которой в каждом слове символы переставлены в случайном порядке.
"""
s = "Движенья нет сказал мудрец брадатый и 5 раз дал по шапке внуку"
h = hashlib.md5(b"password")
p = h.hexdigest()
print(p)
h2 = hashlib.md5(b"password")
# Пароль, введенный nользователем
if p == h2.hexdigest():
	print("Пароль nравильный")
def funcz(s):
	
	s = s.split()
	s1 = []
	for x in s:
		z = list(x)
		random.shuffle(z)
		z = "".join(z)
		s1.append(z)
	return " ".join(s1)

print(funcz(s))