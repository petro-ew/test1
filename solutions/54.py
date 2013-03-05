#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
"""
54. Одна запись в списке запланированных дел представляет собой экземпляр класса DailyItem,
 который содержит время начала и окончания работы,
  описание и признак выполнения.
   Реализовать класс DailySchedule,
    представляющий собой план работ на день.
     Реализовать методы
      добавления,
      удаления
       и изменения планируемой работы.
        При добавлении проверять корректность временных рамок
   (они не должны пересекаться с уже запланированными мероприятиями).
   В случае попытки добавить мероприятие,
    пересекающееся по времени с уже запланированными,
     генерировать исключение.
      Реализовать метод поиска свободного промежутка времени.
       Условие поиска задает размер искомого интервала,
        а также временные рамки, в которые он должен попадать.
         Метод поиска возвращает экземпляр класса DailyItem с пустым описанием вида работ.
         Реализовать метод Redo (еще раз),
          возвращающий список дел, не выполненных в течении дня.

"""
"""
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
"""
import sys
import copy
from colorama import Fore, Back, Style, init

class DailyItem:
    #запись в списке запланированных дел.
    def __init__(self, t_st, t_ed, w_data, pr_w_ok):
        self.t_start = t_st
        self.t_end = t_ed
        self.work_data = w_data
        self.pr_work_ok = pr_w_ok
        print("konstruktor bzovogo klassa DailyItem")
    def time_start(self):
        print("date start время начала", self.t_start)
        return  self.t_start
    def time_end(self):
        print("date end окончания работы", self.t_end)
        return  self.t_end
    def data(self):
        print("data описание", self.work_data)
        return self.work_data
    def pr_end(self):
        print("priznak vipolneniya признак выполнения", self.pr_work_ok)
        return self.pr_work_ok

class DailyShedule:

    def __init__(self):
        self.sp_time_start = []
        self.sp_time_stop = []
        self.sp_work_data = []
        self.sp_pr_work_ok = []
        self.lt_svob = []
        self.sp_plan = []
        #self.old_name = "искомое значение"
        #self.new_name = "новое значение"
        print("konstruktor bzovogo klassa  план работ на день")
    def add(self):
        print("add work добавления")
        self.sp_time_start.append(di.t_start)
        self.sp_time_stop.append(di.t_end)
        self.sp_work_data.append(di.work_data)
        self.sp_pr_work_ok.append(di.pr_work_ok)
#        t_st = 6
#        t_ed = 6.30
#        w_data = "Завтрак"
#        pr_w_ok = "не лезет"
        #di = DailyItem(6, 6.30, "Завтрак", "не лезет")
        #DailyItem(t_st, t_ed, w_data, pr_w_ok)
    def delete(self, name):
        if name in self.sp_work_data:
            ind = self.sp_work_data.index(name)
            del self.sp_work_data[ind]
            del self.sp_pr_work_ok[ind]
            del self.sp_time_start[ind]
            del self.sp_time_stop[ind]
            print(Fore.RED + Style.BRIGHT + "удалено:" + Fore.RESET + Style.RESET_ALL, name)

    def change(self, old_name, new_name):
        print(old_name)
        if old_name in self.sp_work_data:
            ind = self.sp_work_data.index(old_name)
            del self.sp_work_data[ind]
            self.sp_work_data.insert(ind, new_name)
            print("есть такое!", old_name, "index = ", ind, "new_name = ", new_name)

        print("change work изменения планируемой работы")

    def plan(self):
        #print("plan work  план работ на день")
        #print(self.sp_time_start, self.sp_time_stop, self.sp_work_data, self.sp_pr_work_ok)
        for i in range(len(self.sp_time_start)):
            l2 = (self.sp_time_start[i], self.sp_time_stop[i], self.sp_work_data[i], self.sp_pr_work_ok[i])
            #l2 = list(l2)
            self.sp_plan.append(l2)
        spmn = copy.deepcopy(self.sp_plan)
        mn = set(spmn)
        spmn = list(mn)
        print(Fore.GREEN + Style.BRIGHT + "План работ на день" + Fore.RESET + Style.RESET_ALL, spmn)

    def search(self):
        print("search time метод поиска свободного промежутка времени.")
        lt_stop = copy.deepcopy(self.sp_time_stop)
        lt_start = copy.deepcopy(self.sp_time_start)
        lt_start.append(24)
        lt_stop.insert(0,0)
        #print(lt_stop, lt_start)
        for i in range(len(lt_stop)):

            l1 = (lt_stop[i], lt_start[i])
            l1 = list(l1)
            self.lt_svob.append(l1)
            #print(l1)
        print(Fore.BLUE + Style.BRIGHT + "свободные промежутки времени: " + Fore.RESET + Style.RESET_ALL, self.lt_svob)

    def redo(self):
        print("redo возвращающий список дел, не выполненных в течении дня.")


dsh = DailyShedule()
di = DailyItem(6, 6.30, "Завтрак", "не лезет")
dsh.add()
di = DailyItem(10, 19.30, "Работа", "отбой")
dsh.add()
di = DailyItem(22, 22.30, "Ужин", "не лезет")
dsh.add()
dsh.plan()
dsh.change("Работа", "Отдых блин")

dsh.delete("Ужин")
dsh.plan()
di = DailyItem(24, 24.30, "2-й Ужин", "не лезет")
dsh.add()
dsh.plan()
dsh.search()
#dsh.add(6, 6.30, "Завтрак", "не лезет")
#dsh.add(10, 19.30, "Работа", "отбой")
#dsh.add(22, 22.30, "Ужин", "не лезет")




dsh.plan()