#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
""""
52. Реализовать класс Account, представляющий собой банковский счет.
 В классе должны быть четыре атрибута:
  ФИО владельца,
   номер счета,
    процент начисления
     и сумма в рублях.
   Необходимо реализовать следующие операции:
    сменить владельца счета,
     снять некоторую сумму денег со счета
     (проверять, что достаточно денег для снятия, в противном случае генерировать исключение),
      положить деньги на счет,
       начислить проценты,
        вывести на экран значения атрибутов.
"""
class MyError(Exception):pass
class Account: #bazoviy class
#    def __init__(self, user_fio, user_num_acc, user_percent, user_balance):
#        self.user_fio = "Petrovichev Viktor Viktorovich"
#        self.user_num_acc = 1234567890
#        self.user_percent = 5
#        self.user_balance = 30000
    def __init__(self, u_f, u_n_a, u_p, u_b):
        self.user_fio = u_f
        self.user_num_acc = u_n_a
        self.user_percent = u_p
        self.user_balance = u_b
        self.add = 0
        self.get = 0
        print("konstruktor bzovogo klassa")
    def fio(self):
        self.user_fio = "Petrovichev Viktor Viktorovich"
        return self.user_fio
    def num_acc(self):
        self.user_num_acc = 1234567890
        return self.user_num_acc
    def percent(self):
        self.user_percent = 5
        self.user_balance = self.user_percent * self.user_balance / 100 + self.user_balance
    def add_balance(self, add):
        print("счет : ", self.user_balance)
        print("добавить: ", add)
        self.user_balance = self.user_balance + add
        return self.user_balance

    def balance(self):
        return self.user_balance

    def print_page(self):
        print(self.user_fio, self.user_num_acc, self.user_balance, self.user_percent)

    def get_money(self, get):
        print("счет : ", self.user_balance)
        print("снять с баланса: ", get)
        self.user_balance = self.user_balance - get
        if self.user_balance < 0:
            raise MyError("Нет столько денег на счету !")
        return self.user_balance


acc = Account("Platonov", 987654321, 5, 1000)
setattr(acc, "fio", "Platonov Dmitry Vyacheslavovich")
print(getattr(acc, "fio"))
#print(getattr(acc, "balance")())
#acc.add_balance(60)
print(acc.balance())
acc.print_page()
print(acc.percent())
try:
    acc.get_money(10000)
    print(acc.balance())

except MyError as err:
    print ("Сообщение об ошибке")
    print("Нет столько денег на счету !")
