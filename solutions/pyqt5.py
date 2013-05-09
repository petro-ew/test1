#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import sys
import os
import psycopg2
#-----------------------------------------------------------------------------
# чтение из INI файла, почему то на массе операционных систем на работает ...

from PyQt4.QtCore import QSettings
#----------------------------------------------------------------------------------
#Функция которая достает из файла ini настройки.
def store_ini():
    #s = QSettings()
    s = QSettings("pyqt4.ini", QSettings.IniFormat)
    #s.settings(QSettings.IniFormat, QSettings.UserScope, "MySoft", "Star Runner")
    s.setValue("base/login", "postgres")
    s.setValue("base/password", "texnolog")
    s.setValue("base/ip", "127.0.0.1")
    s.setValue("base/name", "firma1")


def read_ini():
    s = QSettings("pyqt4.ini", QSettings.IniFormat)
    base_login = str(s.value("base/login", "postgres"))
    base_password = str(s.value("base/password", "texnolog"))
    ip_base = str(s.value("base/ip", "127.0.0.1"))
    base_name = str(s.value("base/name", "firma1"))
    l1 = (base_login, base_password, ip_base, base_name)
    #print(base_login, base_password, ip_base, base_name)
    return l1

#---------------------------------------------------------------
#Исполнение SQL запросов, коннект к базе данных
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
        print("Не могу подключиться к базе данных(def sql_data(sql))!! Do not connect to Database!!")
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records
#---------------------------------------
def sql_update(sql):
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
        print("Не могу подключиться к базе данных(def sql_data(sql))!! Do not connect to Database!!")
    cur = conn.cursor()
    cur.execute(sql)
    #records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return
#---------------------------------------


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore, uic
#--------------------------------------------------------
#Подгружаем графический интерфейс из XML файла "pyqt5.ui"
Form, Base = uic.loadUiType("pyqt5.ui")

