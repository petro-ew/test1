#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import random
"""
34.
То же, что и задача 33, но первую и последнюю букву каждого слова оставить на своих местах.
    33.
    Написать функцию,
    получающую в качестве аргумента строку,
    и возвращающую ту же строку,
    в которой в каждом слове символы переставлены в случайном порядке.
"""
s = "Движенья нет сказал мудрец брадатый и 5 раз дал по шапке внуку"
def funcz(s):

    s = s.split()
    s1 = []
    #z1 = []
    for x in s:
        z = list(x)
        if len(z) !=1:
            nac = z[0]
            kon = z[-1]
            #z1.append(z[0])
            #z1.append(z[-1])
            z = z[1:-1]
            #z = z[:-1]
            #z = z[1:]
            random.shuffle(z)
            z = "".join(z)
            z = nac + z + kon
            #print(z)
            s1.append(z)
        else:
            s1.append(x)
    print(s1)
    return " ".join(s1)

print(funcz(s))#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import random
"""
34.
То же, что и задача 33, но первую и последнюю букву каждого слова оставить на своих местах.
    33.
    Написать функцию,
    получающую в качестве аргумента строку,
    и возвращающую ту же строку,
    в которой в каждом слове символы переставлены в случайном порядке.
"""
s = "Движенья нет сказал мудрец брадатый и 5 раз дал по шапке внуку"
def funcz(s):

    s = s.split()
    s1 = []
    #z1 = []
    for x in s:
        z = list(x)
        if len(z) !=1:
            nac = z[0]
            kon = z[-1]
            #z1.append(z[0])
            #z1.append(z[-1])
            z = z[1:-1]
            #z = z[:-1]
            #z = z[1:]
            random.shuffle(z)
            z = "".join(z)
            z = nac + z + kon
            #print(z)
            s1.append(z)
        else:
            s1.append(x)
    print(s1)
    return " ".join(s1)

print(funcz(s))