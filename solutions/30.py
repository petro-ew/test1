#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
30.
 Написать функцию,
  которая получает в качестве аргумента строку,
   и возвращает её же, но с удаленными комментариями.
    Комментарий - это все, что находится между символами "/*" и "*/", включая сами эти символы.
Пример: "x += 1; /* увеличиваем x на 1 */ x /= 2; /* и делим пополам */" -> "x +=1;  x /= 2; "

"""
s =  "x += 1; /* увеличиваем x на 1 */ x /= 2; /* и делим пополам */"
def funcz(s):
    """
    получает в качестве аргумента строку,
    и возвращает её же, но с удаленными комментариями.
    :param s:
    :return:
    """
    print(s)
    ss1 = "/*"
    col1 = s.count("/*")
    col2 = s.count("*/")
    sp = []
    #print("count col1 = ", col1, "col2 = ",  col2)
    if col1 == col2:
        for i in range(0, col1):
            s1 = ""
            ss2 = "*/"
            z = s.find(ss1)
            z2 = s.find(ss2)+2
            sp.append(s[:z])
            #print(s)
            #s = s[z] + 'g' + s[z:]
            s2 = s[z2:]
            #print(s2)
            s = s2
            #print(s)
    sp = "".join(sp)
   # s1 = s[]
    #print(z, z2, sp)
    return sp
print(funcz(s))#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
30.
 Написать функцию,
  которая получает в качестве аргумента строку,
   и возвращает её же, но с удаленными комментариями.
    Комментарий - это все, что находится между символами "/*" и "*/", включая сами эти символы.
Пример: "x += 1; /* увеличиваем x на 1 */ x /= 2; /* и делим пополам */" -> "x +=1;  x /= 2; "

"""
s =  "x += 1; /* увеличиваем x на 1 */ x /= 2; /* и делим пополам */"
def funcz(s):
    """
    получает в качестве аргумента строку,
    и возвращает её же, но с удаленными комментариями.
    :param s:
    :return:
    """
    print(s)
    ss1 = "/*"
    col1 = s.count("/*")
    col2 = s.count("*/")
    sp = []
    #print("count col1 = ", col1, "col2 = ",  col2)
    if col1 == col2:
        for i in range(0, col1):
            s1 = ""
            ss2 = "*/"
            z = s.find(ss1)
            z2 = s.find(ss2)+2
            sp.append(s[:z])
            #print(s)
            #s = s[z] + 'g' + s[z:]
            s2 = s[z2:]
            #print(s2)
            s = s2
            #print(s)
    sp = "".join(sp)
   # s1 = s[]
    #print(z, z2, sp)
    return sp
print(funcz(s))