__author__ = 'petro-ew'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cmath
import math
#закомментировал на время... надо разобраться...
"""
Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "]
Digits = [Zero, One]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: py1.py <number>")
except ValueError as err:
    print(err, "in", digits)

"""
"""
print("hello", "world")
l1 = [1,3,4,5,-3,-7]
print("список l1=",l1)
l1.extend([1,2,3,4])
print("список extend l1=",l1)

print("как я понял начинается с нуля и сначла идет позиция вставляемого данного в объекте список , а потом его занчение.")
l1.insert(3,-2)
print("список insert на 4ю позицию (-2) l1=",l1)
l1.pop()
print("pop удаляет и возвращает последний элемент списка")
print("список pop l1=",l1)
l1.reverse()
print("список reverse изменяет порядок следования элементов на обратный l1=",l1)

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            print("i=",i)
            return i
        except ValueError as err:
            print(err)
age = get_int("enter your age: ")
print("randomaizing games :-)")
import random
x = random.randint(1, 6)
print("x=",x)
y = random.choice(["zzz","yyy","sss","ccc","hhh"])
print("y=",y)
"""
"""
def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except(IOError, OSError) as err:
        print(err)
        return[]
    finally:
        if fh is not None:
            fh.close()
    print(lines)
    return lines
z = read_data("zzzz")
"""
"""
a = 9
if 0 <= a <= 10:
    print ("True")
else:
    print("False")
x = 56545.75764/3.276983785123
x = "{0:1.15f}".format(x)
print(x)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1=[]
x=0
while x < n:
    x=x+1
    l1.append(x)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1=[]
for x in range(1,n+1):
    l1.append(x)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
l1 = range(1,n+1)
l1 = list(l1)
print(l1)
l2 = [x ** 2 for x in l1]
print(l2)
"""
"""
#список квадратов чисел от 1 до 10
n=int(input())
print("n=",n)
print([x ** 2 for x in list(range(1,n+1))])
"""
"""
#список квадратов чисел от 1 до 10
n = int(input())
print("n=", n)
l2 = [x ** 2 for x in range(1, n + 1)]
print(l2)
"""
"""
n = int(input())
l1 = []
l2 = []
for x in range(1,n+1):
    if x % 2 == 0: #x % 2 проверка на четность.
        l1.append(x)
    else:
        l2.append(x)
print("четные = l1=", l1)
print("нечетные=", l2)
"""
#=======================================================
#31-01-2013
#=======================================================
"""
1. - сделано
два списка l1 и l2
возможно различной длины n и m
сделать l3 такой что у нег 1й элемент равен первому элементу из списка l1,
 а второй элемент равен первому элементу из списка l2 и тд
после окончания одного из списка,
следуют оставшиеся элементы из второго списка
"""
"""
#просто про работу со списками
#можно брать каждый второй элемент списка
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = len(l1[1::2])
y = l1[1::2]
print(l1 , z, y)
"""

