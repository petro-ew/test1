#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
class MyClass:
    x = 10  # атрибут класса
    def __init__(self):
        self.y = 20 #аттрибут экземпляра класса
c1 = MyClass()
c2 = MyClass()
print(c1.x, c2.x)
MyClass.x = 88
print(c1.x, c2.x)
print(c1.y, c2.y)
c1.y = 88
print(c1.y, c2.y)
MyClass.x = 88
c1.x = 200
c2.x = 300
if c1.x < c2.x:
    print("ura!")
print(c1.x, MyClass.x)
#-------------------------------------------------------
class MyClass2:
    def __init__(self, value1, value2): #конструктор
        self.x = value1
        self.y = value2
c = MyClass2(100, 300) #создаем экземпляр класса
print(c.x, c.y)
#-------------------------------------------------------
class MyClass3:
    def __init__(self):
        print("Vizvan metod __init__()")
    def __del__(self):
        print("Vizvan metod __del__()")
c1 = MyClass3()
del c1
c2 = MyClass3()
c3 = c2
del c2
del c3

#-------------------------------------------------------
class Class1: #Базовый класс
    def func1(self):
        print("Metod func1() klassa Class1")
    def func2(self):
        print("Metod func2() klassa Class1 ")
class Class2(Class1): #Класс Class2 наследует Class1
    def func3(self):
        print("Metod func3() klassa Class2 ")
c =  Class2() # Cozdaem ekzemplyar class2
c.func1() #vivedet metod func1 class1
c.func2()
c.func3()
#--------------------------------------------------------

class Class4:
    def __init__(self):
        print("konstruktor bazovogo klassa")
    def func1(self):
        print("metod func1() bazovogo klassa")

class Class5(Class4):         #class5 nasleduet class4
    def __init__(self):
        print("konstructor proizvodnogo classa")
        Class4.__init__(self) #vizivaem konstruktor bazovogo klassa
    def func1(self):
        print("metod func1() klassa Class5")
        Class4.func1(self)    #vizivaem metod bazovogo klassa

c = Class5() #Cozdaem ekzemplyar klassa Class5
c.func1()    #vizivaem metod func1()

#---------------------------------------------
class Vehicle: #Базовый класс
    def __init__(self):
        print("konstruktor bazovogo klassa Vehicle")
    def move_forvard(self):
        print("look forward")
        print ("if none == MOVE FORVARD!")
        #print("Move FORWARD!")
    def move_back(self):
        print("Move BACKWARD")

class Car(Vehicle):
    def __init__(self):
        print("konstructor proizvodnogo klassa Car ot Vehicle")
        super().__init__()
    def move_forvard(self):
        print("metod proverit benzin")
        print("zevesti esli ne zavedena")
    #    Vehicle.move_forvard(self)
        super().move_forvard()
    def benzoback(self):


car = Car()
car.move_forvard()#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
class MyClass:
    x = 10  # атрибут класса
    def __init__(self):
        self.y = 20 #аттрибут экземпляра класса
c1 = MyClass()
c2 = MyClass()
print(c1.x, c2.x)
MyClass.x = 88
print(c1.x, c2.x)
print(c1.y, c2.y)
c1.y = 88
print(c1.y, c2.y)
MyClass.x = 88
c1.x = 200
c2.x = 300
if c1.x < c2.x:
    print("ura!")
print(c1.x, MyClass.x)
#-------------------------------------------------------
class MyClass2:
    def __init__(self, value1, value2): #конструктор
        self.x = value1
        self.y = value2
c = MyClass2(100, 300) #создаем экземпляр класса
print(c.x, c.y)
#-------------------------------------------------------
class MyClass3:
    def __init__(self):
        print("Vizvan metod __init__()")
    def __del__(self):
        print("Vizvan metod __del__()")
c1 = MyClass3()
del c1
c2 = MyClass3()
c3 = c2
del c2
del c3

#-------------------------------------------------------
class Class1: #Базовый класс
    def func1(self):
        print("Metod func1() klassa Class1")
    def func2(self):
        print("Metod func2() klassa Class1 ")
class Class2(Class1): #Класс Class2 наследует Class1
    def func3(self):
        print("Metod func3() klassa Class2 ")
c =  Class2() # Cozdaem ekzemplyar class2
c.func1() #vivedet metod func1 class1
c.func2()
c.func3()
#--------------------------------------------------------

class Class4:
    def __init__(self):
        print("konstruktor bazovogo klassa")
    def func1(self):
        print("metod func1() bazovogo klassa")

class Class5(Class4):         #class5 nasleduet class4
    def __init__(self):
        print("konstructor proizvodnogo classa")
        Class4.__init__(self) #vizivaem konstruktor bazovogo klassa
    def func1(self):
        print("metod func1() klassa Class5")
        Class4.func1(self)    #vizivaem metod bazovogo klassa

c = Class5() #Cozdaem ekzemplyar klassa Class5
c.func1()    #vizivaem metod func1()

#---------------------------------------------
class Vehicle: #Базовый класс
    def __init__(self):
        print("konstruktor bazovogo klassa Vehicle")
    def move_forvard(self):
        print("look forward")
        print ("if none == MOVE FORVARD!")
        #print("Move FORWARD!")
    def move_back(self):
        print("Move BACKWARD")

class Car(Vehicle):
    def __init__(self):
        print("konstructor proizvodnogo klassa Car ot Vehicle")
        super().__init__()
    def move_forvard(self):
        print("metod proverit benzin")
        print("zevesti esli ne zavedena")
    #    Vehicle.move_forvard(self)
        super().move_forvard()
    def benzoback(self):


car = Car()
car.move_forvard()