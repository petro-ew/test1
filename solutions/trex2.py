#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
class MyClass:
    def __enter__(self):
        print("vizvan metod __enter__()")
        return self
    def __exit__(self, Type, Value, Trace):
        print("vizvan nmetod __exit__()")
        if Type is None:
            print("Iscluchenia ne vozniklo")
        else:
            print("Value =", Value)
            return False
print("posledovatelnost pri otsutsvii isklucheniya:")
with MyClass():
    print("Block vnutri with")
print("Posledovatelnost pri nalichii iskluchenia:")
with MyClass() as object:
    print("Block vnutri with")
    raise TypeError("Iskluchenie TypeError")

