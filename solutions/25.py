#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
import string
"""
25.
 Написать функцию,
  берущую в качестве аргумента строку,
   и возвращающую новую строку,
    в которой добавлены пробелы после знаков препинания (. , : ; ? !),
     если их там нет.
Пример: "Вставай,проклятьем заклейменный" -> "Вставай, проклятьем заклейменный"
"""
s = "Вставай,проклятьем заклейменный!Вражина:страшный?непонятный!a?"
print("Исходная строка: ", s)
def str1(s):
	s1 = list(s)
	#print(s1)
	s2 = s1[:]
	print(len(s1))
	m = [".", ",", ":", ";", "?", "!"]
	jj = 0
	for j in range(len(s1)):
		for i in range(len(m)):
			x = str(m[i])
			#print("x = ", x)
			if s1[j] == x:
				n = j
				#print("index x = :", n)
				print("Нашли j =", j, "s[j] =", s1[j], "x = ", x , " index x (n) = : ", n, " counter jj = ", jj)
				s2.insert(int(n+1+jj), " ")
				jj+=1
				#print(" counter jj = ", jj)	
				#print("spisok s1 = ", s1)
	s2 = "".join(s2)
	print(s2)
	print(len(s2))
	return s2

def str2(s):
        r = ""
        m = [".", ",", ":", ";", "?", "!"]
        for a in s:
                r += a
                if a in m:
                        r += " "
        return r

def str3(s):
        r = []
        m = [".", ",", ":", ";", "?", "!"]
        for a in list(s):
                r.append(a)
#                print(a)
                if a in m:
                        r.append(" ")
        return "".join(r)

def str4(s):
    m = [".", ",", ":", ";", "?", "!"]
    return "".join([a + " " if a in m else a for a in s])

print(str4(s))

"""	
	for j in range(len(s1)):
		for i in range(len(m)):
			x = str(m[i])
			#print("x = ", x)
			if s1[j] == x:
				#print("Нашли", j)
				n = s1.index(x)
				#print("index x = :", n)
				s1.insert(int(n+1), " ")	
				#print("spisok s1 = ", s1)
"""				
	
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
import string
"""
25.
 Написать функцию,
  берущую в качестве аргумента строку,
   и возвращающую новую строку,
    в которой добавлены пробелы после знаков препинания (. , : ; ? !),
     если их там нет.
Пример: "Вставай,проклятьем заклейменный" -> "Вставай, проклятьем заклейменный"
"""
s = "Вставай,проклятьем заклейменный!Вражина:страшный?непонятный!a?"
print("Исходная строка: ", s)
def str1(s):
	s1 = list(s)
	#print(s1)
	s2 = s1[:]
	print(len(s1))
	m = [".", ",", ":", ";", "?", "!"]
	jj = 0
	for j in range(len(s1)):
		for i in range(len(m)):
			x = str(m[i])
			#print("x = ", x)
			if s1[j] == x:
				n = j
				#print("index x = :", n)
				print("Нашли j =", j, "s[j] =", s1[j], "x = ", x , " index x (n) = : ", n, " counter jj = ", jj)
				s2.insert(int(n+1+jj), " ")
				jj+=1
				#print(" counter jj = ", jj)	
				#print("spisok s1 = ", s1)
	s2 = "".join(s2)
	print(s2)
	print(len(s2))
	return s2

def str2(s):
        r = ""
        m = [".", ",", ":", ";", "?", "!"]
        for a in s:
                r += a
                if a in m:
                        r += " "
        return r

def str3(s):
        r = []
        m = [".", ",", ":", ";", "?", "!"]
        for a in list(s):
                r.append(a)
#                print(a)
                if a in m:
                        r.append(" ")
        return "".join(r)

def str4(s):
    m = [".", ",", ":", ";", "?", "!"]
    return "".join([a + " " if a in m else a for a in s])

print(str4(s))

"""	
	for j in range(len(s1)):
		for i in range(len(m)):
			x = str(m[i])
			#print("x = ", x)
			if s1[j] == x:
				#print("Нашли", j)
				n = s1.index(x)
				#print("index x = :", n)
				s1.insert(int(n+1), " ")	
				#print("spisok s1 = ", s1)
"""				
	
