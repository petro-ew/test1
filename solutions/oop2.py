#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
52-1. ================================
добавить в класс car бензобак
 максимальный объем бензобака 50 литров
добавить метод для заправки бензобака
аргументом которого будет число с плавуещей точкой
которое обознаяает количество заливаемого топлива
или строку "FUll" если бензобак надо заправить полный
Добавить проверку наличия бензина в метод мув форвард
При создании экземпляра - бензобак пустой )

добавить заправочную станцию )
"""
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
        self.benz = 0
        super().__init__()
    def move_forvard(self):
        print("metod proverit benzin")
        if car.benz > 0:
            print("zevesti esli ne zavedena") #    Vehicle.move_forvard(self)
            super().move_forvard()
        else:
            print("zapravte mashinu!")
    def zapravka(self, benzto):
        print("metod zapravki")
        if benzto == "full":
            print("ya edu na Yamaika!")
            benzto = 50 - self.benz
            print("zaprivilis na ", benzto)
        if self.benz == 0:
            print("Nado zapravitsua!")
            #exit()
        if self.benz < 50:
            #print("zapravili do 50")
            self.benz = self.benz + benzto
            print("zapravilis na ", self.benz)
        else:
            print("Polniy bak zapravka ne treba")
        if self.benz > 50:
            print("Nelsya zalit bolshe 50 L!")
            self.benz = 50

    def youbenz(self):
        print("benzina v bake: ", self.benz)

        
car = Car()
car.youbenz()
car.zapravka(60)
car.youbenz()
#car.zapravka("full")

car.youbenz()


car.move_forvard()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

"""
52-1. ================================
добавить в класс car бензобак
 максимальный объем бензобака 50 литров
добавить метод для заправки бензобака
аргументом которого будет число с плавуещей точкой
которое обознаяает количество заливаемого топлива
или строку "FUll" если бензобак надо заправить полный
Добавить проверку наличия бензина в метод мув форвард
При создании экземпляра - бензобак пустой )

добавить заправочную станцию )
"""
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
        self.benz = 0
        super().__init__()
    def move_forvard(self):
        print("metod proverit benzin")
        if car.benz > 0:
            print("zevesti esli ne zavedena") #    Vehicle.move_forvard(self)
            super().move_forvard()
        else:
            print("zapravte mashinu!")
    def zapravka(self, benzto):
        print("metod zapravki")
        if benzto == "full":
            print("ya edu na Yamaika!")
            benzto = 50 - self.benz
            print("zaprivilis na ", benzto)
        if self.benz == 0:
            print("Nado zapravitsua!")
            #exit()
        if self.benz < 50:
            #print("zapravili do 50")
            self.benz = self.benz + benzto
            print("zapravilis na ", self.benz)
        else:
            print("Polniy bak zapravka ne treba")
        if self.benz > 50:
            print("Nelsya zalit bolshe 50 L!")
            self.benz = 50

    def youbenz(self):
        print("benzina v bake: ", self.benz)

        
car = Car()
car.youbenz()
car.zapravka(60)
car.youbenz()
#car.zapravka("full")

car.youbenz()


car.move_forvard()