class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """

        :type self: object MainWindow
        :param parent:
        """
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        #--------------------------------------------------------------
        #Прозрачная форма (transparent) - пока не нужно
        #palette = QPalette(self.palette())
        #palette.setColor(palette.Background, Qt.transparent)
        #self.setPalette(palette)
        #--------------------------------------------------------------


        def check_box_on_off_on(id_akt_uslug):
            """
            #------------------------------------------------------------------
            #Узнаем стоит ли флажок ок
            #------------------------------------------------------------------
            :param id_akt_uslug: передается в функцию , береться из таблицы с базы. или с нее же но с таблицы программа текстом.
            """
            id_akt_uslug = id_akt_uslug
            sql = 'SELECT usl_perfomed FROM public.akt_uslug WHERE id_akt_uslug =' + id_akt_uslug + ';'
            #try:
            data = sql_data(sql)
            #except:
                #print("Не могу подключиться к базе данных!! Do not connect to Database!!")
            #делаем неактивным checkBox_ok если флажок стоит.
            data = data[0]
            data = data[0]
            data = str(data)
            print("data=", data)
            if data == "True":
                print("зашли в иф на True")
                self.checkBox_ok.setEnabled(False)
            else:
                self.checkBox_ok.setEnabled(True)
            return
            #---------------------------------------------------------------------------------------------------

        def write_table_one(id_akt_uslug):
            id = id_akt_uslug
            print("id =", id)
            sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work, akt_uslug.usl_perfomed, akt_uslug.id_akt_uslug FROM public.akt_uslug WHERE id_akt_uslug =' + id + ';'
            data = sql_data(sql)
            self.tableWidget_one.setRowCount(len(data))
            rows = len(data)
            cols = len(data[0])
            print("rows=" + str(rows) + "cols=" + str(cols))
            entries = data
            self.tableWidget_one.setRowCount(len(entries))
            self.tableWidget_one.setColumnCount(cols)
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget_one.setItem(i, j, item)
            #включаем сортировку в таблицы после ее заполнения что бы не было багов и косяков
            self.tableWidget_one.setSortingEnabled(True)

        #---------------------------------------------------------------------------
        #функция очищения таблицы tableWidget_one.
        def clear_table_one():
            #удаляем то что было в таблице до нас.
            n_one = self.tableWidget_one.rowCount()
            print("n_one = ", n_one)
            for i in range(0, n_one):
                self.tableWidget_one.removeRow(0)
            #отключаем сортировку в таблице перед ее заполнением что бы не было багов и косяков
            self.tableWidget_one.setSortingEnabled(False)
        #-----------------------------------------------------------------------------------------
        #Функция очищения записей таблицы TableWidget
        def clear_table():
            #удаляем то что было в таблице до нас.
            n = self.tableWidget.rowCount()
            print("n = ", n)
            for i in range(0, n):
                self.tableWidget.removeRow(0)
            #отключаем сортировку в таблице перед ее заполнением что бы не было багов и косяков
            self.tableWidget.setSortingEnabled(False)
        #--------------------------------------------------------------------------------------------
        #Функция записи результатов запроса в таблицу
        def write_table(data):
            data = data
            print(data)
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
           # self.tableWidget.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget.setItem(i, j, item)
            #включаем сортировку в таблицы после ее заполнения что бы не было багов и косяков
            self.tableWidget.setSortingEnabled(True)

        #----------------------------------------------------------------------------------------------
        #функция ее мы вызываем когда нажимаем на кнопку обновить таблицу TableWidget

        def refresh_mtab():
            #очищаем таблицу и отключаем сортировку в таблице, вызвав функцию clear_table()
            clear_table()
            #формируем sql запрос
            sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work, akt_uslug.usl_perfomed,  id_akt_uslug FROM public.akt_uslug WHERE usl_perfomed = false;'
            #print(sql)
            #записываем полученные данные от базы данных в таблицу манагеров
            #try:
            data = sql_data(sql)
            print(data)
            data_str = []
            for i in data:
                i = str(i)
                data_str.append(i)
            print("data_str refresh_mtab= ", data_str)
            #except:
            #    print("Не могу подключиться к базе данных!! Do not connect to Database!!")
            #print(len(data))
            #вызываем функцию заполнения таблицы из данных базы данных
            #try:
            write_table(data)
            self.tableWidget_one.removeRow(0)
            #except:
            #    print("Не могу подключиться к базе данных, по этому нет данных!! Do not connect to Database!!")

        def refresh_mtab_one():
            #очищение и обновление маленькой таблицы.
            id = self.tableWidget_one.item(0, 8).text()
            sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work, akt_uslug.usl_perfomed, akt_uslug.id_akt_uslug FROM public.akt_uslug WHERE id_akt_uslug =' + id + ';'
            data = sql_data(sql)
            self.tableWidget_one.setRowCount(len(data))
            rows = len(data)
            cols = len(data[0])
            print("rows=" + str(rows) + "cols=" + str(cols))
            entries = data
            self.tableWidget_one.setRowCount(len(entries))
            self.tableWidget_one.setColumnCount(cols)
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget_one.setItem(i, j, item)
            #включаем сортировку в таблицы после ее заполнения что бы не было багов и косяков
            self.tableWidget_one.setSortingEnabled(True)


        def cell_was_clicked(row, column):
            """

            :param row: строка ячейки таблицы на которую нажали
            :param column: столбец ячейки таблицы на которую нажали
            """
            print("cell was clicked!")
            #----------------------------------------------------------------
            #Записываем данные в переменные
            m_name = self.tableWidget.item(row, 0).text()
            m_otchestvo = self.tableWidget.item(row, 1).text()
            m_family = self.tableWidget.item(row, 2).text()
            m_shortname = self.tableWidget.item(row, 3).text()
            m_login = self.tableWidget.item(row, 4).text()
            m_admin = self.tableWidget.item(row, 5).text()
            m_lastkp = self.tableWidget.item(row, 6).text()
            m_lastdog = self.tableWidget.item(row, 7).text()
            id_akt_uslug = self.tableWidget.item(row, 8).text()
            print("id_akt_uslug cell_was_clicked =", id_akt_uslug)
            #-------------------------------------------------------------
            #------------------------------------------------------------------
            #Узнаем стоит ли флажок ок
            check_box_on_off_on(id_akt_uslug)
            #---------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
            #d_manager = {"id": m_id, "name": m_name, "otchestvo": m_otchestvo, "family": m_family, "shortname": m_shortname, "login": m_login, "active": m_active,
            #             "admin": m_admin, "lastkp": m_lastkp, "lastdog": m_lastdog, "email": m_email,"tel": m_tel}
            #-----------------------------------------------------------------------------------------------------
            #Очистка таблицы tableWidgetOne
            clear_table_one()
            #----------------------------------------------------------
            #Записываем данные в tableWidget_one
            write_table_one(id_akt_uslug)
            #----------------------------------------------------------------------------------------
            """
            ok_true = self.tableWidget_one.item(0, 7).text()
            print ("was_clicked!! ok_true=", ok_true)
            if ok_true == 'True':
                print("IF сработал!")
                self.checkBox_ok.setEnabled(False)
            else:
                self.checkBox_ok.setEnabled(True)
            """
            #----------------------------------------------------------------------------------------------
            #Отладочный принт выдает номер столбца и колонки ячейки на которую нажала мышка
            #print("Row %d and Column %d was clicked" % (row, column))
            #item = self.tableWidget.item(row, column).text()
            #print (item, d_manager)
            #-----------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------
        #-Функция дл обновления услуги
        def eng_usl_update():
            """

                фуккция обновления
            """
            #------------------------------------------------------------------
            #Узнаем стоит ли флажок ок
            id = self.tableWidget_one.item(0, 8).text()
            check_box_on_off_on(id)
            #---------------------------------------------------------------------------------------------------
            ok_true = self.tableWidget_one.item(0, 7).text()
            print("ok_true= ", ok_true)
            if self.checkBox_ok.checkState():
                ok = "true"
                print("ok = ", ok)
                """
                SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
                data = ("O'Reilly", )
                cur.execute(SQL, data) # Note: no % operator
                """
                sql = "UPDATE akt_uslug SET usl_perfomed = 'True' WHERE id_akt_uslug = " + id + ";"
                #try:
                sql_update(sql)
                #print(data)
                #except:
                #print("Не могу подключиться к базе данных!! Do not connect to Database!!")
                #обновляем таблицу tableWidget

                self.checkBox_ok.setChecked(0)
                refresh_mtab()
                refresh_mtab_one()
            else:
                ok = "false"
                print("ok = ", ok)

        """
        def changeTitle(self, value):
            if self.checkBox_ok.isChecked():
                self.setWindowTitle('Checkbox')
            else:
                self.setWindowTitle('')
        """
        #----------------------------------------------------------------------------------------
        #-функция выбора показания всех услуг
        def eng_usl_all():
            if self.checkBox_all.checkState():
                al = "true"
                print("al = ", al)
                #формируем SQL запрос
                sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work, akt_uslug.usl_perfomed,  id_akt_uslug FROM public.akt_uslug'
                 #записываем полученные данные от базы данных в таблицу манагеров
                try:
                    data = sql_data(sql)
                except:
                    print("Не могу подключиться к базе данных!! Do not connect to Database!!")
                #print(len(data))
                #очищаем таблицу и отключаем сортировку в таблице, вызвав функцию clear_table()
                clear_table()
                #вызываем функцию заполнения таблицы из данных базы данных
                write_table(data)

            else:
                al = "false"
                print("al = ", al)
                #формируем SQL запрос
                sql = 'SELECT akt_uslug.srok_sdachi,  akt_uslug.name_uslugi, akt_uslug.id_client_card,' \
                ' akt_uslug.fio_manager, akt_uslug.adres_object, akt_uslug.fio_contact_lico, ' \
                ' akt_uslug.start_work, akt_uslug.usl_perfomed,  id_akt_uslug FROM public.akt_uslug WHERE usl_perfomed = false;'
                 #записываем полученные данные от базы данных в таблицу манагеров
                try:
                    data = sql_data(sql)
                except:
                    print("Не могу подключиться к базе данных!! Do not connect to Database!!")
                #print(len(data))
                #очищаем таблицу и отключаем сортировку в таблице, вызвав функцию clear_table()
                clear_table()
                #вызываем функцию заполнения таблицы из данных базы данных
                try:
                    write_table(data)
                except:
                    print("Не могу подключиться к базе данных, по этому нет данных!! Do not connect to Database!!")

        #----------------------------------------------------------------------------------------------------
        self.setWindowTitle('Программа модуль для КДМ ДБ для инженеров')
        #Запрещаем редактировать ячейки таблицы манагеров и таблицы выделенного манагера.
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_one.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #----------------------------------------------------------------------------------------------------
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton_exit.setToolTip("Нажав эту кнопку покидаем программу")
        self.connect(self.pushButton_update, QtCore.SIGNAL("clicked()"), eng_usl_update)
        #-----------------------------------------------------------------------------------------------------
        #Устанавливаем количество столбцов таблиц
        self.tableWidget.setColumnCount(9)
        self.tableWidget_one.setColumnCount(9)
        #-----------------------------------------------------------------------------------------------------
        #Выставляем ширину столбцов для каждого участка
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().resizeSection(0, 90)
        self.tableWidget.horizontalHeader().resizeSection(4, 150)
        #self.tableWidget.horizontalHeader().resizeSection(1, 250)
        self.tableWidget.horizontalHeader().resizeSection(2, 80)
        self.tableWidget_one.horizontalHeader().resizeSection(0, 90)
        self.tableWidget_one.horizontalHeader().resizeSection(4, 150)
        #self.tableWidget_one.horizontalHeader().resizeSection(1, 250)
        self.tableWidget_one.horizontalHeader().resizeSection(2, 80)
        #-----------------------------------------------------------------------------------------------------
        #Наименование столбцов
        self.tableWidget.setHorizontalHeaderLabels(('Дата сдачи', 'Услуга', 'ID \n карты', 'ФИО\n менеджера', 'Адрес объекта', 'ФИО \n Клиента', 'Дата \n поступления \n в работу', 'Работа\n выполнена', 'ID'))
        self.tableWidget_one.setHorizontalHeaderLabels(('Дата сдачи', 'Услуга', 'ID \n карты', 'ФИО\n менеджера', 'Адрес объекта', 'ФИО \n Клиента', 'Дата \n поступления \n в работу', 'Работа\n выполнена', 'ID'))
        #-----------------------------------------------------------------------------------------------------
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL("clicked()"), refresh_mtab)
        self.tableWidget.cellClicked.connect(cell_was_clicked)
        #----------------------------------------------------
        #реакция на чекбокс ОК то есть работа выполнена.
        #self.connect(self.checkBox_ok, QtCore.SIGNAL('stateChanged(int)'), eng_usl_update)
        self.connect(self.checkBox_ok, QtCore.SIGNAL('toggled(bool)'), eng_usl_update)
        #self.connect(self.checkBox_all, QtCore.SIGNAL('stateChanged(int)'), eng_usl_all)
        self.connect(self.checkBox_all, QtCore.SIGNAL('toggled(bool)'), eng_usl_all)