"""
n = int(input())
m = int(input())
l1 = range(1, n+1)
l1 = list(l1)
l2 = range(1, m+1)
l2 = list(l2)
print(l1, l2)
l3 = []
if n<=m:
    z=n
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
else:
    z=m
    for i in range(len(l2)):
        l3.append(l1[i])
        l3.append(l2[i])
i=i+1
if n>m:
    for x in range(i, i+1):
        l3.append(l1[x])
else:
    for x in range(i, i+1):
        l3.append(l2[x])
print(l3)
"""
"""
2. - есть вопросы по поводу математики
написать функцию, которая решает квадратное уравнение.
аргументы функции коэффициэнты функци a, b, c
корни возвращал в виде списка.
если корней нет - в виде пустого списка
если корень 1 то список из 1 элемента
если 2 корня возвращаем из двух элементов,
которые равны корням, первым идет меньший корень.
a*x**2+b*x+c = 0
discr = b**2 - 4*a*c
"""
"""
a = int(input())
b = int(input())
c = int(input())
l1 = []
print("a, b, c = ",a, b, c)

def quake1(a, b, c):
    discr = b**2-4*a*c
    print("discr = ", discr)
    if discr == 0:
        x1 = (-b)/(2*a)
        print(x1)
        l1.append(x1)
        print(l1)
        return l1
    else:
        if discr > 0:
            x1= (-b+math.sqrt(discr))/2*a
            l1.append(x1)
            x2= (-b-math.sqrt(discr))/2*a
            l1.append(x2)
            print(l1)
            return l1
        else:
            print(l1)
            return l1

quake1(a, b, c)
"""
#variant - 2
"""
a = int(input())
b = int(input())
c = int(input())
l1 = []
print("a, b, c = ",a, b, c)
discr = b**2-4*a*c
print("discr = ", discr)
if discr == 0:
    x1 = (-b)/(2*a)
    print(x1)
    l1.append(x1)
    print(l1)
else:
    if discr > 0:
        x1= (-b+math.sqrt(discr))/2*a
        l1.append(x1)
        x2= (-b-math.sqrt(discr))/2*a
        l1.append(x2)
        print(l1)
    else:
        print(l1)

"""
"""
3. - сделана.
есть л1 состоящий уникальных элементов
есть л2 тоже из уникальных элементов
получить список л3,
состоящих из всех элементов входящих в оба списка одновременно
"""
"""
l2 = [1, 2, 3, 8, 5, 10]
l1 = [4, 3, 9, 5]
l3 = []
for i in range(len(l1)):
    for y in range(len(l2)):
        if l1[i] == l2[y]:
            l3.append((l1[i]))
print(l3)
"""
"""
#убирает повторы
l2 = [1, 2, 3, 8, 5, 10, 256]
l1 = [4, 3, 9, 5, 89, 298, 1234, 1, 1, 2, 1, 2, 3, 10]
l3 = l2+l1
l3=list(set(l3))
print(l3)
"""
"""
4. - сделана
cловарь д1 состоящий из пары имя - значение.
построить словарь д2,
 так, что у него ключи и значения поменяны местами по отношению к словарю д1.
"""
"""
d1 = dict({"id": 2011, "name": "red book", "size": 386})
print(d1)
d2 = {} # создали словарь
l1 = []
l2 = []
for key, value in d1.items():
#    print("key, value= ", key, value)
    l1.append(key)
    l2.append(value)
#print(l1,l2)
for i in range(len(l1)):
#    print(l2[i],l1[i])
    d2[l2[i]] = l1[i]
print(d2)
"""
#new version
d = dict({"id": 2011, "name": "red book", "size": 386})
print(d)
inverted_d = {v: k for k, v in d.items()}
print(inverted_d)
#eshe version
a_dict = {'a': 1, 'b': 2, 'c': 3}
print(a_dict)
d3 = {value:key for key, value in a_dict.items()}
print(d3)
"""
"""
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
"""
"""
2. В словаре d значениями являются целые числа.
 Вывести на экран все пары ключ:значение из d
 в порядке возрастания значений.
  Пример:
d = {'aaa':5, 'ddd':2, 'qqq':3}
Вывод программы:
'ddd':2
'qqq':3
'aaa':5
"""
d = {'aaa':5, 'ddd':2, 'qqq':3}
print(d)
l1 = []
l2 = []
for key, value in d.items():
    print("key, value= ", key, value)
    l1.append(key)
    l2.append(value)
print(l1,l2)
l2.sort(key = lambda x: x[5])
print(l2)
#sorted(l2, key=lambda x:


"""
3. Программа запрашивает натуральное число n.
 Выводит список всех простых чисел, меньших либо равных n.
"""
"""
4. Программа запрашивает два целых числа a и b.
 Найти и вывести на экран наибольший общий делитель a и b.
"""
"""
5. Программа запрашивает натуральное число n.
 Вывести все тройки чисел
  a, b, c такие,
   что a<=n, b<=n, c<=n
   и a**2 + b**2 равно c**2
"""
"""
6. Написать функцию, возвращающую сумму квадратов элемента списка.
"""
"""
7. Написать функцию,
 возвращающую минимальный и максимальный элемент списка,
  в виде кортежа из двух элементов.
"""
"""
8. Написать функцию,
принимающую в качестве аргумента список и возвращающую список такой же длины,
 построенный по следующему принципу:
Первый элемент списка = первый элемент аргумента
Второй элемент списка = последний элемент аргумента
Третий элемент списка = второй элемент списка
Четвертый элемент списка = предпоследний элемент списка
и так далее
Пример к 8-й задаче:
Аргумент: [1,2,3,4,5]
Результат: [1,5,2,4,3]
"""
