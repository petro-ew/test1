__author__ = 'petro-ew'
import sys
import cmath
import math
#=======================================================
#1-02-2013
#=======================================================
"""
1 - est time 1:50 hh:mm zak to 11:50
1. Имеются два списка с уникальными элементами, l1 и l2.
 Построить список l3 такой,
  что каждый из его элементов входит в l1 или l2,
   НО не в оба сразу.
    Пример:
l1 = [1, 3, 5]
l2 = [2, 5, 7]
Ответ: l3 = [1, 3, 2, 7] (можно в любом другом порядке)
"""

l1 = [1, 3, 5, 4, 11, 12]
l2 = [2, 5, 7, 4, 9]
l11 = l1[:]
l22 = l2[:]
ll1 = len(l1)
ll2 = len(l2)
print("список l1 = ", l1)
print("список l2 = ", l2)
#print("длина списка ll1 = ", ll1)
#print("длина списка ll2 = ", ll2)
if ll1 >= ll2:
    for i in range(len(l2)):
        y = l2[i]
#        print("y = ", y)
        if y in l1:
#            print("Bingo!")
            l22.remove(y)
            l11.remove(y)
#            print(l1)
#            print(l2)
else:
    for i in range(len(l1)):
        y = l1[i]
#        print("y = ", y)
        if y in l2:
#            print("Bingo!")
            l11.remove(y)
            l22.remove(y)
#            print(l1)
#            print(l2)
l3 = l11 + l22
#print(l11)
#print(l22)
print(l3)
__author__ = 'petro-ew'
import sys
import cmath
import math
#=======================================================
#1-02-2013
#=======================================================
"""
1 - est time 1:50 hh:mm zak to 11:50
1. Имеются два списка с уникальными элементами, l1 и l2.
 Построить список l3 такой,
  что каждый из его элементов входит в l1 или l2,
   НО не в оба сразу.
    Пример:
l1 = [1, 3, 5]
l2 = [2, 5, 7]
Ответ: l3 = [1, 3, 2, 7] (можно в любом другом порядке)
"""

l1 = [1, 3, 5, 4, 11, 12]
l2 = [2, 5, 7, 4, 9]
l11 = l1[:]
l22 = l2[:]
ll1 = len(l1)
ll2 = len(l2)
print("список l1 = ", l1)
print("список l2 = ", l2)
#print("длина списка ll1 = ", ll1)
#print("длина списка ll2 = ", ll2)
if ll1 >= ll2:
    for i in range(len(l2)):
        y = l2[i]
#        print("y = ", y)
        if y in l1:
#            print("Bingo!")
            l22.remove(y)
            l11.remove(y)
#            print(l1)
#            print(l2)
else:
    for i in range(len(l1)):
        y = l1[i]
#        print("y = ", y)
        if y in l2:
#            print("Bingo!")
            l11.remove(y)
            l22.remove(y)
#            print(l1)
#            print(l2)
l3 = l11 + l22
#print(l11)
#print(l22)
print(l3)
