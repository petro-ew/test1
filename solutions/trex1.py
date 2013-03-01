#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys, traceback
try:
    x = 1 / 0
except ZeroDivisionError:
    Type, Value, Trace = sys.exc_info()
    print("Type: ", Type)
    print("Value:", Value)
    print("Trace:", Trace)
    print("\n", "print_exception()".center(40, "-"))
    traceback.print_exception(Type, Value, Trace, limit=5, file=sys.stdout)
    print("\n", "print_tb()".center(40, "-"))
    traceback.print_tb(Trace, limit=1, file=sys.stdout)
    print("\n", "format_exception()".center(40, "-"))
    print(traceback.format_exception(Type, Value, Trace, limit=5))
    print("\n", "format_exception_only()".center(40, "-"))
    print(traceback.format_exception_only(Type, Value))
print("######################(1)###############################")
try:
    x = 1 / 0
except:
    x = 0
print(x)
print("######################(2)###############################")
print("########################################################")
try:
    x = 10 / 2
    #x = 10 / 0
except ZeroDivisionError:
    print("Delenie na null blin!")
else:
    print("Block Else")
finally:
    print("Block finally")
print("######################(3)###############################")
print("########################################################")

print("Vvedite slovo 'stop' dlya poluchenia resultata")
summa = 0
while True:
    x = input("Vvedite chislo: ")
    x = x.rstrip("\r")
    if x == "stop":
        break
    try:
        x = int(x)
    except ValueError:
        print("Neobhodimo vvesti celoe chislo")
    else:
        summa += x
print("summa chisel ravna : ", summa)
input()
print("######################(4)###############################")
print("########################################################")
