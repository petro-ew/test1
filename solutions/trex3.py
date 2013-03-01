#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
try:
    raise ValueError("opisanie iskluchenia")
except ValueError as msg:
    print(msg)

class MyError(Exception):
    def __init__(self, value):
        self.msg = value
    def __str__(self):
        return self.msg
try:
    raise MyError("Opisanie iskluchenia")
except MyError as err:
    print(err)
    print(err.msg)
raise MyError("Opisanie iskluchenia")
