#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
#from __future__ import print_function
from colorama import Fore, Back, Style, init
import sys

init()

# Fore, Back and Style are convenience classes for the constant ANSI strings that set
#     the foreground, background and style. The don't have any magic of their own.
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

NAMES = {Fore.BLACK: 'black', Fore.RED: 'red', Fore.GREEN: 'green', Fore.YELLOW: 'yellow', Fore.BLUE: 'blue', Fore.MAGENTA: 'magenta', Fore.CYAN: 'cyan', Fore.WHITE: 'white', Fore.RESET: 'reset', Back.BLACK: 'black', Back.RED: 'red', Back.GREEN: 'green', Back.YELLOW: 'yellow', Back.BLUE: 'blue', Back.MAGENTA: 'magenta', Back.CYAN: 'cyan', Back.WHITE: 'white', Back.RESET: 'reset'}
# show the color names
sys.stdout.write('        ')
for foreground in FORES:
    sys.stdout.write('%s%-7s' % (foreground, NAMES[foreground]))
    print()
# make a row for each background color
for background in BACKS:
    sys.stdout.write('%s%-7s%s %s' % (background, NAMES[background], Back.RESET, background))
# make a column for each foreground color
for foreground in FORES:
    sys.stdout.write(foreground)
# show dim, normal bright
for brightness in STYLES:
    sys.stdout.write('%sX ' % brightness)
    sys.stdout.write(Style.RESET_ALL + ' ' + background)
    print(Style.RESET_ALL)

print()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')

init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')

"""
#----------ascii----------------------------------------------
print ('\033[1;30mGray like Ghost\033[1;m')
print ('\033[1;31mRed like Radish\033[1;m')
print ('\033[1;32mGreen like Grass\033[1;m')
print ('\033[1;33mYellow like Yolk\033[1;m')
print ('\033[1;34mBlue like Blood\033[1;m')
print ('\033[1;35mMagenta like Mimosa\033[1;m')
print ('\033[1;36mCyan like Caribbean\033[1;m')
print ('\033[1;37mWhite like Whipped Cream\033[1;m')
print ('\033[1;38mCrimson like Chianti\033[1;m')
print ('\033[1;41mHighlighted Red like Radish\033[1;m')
print ('\033[1;42mHighlighted Green like Grass\033[1;m')
print ('\033[1;43mHighlighted Brown like Bear\033[1;m')
print ('\033[1;44mHighlighted Blue like Blood\033[1;m')
print ('\033[1;45mHighlighted Magenta like Mimosa\033[1;m')
print ('\033[1;46mHighlighted Cyan like Caribbean\033[1;m')
print ('\033[1;47mHighlighted Gray like Ghost\033[1;m')
print ('\033[1;48mHighlighted Crimson like Chianti\033[1;m')
#----------------------------------------------------------------
"""
