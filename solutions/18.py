#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import collections
"""
18.
 Написать функцию, берущую в качестве параметра список строк, и возвращающую словарь,
 в котором ключ - строка из этого списка,
  а значение - сколько раз она встречалась в списке.

Пример: ['aaa', 'bb', 'c', 'cc', 'aaa', 'c', 'aaa'] -> {'bb':1, 'aaa':3, 'c':2, 'cc':1 }

"""

l1 = ['aaa', 'bb', 'c', 'cc', 'aaa', 'c', 'aaa']
cnt = collections.Counter(l1)
#d2 = {}
d2 = collections.Counter(l1)
print(d2)
d3={}
def func(l1):
    """
    функция берет список и возвращает труе или фальсе
    """
    zz=0
    for i in range(len(l1)):
        z=l1[i]
        print(z)
        k=0
        for j in range(len(l1)):
          if z == l1[j]:
            k+=1
            d3[z]=k
    return d3
print(func(l1))
"""
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d4)
"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import collections
"""
18.
 Написать функцию, берущую в качестве параметра список строк, и возвращающую словарь,
 в котором ключ - строка из этого списка,
  а значение - сколько раз она встречалась в списке.

Пример: ['aaa', 'bb', 'c', 'cc', 'aaa', 'c', 'aaa'] -> {'bb':1, 'aaa':3, 'c':2, 'cc':1 }

"""

l1 = ['aaa', 'bb', 'c', 'cc', 'aaa', 'c', 'aaa']
cnt = collections.Counter(l1)
#d2 = {}
d2 = collections.Counter(l1)
print(d2)
d3={}
def func(l1):
    """
    функция берет список и возвращает труе или фальсе
    """
    zz=0
    for i in range(len(l1)):
        z=l1[i]
        print(z)
        k=0
        for j in range(len(l1)):
          if z == l1[j]:
            k+=1
            d3[z]=k
    return d3
print(func(l1))
"""
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d4)
"""