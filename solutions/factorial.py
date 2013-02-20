#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

nf = 4
def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) * n

def fact2(n):
    return fact2(n - 1) * n if n > 1 else 1

print(fact2(nf))
