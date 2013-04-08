#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


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
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    #row_count = 0
    #for row in cur:
    #    row_count += 1
    #    print("row: %s    %s\n" % (row_count, row))
    #pprint.pprint(records)
    conn.commit()
    cur.close()
    conn.close()
    return records

    """
        def sql_data(sql):
        conn = psycopg2.connect("dbname=' ' user=' ' host=' ' password=' '");
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return(data)
    """


#from os import path, curdir

from PyQt4 import QtGui, QtCore, uic

Form, Base = uic.loadUiType("pyqt4.ui")


class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """

        :type self: object MainWindow
        :param parent:
        """
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton_exit.setToolTip("Нажав эту кнопку покидаем программу")
        #self.setToolTip("Главное Окно")
        self.lineEdit_name.setToolTip("Введите Имя")
        self.lineEdit_otchestvo.setPlaceholderText("Введите Отчество")
        self.lineEdit_shortname.setPlaceholderText("Введите Короткое Имя")


        def dataline():
            """
            :return: word
            """
            #self.label1.setText("<b>"+word+"<b>")
            if self.checkBox_acticve.checkState():
                mactive = "false"
            else:
                mactive = "true"
            if self.checkBox_admin.checkState():
                madmin = "true"
            else:
                madmin = "false"

            mname = self.lineEdit_name.text()
            motchestvo = self.lineEdit_otchestvo.text()
            mfamily = self.lineEdit_family.text()
            mshortname = self.lineEdit_shortname.text()
            d1 = {"name": mname, "otchestvo": motchestvo, "family": mfamily, "shortname": mshortname, "active": mactive,
                  "admin": madmin}
            print(d1)

        def manager_del():
            """

            функция удаления манагера из базы данных
            """
            if self.checkBox_acticve.checkState():
                mactive = "false"
            else:
                mactive = "true"
            if self.checkBox_admin.checkState():
                madmin = "true"
            else:
                madmin = "false"

            mname = self.lineEdit_name.text()
            motchestvo = self.lineEdit_otchestvo.text()
            mfamily = self.lineEdit_family.text()
            mshortname = self.lineEdit_shortname.text()
            d1 = {"name": mname, "otchestvo": motchestvo, "family": mfamily, "shortname": mshortname, "active": mactive,
                  "admin": madmin}
            print(d1)

        def refresh_mtab():
            #sql = 'SELECT manager_fio.manager_name, manager_fio.manager_family, manager_fio.manager_otchestvo,' \
            #          ' manager_fio.manager_short_fio, manager_fio.manager_admin_ok, manager_fio.manager_active FROM public.manager_fio;'
            """
            tableWidget->setColumnCount( 2 );
            tableWidget->setRowCount( 2 );
            QTableWidgetItem *newItem = new QTableWidgetItem( "Preved!" );
            tableWidget->setItem( 1, 1, newItem );
             for (row=0; row < rec_count; row++)
            {
                 for (col=0; col < 10; col++)
                {
                    strcpy(s, PQgetvalue(res, row, col));
                    StringGrid1->Cells[col][row+1] = s;
                }
            }
            """
            sql = 'SELECT * FROM manager_fio'
            sql = 'SELECT * FROM manager_fio'
            print(sql)
            data = sql_data(sql)
            print(len(data))
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
                    print(col)
                    self.tableWidget.setItem(i, j, item)

                    #index = self.tableWidget.index(row, column, QtCore.QModelIndex())
                    #self.tableWidget.setData(index, (row + 1) * (column + 1))
            #print(data)
            #for raw in data:
            #manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active = raw
                #print(manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active)
                #print(raw)

        #QtCore.QObject.connect(self.lineEdit_name, QtCore.SIGNAL("returnPressed()"), lineedit1)
        #QtCore.QObject.connect(self.lineEdit_otchestvo, QtCore.SIGNAL("returnPressed()"), lineedit2)

        #QtCore.QObject.connect(self.pushButton_table_refresh, QtCore.SIGNAL("clicked()"), lineedit2)
        QtCore.QObject.connect(self.pushButton_insert_table1, QtCore.SIGNAL("clicked()"), dataline)
        QtCore.QObject.connect(self.pushButton_manager_delete, QtCore.SIGNAL("clicked()"), manager_del)
        QtCore.QObject.connect(self.pushButton_table1_refresh, QtCore.SIGNAL("clicked()"), refresh_mtab)



if __name__ == "__main__":
    import sys
    #store_ini()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

