#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
43. Написать программу,
 считывающую текстовой файл
  и выводящую 20 самых часто встречающихся в нем слов.
   Слово - это последовательность символов,
    не содержащая разделителей.
     Разделители - это символы в данной строке: " .,:;-?!\n".
      Имя файла передается в качестве парамтра командной строки.

"""
import sys
import string
import os.path
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("%-25s%s" % ("Файл:", __file__))
print("%-25s%s" % ("Текущий рабочий каталог:", os.getcwd()))
print("%-25s%s" % ("Каталог для импорта:", sys.path[0]))
print("%-25s%s" % ("Путь к файлу:", os.path.abspath(r"text/part1.txt")))
s1 = " .,:;-?!\n"
strip = string.whitespace + string.punctuation + string.digits + s1
dict = {}
with open(os.path.abspath("text/generation_pi.txt"),"r", encoding="utf-8") as f:
    for line in f:
        for word in line.lower().split():
            word = word.strip(strip)
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    l1 = list(dict.items())
    l1 = sorted(l1, key = lambda x:x[1], reverse=True)
    l1 = l1[:60]
    print(l1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
43. Написать программу,
 считывающую текстовой файл
  и выводящую 20 самых часто встречающихся в нем слов.
   Слово - это последовательность символов,
    не содержащая разделителей.
     Разделители - это символы в данной строке: " .,:;-?!\n".
      Имя файла передается в качестве парамтра командной строки.

"""
import sys
import string
import os.path
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("%-25s%s" % ("Файл:", __file__))
print("%-25s%s" % ("Текущий рабочий каталог:", os.getcwd()))
print("%-25s%s" % ("Каталог для импорта:", sys.path[0]))
print("%-25s%s" % ("Путь к файлу:", os.path.abspath(r"text/part1.txt")))
s1 = " .,:;-?!\n"
strip = string.whitespace + string.punctuation + string.digits + s1
dict = {}
with open(os.path.abspath("text/generation_pi.txt"),"r", encoding="utf-8") as f:
    for line in f:
        for word in line.lower().split():
            word = word.strip(strip)
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    l1 = list(dict.items())
    l1 = sorted(l1, key = lambda x:x[1], reverse=True)
    l1 = l1[:60]
    print(l1)
