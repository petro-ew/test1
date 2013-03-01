#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#22-1
#упражнение к главе 1 из учебника.
надо сделать так что бы заменялись звездочки на символы данной цифры.
 Да и вообще переписать бы не помешало бы 
"""
__author__ = 'petro-ew'
import sys
import cmath
import math
import string
"""
Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "]
Digits = [Zero, One]
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: py1.py <number>")
except ValueError as err:
    print(err, "in", digits)
"""
Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "]
digits = [Zero, One]
try:
	numbers2 = []
	numbers3 = []
	numbers = list(sys.argv[1])
	for i in range(len(numbers)):
		numbers2.append(int(numbers[i]))
	print(numbers, numbers2)
	if 0 in numbers2:
		print("Мы ввели НУЛЬ!!!", Zero)
		for i in range(len(Zero)):
			#print(Zero[i])
			spzero = list(Zero[i])
			#print(spzero)
			for j in range(len(spzero)):
				#print(spzero[j])
				if spzero[j] == '*':
					del spzero[j]
					spzero.insert(j, 0)
					#print(spzero)
					numbers3.append(spzero)
				#print(spzero)
			#print(numbers3)
		for j in range(len(numbers3)):
			print(numbers3[j])
	print(numbers3)
	if 1 in numbers2:
		print("Мы ввели ОДИН!!!", One)
except IndexError:
    print("usage: py1.py <number>")
except ValueError as err:
    print(err, "in", digits)

a = 'abc'
print(a)
a = list(a)
print(a)
a = "".join(a)
print(a)#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#22-1
#упражнение к главе 1 из учебника.
надо сделать так что бы заменялись звездочки на символы данной цифры.
 Да и вообще переписать бы не помешало бы 
"""
__author__ = 'petro-ew'
import sys
import cmath
import math
import string
"""
Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "]
Digits = [Zero, One]
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: py1.py <number>")
except ValueError as err:
    print(err, "in", digits)
"""
Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "]
digits = [Zero, One]
try:
	numbers2 = []
	numbers3 = []
	numbers = list(sys.argv[1])
	for i in range(len(numbers)):
		numbers2.append(int(numbers[i]))
	print(numbers, numbers2)
	if 0 in numbers2:
		print("Мы ввели НУЛЬ!!!", Zero)
		for i in range(len(Zero)):
			#print(Zero[i])
			spzero = list(Zero[i])
			#print(spzero)
			for j in range(len(spzero)):
				#print(spzero[j])
				if spzero[j] == '*':
					del spzero[j]
					spzero.insert(j, 0)
					#print(spzero)
					numbers3.append(spzero)
				#print(spzero)
			#print(numbers3)
		for j in range(len(numbers3)):
			print(numbers3[j])
	print(numbers3)
	if 1 in numbers2:
		print("Мы ввели ОДИН!!!", One)
except IndexError:
    print("usage: py1.py <number>")
except ValueError as err:
    print(err, "in", digits)

a = 'abc'
print(a)
a = list(a)
print(a)
a = "".join(a)
print(a)