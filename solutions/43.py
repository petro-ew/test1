#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
"""
43.
 Написать функцию,
 получающую два аргумента - имя файла и строку s,
  и выводящую на экран все строки из файла,
   в которые содержат s
    в качестве подстроки.
"""

#strip = "\n"
def funcz(a, b):
    with open(a, "r", encoding="utf-8") as f:
        for line in f:
            if b in line:
                line = line.strip("\n")
                print(line)
    return

funcz(sys.argv[1], sys.argv[2])