if __name__ == "__main__":
    import sys
    store_ini()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


    """
табличные данные
ALTER TABLE akt_uslug ADD COLUMN id_akt_uslug integer;
ALTER TABLE akt_uslug ALTER COLUMN id_akt_uslug SET NOT NULL;
ALTER TABLE akt_uslug ALTER COLUMN id_akt_uslug SET DEFAULT nextval('auto_id_akt_uslug'::regclass);
-- ALTER TABLE akt_uslug DROP COLUMN srok_sdachi;

ALTER TABLE akt_uslug ADD COLUMN srok_sdachi date;
-- ALTER TABLE akt_uslug DROP COLUMN akt1;

ALTER TABLE akt_uslug ADD COLUMN akt1 boolean;
-- Column: akt2

-- ALTER TABLE akt_uslug DROP COLUMN akt2;

ALTER TABLE akt_uslug ADD COLUMN akt2 boolean;
-- Column: usl_master

-- ALTER TABLE akt_uslug DROP COLUMN usl_master;

ALTER TABLE akt_uslug ADD COLUMN usl_master text;
-- Column: id_client_card

-- ALTER TABLE akt_uslug DROP COLUMN id_client_card;

ALTER TABLE akt_uslug ADD COLUMN id_client_card integer;


-- ALTER TABLE akt_uslug DROP COLUMN akt_uslug_ms;

ALTER TABLE akt_uslug ADD COLUMN akt_uslug_ms text;

-- ALTER TABLE akt_uslug DROP COLUMN name_uslugi;

ALTER TABLE akt_uslug ADD COLUMN name_uslugi text;

-- ALTER TABLE akt_uslug DROP COLUMN sdelana;

ALTER TABLE akt_uslug ADD COLUMN sdelana text;

-- ALTER TABLE akt_uslug DROP COLUMN payment;

ALTER TABLE akt_uslug ADD COLUMN payment text;

-- ALTER TABLE akt_uslug DROP COLUMN create_time;

ALTER TABLE akt_uslug ADD COLUMN create_time date;

-- ALTER TABLE akt_uslug DROP COLUMN fio_manager;

ALTER TABLE akt_uslug ADD COLUMN fio_manager text;

- ALTER TABLE akt_uslug DROP COLUMN start_work;

ALTER TABLE akt_uslug ADD COLUMN start_work date;

-- ALTER TABLE akt_uslug DROP COLUMN start_work_check;

ALTER TABLE akt_uslug ADD COLUMN start_work_check boolean;


---------------------------

-- ALTER TABLE contact_lico DROP COLUMN adres_cl;

ALTER TABLE contact_lico ADD COLUMN adres_cl text;
"""
