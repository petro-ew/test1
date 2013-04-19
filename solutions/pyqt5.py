#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import sys
import os
import psycopg2

from PyQt4.QtCore import QSettings

def store_ini():
    #s = QSettings()
    s = QSettings("pyqt4.ini", QSettings.IniFormat)
    #s.settings(QSettings.IniFormat, QSettings.UserScope, "MySoft", "Star Runner")
    s.setValue("base/login", "postgres")
    s.setValue("base/password", "texnolog")
    s.setValue("base/ip", "127.0.0.1")
    s.setValue("base/name", "firma1")


def read_ini():
    """



    :rtype : object
    :return:
    """
    s = QSettings("pyqt4.ini", QSettings.IniFormat)
    base_login = str(s.value("base/login", "postgres"))
    base_password = str(s.value("base/password", "texnolog"))
    ip_base = str(s.value("base/ip", "127.0.0.1"))
    base_name = str(s.value("base/name", "firma1"))
    l1 = (base_login, base_password, ip_base, base_name)
    #print(base_login, base_password, ip_base, base_name)
    return l1


def sql_data(sql):
    l_db = read_ini()
    print(l_db)
    HOST = l_db[2]        #'127.0.0.1'
    DB_NAME = l_db[3]     #'firma1'
    DB_USER = l_db[0]     #'postgres'
    DB_PASS = l_db[1]     #'texnolog'
    print(HOST, DB_NAME, DB_USER, DB_PASS)
    try:
        conn = psycopg2.connect(host=HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    except:
        print("Не могу подключиться к базе данных!! Do not connect to Database!!")
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records

from PyQt4 import QtGui, QtCore, uic

Form, Base = uic.loadUiType("pyqt5.ui")

class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """

        :type self: object MainWindow
        :param parent:
        """
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        def refresh_mtab():
            #формируем sql запрос
            sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work FROM public.akt_uslug;'
            #sql = 'SELECT * FROM manager_fio'
            #print(sql)
            #записываем полученные данные от базы данных в таблицу манагеров
            data = sql_data(sql)
            #print(len(data))
            self.tableWidget.setRowCount(len(data))
            """
            for row in range(len(data)):
                i = row
                for column in range(row):
                    item = data[(row)]
                    print("item=",item)
                    self.table.setItem(1, 0, QtGui.QTableWidgetItem(self.led.text()))
            """
            rows = len(data)
            cols = len(data[1])
            entries = data
            self.tableWidget.setRowCount(len(entries))
            self.tableWidget.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget.setItem(i, j, item)

                    #index = self.tableWidget.index(row, column, QtCore.QModelIndex())
                    #self.tableWidget.setData(index, (row + 1) * (column + 1))
                    #print(data)
                    #for raw in data:
                        #manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active = raw
                        #print(manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active)
                        #print(raw)

        def cell_was_clicked(row, column):
            """

            :param row: строка ячейки таблицы на которую нажали
            :param column: столбец ячейки таблицы на которую нажали
            """
            #----------------------------------------------------------------
            #Записываем данные в переменные
            m_id = self.tableWidget.item(row, 0).text()
            m_name = self.tableWidget.item(row, 1).text()
            m_otchestvo = self.tableWidget.item(row, 2).text()
            m_family = self.tableWidget.item(row, 3).text()
            m_shortname = self.tableWidget.item(row, 4).text()
            m_login = self.tableWidget.item(row, 5).text()
            m_admin = self.tableWidget.item(row, 6).text()
            m_lastkp = self.tableWidget.item(row, 7).text()
            m_lastdog = self.tableWidget.item(row, 8).text()
            #-------------------------------------------------------------

            #---------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
           # d_manager = {"id": m_id, "name": m_name, "otchestvo": m_otchestvo, "family": m_family, "shortname": m_shortname, "login": m_login, "active": m_active,
           #              "admin": m_admin, "lastkp": m_lastkp, "lastdog": m_lastdog, "email": m_email,"tel": m_tel}
            #-----------------------------------------------------------------------------------------------------

            #----------------------------------------------------------
            #Записываем данные в LineEdits

            self.tableWidget_one.setItem(0, 0, QtGui.QTableWidgetItem(str(m_id)))
            self.tableWidget_one.setItem(0, 1, QtGui.QTableWidgetItem(str(m_name)))
            self.tableWidget_one.setItem(0, 2, QtGui.QTableWidgetItem(str(m_otchestvo)))
            self.tableWidget_one.setItem(0, 3, QtGui.QTableWidgetItem(str(m_family)))
            self.tableWidget_one.setItem(0, 4, QtGui.QTableWidgetItem(str(m_shortname)))
            self.tableWidget_one.setItem(0, 5, QtGui.QTableWidgetItem(str(m_login)))
            self.tableWidget_one.setItem(0, 6, QtGui.QTableWidgetItem(str(m_admin)))
            self.tableWidget_one.setItem(0, 7, QtGui.QTableWidgetItem(str(m_lastkp)))
            self.tableWidget_one.setItem(0, 8, QtGui.QTableWidgetItem(str(m_lastdog)))

            #-----------------------------------------------------------

            #----------------------------------------------------------------------------------------------
            #Отладочный принт выдает номер столбца и колонки ячейки на которую нажала мышка
            #print("Row %d and Column %d was clicked" % (row, column))
            #item = self.tableWidget.item(row, column).text()
            #print (item, d_manager)
            #-----------------------------------------------------------------------------------------------

        #----------------------------------------------------------------------------------------------------
        #Запрещаем редактировать ячейки таблицы манагеров
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #----------------------------------------------------------------------------------------------------
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton_exit.setToolTip("Нажав эту кнопку покидаем программу")
        #-----------------------------------------------------------------------------------------------------
        #Устанавливаем количество столбцов таблиц
        self.tableWidget.setColumnCount(8)
        self.tableWidget_one.setColumnCount(8)
        #-----------------------------------------------------------------------------------------------------
        #Выставляем ширину столбцов для каждого участка
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().resizeSection(0, 90)
        self.tableWidget.horizontalHeader().resizeSection(4, 150)
        self.tableWidget.horizontalHeader().resizeSection(1, 250)
        self.tableWidget.horizontalHeader().resizeSection(2, 80)
        self.tableWidget_one.horizontalHeader().resizeSection(0, 90)
        self.tableWidget_one.horizontalHeader().resizeSection(4, 150)
        self.tableWidget_one.horizontalHeader().resizeSection(1, 250)
        self.tableWidget_one.horizontalHeader().resizeSection(2, 80)
        #-----------------------------------------------------------------------------------------------------
        #Наименование столбцов
        self.tableWidget.setHorizontalHeaderLabels(('Дата сдачи', 'Услуга', 'ID \n карты' , 'ФИО\n менеджера', 'Адрес объекта',  'ФИО \n Клиента', 'Дата \n поступления \n в работу', 'Работа\n выполнена'))
        self.tableWidget_one.setHorizontalHeaderLabels(('Дата сдачи', 'Услуга', 'ID \n карты' , 'ФИО\n менеджера', 'Адрес объекта',  'ФИО \n Клиента', 'Дата \n поступления \n в работу', 'Работа\n выполнена'))
        #-----------------------------------------------------------------------------------------------------
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL("clicked()"), refresh_mtab)
        self.tableWidget.cellClicked.connect(cell_was_clicked)


if __name__ == "__main__":
    import sys
    #store_ini()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
