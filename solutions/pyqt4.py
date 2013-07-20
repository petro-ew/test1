#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'petro-ew'
"""
Программа Админка
"""
import sys
import psycopg2
from PyQt4.QtCore import QSettings

#-----------------------------------------------------------------------------------------------------------------------
# qsettings пишем в ini файл значения по умолчанию,
# раньше не работали, и вроде сейчас не работают - руками пишу инишник
#  почему то сработали.
#-----------------------------------------------------------------------------------------------------------------------
def store_ini():
    #s = QSettings()
    s = QSettings("pyqt4.ini", QSettings.IniFormat)
    #s.settings(QSettings.IniFormat, QSettings.UserScope, "MySoft", "Star Runner")
    s.setValue("base/login", "postgres")
    s.setValue("base/password", "texnolog")
    s.setValue("base/ip", "127.0.0.1")
    s.setValue("base/name", "firma1")

#-----------------------------------------------------------------------------------------------------------------------
# qsettings читаем ini файл или берем значения по умолчанию, раньше не работали, почему то сработали.
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


from PyQt4 import QtGui, QtCore, uic

Form, Base = uic.loadUiType("pyqt4.ui")


class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """

        :type self: object MainWindow
        :param parent:
        """
        QtGui.QMainWindow.__init__(self, parent)
        def close():
            #app = QtGui.QApplication(sys.argv)
            """


            """
            qb = MessageBox()
            qb.show()
            #sys.exit(app.exec_())

        def dataline_man():
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
        #---------------------------------------------------------------------------------------------------------------
        # Удалить менеджера
        #---------------------------------------------------------------------------------------------------------------
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
        #---------------------------------------------------------------------------------------------------------------
        # обновить таблицу
        #---------------------------------------------------------------------------------------------------------------
        def refresh_mtab():
            #формируем sql запрос
            sql = 'SELECT manager_fio.manager_id,  manager_fio.manager_name, manager_fio.manager_otchestvo,' \
                ' manager_fio.manager_family, manager_fio.manager_short_fio, manager_fio.manager_login, ' \
                ' manager_fio.manager_admin_ok, manager_fio.manager_lastkp, manager_fio.manager_lastdog, ' \
                ' manager_fio.manager_active,  manager_fio.manager_tel,' \
                ' manager_fio.manager_email  FROM public.manager_fio;'
            #sql = 'SELECT * FROM manager_fio'
            #print(sql)
            #записываем полученные данные от базы данных в таблицу манагеров
            data = sql_data(sql)
            #print(len(data))
            self.tableWidget_manager.setRowCount(len(data))
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
            self.tableWidget_manager.setRowCount(len(entries))
            self.tableWidget_manager.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget_manager.setItem(i, j, item)

                    #index = self.tableWidget.index(row, column, QtCore.QModelIndex())
                    #self.tableWidget.setData(index, (row + 1) * (column + 1))
                    #print(data)
                    #for raw in data:
                    #manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active = raw
                    #print(manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active)
                    #print(raw)

        def cell_was_clicked_manager(row, column):
            """

            :param row: строка ячейки таблицы на которую нажали
            :param column: столбец ячейки таблицы на которую нажали
            """
            #-----------------------------------------------------------------------------------------------------------
            #очищаем данные что были записаны ранее в LineEdits
            self.lineEdit_name.clear()
            self.lineEdit_otchestvo.clear()
            self.lineEdit_family.clear()
            self.lineEdit_shortname.clear()
            self.lineEdit_number_m_lastkp.clear()
            self.lineEdit_number_m_lastdog.clear()
            self.lineEdit_tel_manager.clear()
            self.lineEdit_email_manager.clear()
            self.lineEdit_login_manager.clear()
            #-----------------------------------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            #Записываем данные в переменные
            m_id = self.tableWidget_manager.item(row, 0).text()
            m_name = self.tableWidget_manager.item(row, 1).text()
            m_otchestvo = self.tableWidget_manager.item(row, 2).text()
            m_family = self.tableWidget_manager.item(row, 3).text()
            m_shortname = self.tableWidget_manager.item(row, 4).text()
            m_login = self.tableWidget_manager.item(row, 5).text()
            m_admin = self.tableWidget_manager.item(row, 6).text()
            m_lastkp = self.tableWidget_manager.item(row, 7).text()
            m_lastdog = self.tableWidget_manager.item(row, 8).text()
            m_active = self.tableWidget_manager.item(row, 9).text()
            m_email = self.tableWidget_manager.item(row, 10).text()
            m_tel = self.tableWidget_manager.item(row, 11).text()
            #-----------------------------------------------------------------------------------------------------------

            #-----------------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
            d_manager = {"id": m_id, "name": m_name, "otchestvo": m_otchestvo, "family": m_family, "shortname": m_shortname, "login": m_login, "active": m_active,
                       "admin": m_admin, "lastkp": m_lastkp, "lastdog": m_lastdog, "email": m_email,"tel": m_tel}
            #-----------------------------------------------------------------------------------------------------------

            #-----------------------------------------------------------------------------------------------------------
            #Записываем данные в LineEdits
            self.lineEdit_name.insert(m_name)
            self.lineEdit_otchestvo.insert(m_otchestvo)
            self.lineEdit_family.insert(m_family)
            self.lineEdit_shortname.insert(m_shortname)
            self.lineEdit_number_m_lastkp.insert(m_lastkp)
            self.lineEdit_number_m_lastdog.insert(m_lastdog)
            self.lineEdit_tel_manager.insert(m_tel)
            self.lineEdit_email_manager.insert(m_email)
            self.lineEdit_login_manager.insert(m_login)
            #-----------------------------------------------------------------------------------------------------------

            #-----------------------------------------------------------------------------------------------------------
            #Отладочный принт выдает номер столбца и колонки ячейки на которую нажала мышка
            print("Row %d and Column %d was clicked manager" % (row, column))
            item = self.tableWidget_manager.item(row, column).text()
            print (item, d_manager)
            #-----------------------------------------------------------------------------------------------------------

        #---------------------------------------------------------------------------------------------------------------
        # Инженеры! ******************************************** Инженеры! *********************************************
        """
              engeneer_id integer NOT NULL DEFAULT nextval('auto_id_engeneer_fio'::regclass),
              engeneer_name text,
              engeneer_family text,
              engeneer_otchestvo text,
              engeneer_short_fio text,
              engeneer_login_ok boolean,
              engeneer_login text,
              engeneer_admin_ok boolean,
              engeneer_active boolean,
              CONSTRAINT engeneer_fio_pkey PRIMARY KEY (engeneer_id),
              CONSTRAINT login_engeneer_key UNIQUE (engeneer_login)
        """
#---------------------------------------------------------------------------------------------------------------
        #запись в переменные строчек - инженеры
        #---------------------------------------------------------------------------------------------------------------
        def write_for_strok_add():
            #-----------------------------------------------------------------------------------------------------------
            #Записываем данные в переменные

            eng_active = self.checkBox_login_na_eng.checkState()
            print("eng_active = ", eng_active)
            eng_admin = self.checkBox__eng_admin.checkState()
            print("eng_admin = ", eng_admin)

            eng_name = self.lineEdit_name_eng.text()
            eng_otchestvo = self.lineEdit_otchestvo_eng.text()
            eng_family = self.lineEdit_family_eng.text()
            eng_shortname = self.lineEdit_fio_eng.text()
            eng_login = self.lineEdit_login_eng.text()
            eng_tel = self.lineEdit_tel_eng.text()
            eng_email = self.lineEdit_email_eng.text()
            #eng_ip = self.lineEdit_ip_eng.text()
            print ("UPDATE ENG!!!! ",eng_admin, eng_active)
            if eng_active == 2:
                eng_active = "True"
            elif eng_active == 0:
                eng_active = "False"
            if eng_admin == 2:
                eng_admin = "True"
            elif eng_admin == 0:
                eng_admin = "False"
            print ("UPDATE ENG22222 eng_admin =", eng_admin, "eng_active = ", eng_active)
            #-----------------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
            d_strok_eng_add = {"name": eng_name, "otchestvo": eng_otchestvo, "family": eng_family, "shortname": eng_shortname, "login": eng_login, "active": eng_active,
                        "admin": eng_admin, "email": eng_email,"tel": eng_tel }
            #-----------------------------------------------------------------------------------------------------------
            return d_strok_eng_add
        #---------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------
        #запись в переменные строчек - инженеры
        #---------------------------------------------------------------------------------------------------------------
        def write_for_strok():
            #-----------------------------------------------------------------------------------------------------------
            #Записываем данные в переменные
            eng_id = self.label_id_eng.text()
            eng_active = self.checkBox_login_na_eng.checkState()
            print("eng_active = ", eng_active)
            eng_admin = self.checkBox__eng_admin.checkState()
            print("eng_admin = ", eng_admin)

            eng_name = self.lineEdit_name_eng.text()
            eng_otchestvo = self.lineEdit_otchestvo_eng.text()
            eng_family = self.lineEdit_family_eng.text()
            eng_shortname = self.lineEdit_fio_eng.text()
            eng_login = self.lineEdit_login_eng.text()
            eng_tel = self.lineEdit_tel_eng.text()
            eng_email = self.lineEdit_email_eng.text()
            #eng_ip = self.lineEdit_ip_eng.text()
            print ("UPDATE ENG!!!! ",eng_admin, eng_active)
            if eng_active == 2:
                eng_active = "True"
            elif eng_active == 0:
                eng_active = "False"
            if eng_admin == 2:
                eng_admin = "True"
            elif eng_admin == 0:
                eng_admin = "False"
            print ("UPDATE ENG22222 eng_admin =", eng_admin, "eng_active = ", eng_active)
            #-----------------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
            d_strok_eng = {"id": eng_id, "name": eng_name, "otchestvo": eng_otchestvo, "family": eng_family, "shortname": eng_shortname, "login": eng_login, "active": eng_active,
                        "admin": eng_admin, "email": eng_email,"tel": eng_tel }
            #-----------------------------------------------------------------------------------------------------------
            return d_strok_eng
        #---------------------------------------------------------------------------------------------------------------
        # обновление таблицы инженеров
        #---------------------------------------------------------------------------------------------------------------
        def refresh_etab():
            #формируем sql запрос
            #self.tableWidget_eng.setHorizontalHeaderLabels(('ID', 'Имя', 'Отчество', 'Фамилия',  'ФИО', 'Логин', 'Админ', 'Активен', 'Телефон', 'E-Mail'))
            sql = 'SELECT engeneer_fio.engeneer_id,  engeneer_fio.engeneer_name, engeneer_fio.engeneer_otchestvo,' \
                ' engeneer_fio.engeneer_family, engeneer_fio.engeneer_short_fio, engeneer_fio.engeneer_login, ' \
                ' engeneer_fio.engeneer_admin_ok,  ' \
                ' engeneer_fio.engeneer_active,  engeneer_fio.engeneer_tel,' \
                ' engeneer_fio.engeneer_email  FROM public.engeneer_fio;'
            #sql = 'SELECT * FROM manager_fio'
            #print(sql)
            #записываем полученные данные от базы данных в таблицу манагеров
            data = sql_data(sql)
            print(len(data))
            self.tableWidget_eng.setRowCount(len(data))
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
            self.tableWidget_eng.setRowCount(len(entries))
            self.tableWidget_eng.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = QtGui.QTableWidgetItem(str(col))
                    #print(col)
                    self.tableWidget_eng.setItem(i, j, item)

                    #index = self.tableWidget.index(row, column, QtCore.QModelIndex())
                    #self.tableWidget.setData(index, (row + 1) * (column + 1))
                    #print(data)
                    #for raw in data:
                    #manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active = raw
                    #print(manager_name, manager_family, manager_otchestvo, manager_short_fio, manager_admin_ok, manager_active)
                    #print(raw)

        def cell_was_clicked_eng(row, column):
            print("Zashli v func cell_was_clicked_eng!!!")
            refresh_etab()
            #-----------------------------------------------------------------------------------------------------------
            #очищаем данные что были записаны ранее в LineEdits
            self.lineEdit_name_eng.clear()
            self.lineEdit_otchestvo_eng.clear()
            self.lineEdit_family_eng.clear()
            self.lineEdit_fio_eng.clear()
            self.lineEdit_login_eng.clear()
            self.lineEdit_email_eng.clear()
            self.lineEdit_tel_eng.clear()
            #self.lineEdit_ip_eng.clear()

            #-----------------------------------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            #Записываем данные в переменные
            #d_strok_eng = write_for_strok()
            #print("d blin = ",  d_strok_eng)

            eng_id = self.tableWidget_eng.item(row, 0).text()
            eng_name = self.tableWidget_eng.item(row, 1).text()
            eng_otchestvo = self.tableWidget_eng.item(row, 2).text()
            eng_family = self.tableWidget_eng.item(row, 3).text()
            eng_shortname = self.tableWidget_eng.item(row, 4).text()
            eng_login = self.tableWidget_eng.item(row, 5).text()
            eng_admin = self.tableWidget_eng.item(row, 6).text()
            eng_active = self.tableWidget_eng.item(row, 7).text()
            eng_email = self.tableWidget_eng.item(row, 9).text()
            eng_tel = self.tableWidget_eng.item(row, 8).text()
            #eng_ip = self.tableWidget_eng.item(row, 12).text()
            #-----------------------------------------------------------------------------------------------------------

            #-----------------------------------------------------------------------------------------------------------
            #Создаем словарь с данными (авось потом пригодится ) аналог структуры в С-ях)
            d_eng = {"id": eng_id, "name": eng_name, "otchestvo": eng_otchestvo, "family": eng_family, "shortname": eng_shortname, "login": eng_login, "active": eng_active,
                        "admin": eng_admin, "email": eng_email,"tel": eng_tel}

            #-----------------------------------------------------------------------------------------------------------
            #ddd_eng(d_eng)
            #-----------------------------------------------------------------------------------------------------------
            #print ("ENG_ADMIN = ", eng_admin)
            #print ("ENG_ACTIVE = ", eng_active)

            if eng_active == "True":
                #print("зашли в иф на True")
                self.checkBox_login_na_eng.setCheckState(2)
                #self.checkBox_ok.setCheckState(2)  # пока не получается сделать так ччто бы когда ид_акт_услуг труе одноразово включался чек бокс на труе с возможностью переключения
            if eng_active == "False":
                self.checkBox_login_na_eng.setCheckState(0)  #поменял на фалсе

            if eng_admin == "True":
                #print("зашли в иф на True")
                self.checkBox__eng_admin.setCheckState(2)
                #self.checkBox_ok.setCheckState(2)  # пока не получается сделать так ччто бы когда ид_акт_услуг труе одноразово включался чек бокс на труе с возможностью переключения
            if eng_admin == "False":
                self.checkBox__eng_admin.setCheckState(0)  #поменял на фалсе

            #Записываем данные в LineEdits
            self.lineEdit_name_eng.insert(eng_name)
            self.lineEdit_otchestvo_eng.insert(eng_otchestvo)
            self.lineEdit_family_eng.insert(eng_family)
            self.lineEdit_fio_eng.insert(eng_shortname)
            self.lineEdit_login_eng.insert(eng_login)
            self.lineEdit_tel_eng.insert(eng_tel)
            self.lineEdit_email_eng.insert(eng_email)
            self.label_id_eng.setText(eng_id)
            #self.lineEdit_ip_eng.insert(eng_ip)
            #-----------------------------------------------------------------------------------------------------------

            #-----------------------------------------------------------------------------------------------------------
            #Отладочный принт выдает номер столбца и колонки ячейки на которую нажала мышка
            print("Row %d and Column %d was clicked engeneer" % (row, column))
            item = self.tableWidget_eng.item(row, column).text()
            print (item, d_eng)
            #-----------------------------------------------------------------------------------------------------------
        def update_eng():
            #d_eng = {"id": eng_id, "name": eng_name, "otchestvo": eng_otchestvo, "family": eng_family, "shortname": eng_shortname, "login": eng_login, "active": eng_active,
            #            "admin": eng_admin, "email": eng_email,"tel": eng_tel}
            #d_eng = ddd_eng()
            #print("update_eng ddd_eng = ", d_eng)
            #id_eng = self.label_id_eng.text()
            d_eng  = write_for_strok()
            eng_id =  d_eng['id']
            eng_name = d_eng['name']
            eng_otchestvo = d_eng['otchestvo']
            eng_family = d_eng['family']
            eng_shortname = d_eng['shortname']
            eng_login = d_eng['login']
            eng_active = d_eng['active']
            eng_admin = d_eng['admin']
            eng_email = d_eng['email']
            eng_tel = d_eng['tel']

            #собстно сам запрос
            sql = "UPDATE engeneer_fio SET engeneer_active = '" + eng_active + "', engeneer_admin_ok = '" + eng_admin + "'," \
                " engeneer_name = '" + eng_name + "', engeneer_family = '" + eng_family + "', engeneer_otchestvo = '" + eng_otchestvo + "'," \
                " engeneer_short_fio = '" + eng_shortname + "', engeneer_login = '" + eng_login + "', engeneer_tel = '" + eng_tel + "', " \
                "engeneer_email = '" + eng_email + "' WHERE engeneer_id = " + eng_id + ";"
            print("запрос на апдейт инженеров sql = ", sql)
            sql_update(sql)
            refresh_etab()
        #---------------------------------------------------------------------------------------------------------------
        #Удаление инженера навсегда из базы!!!
        #---------------------------------------------------------------------------------------------------------------
        def eng_del():
            d_eng  = write_for_strok()
            eng_id =  d_eng['id']
            sql = "DELETE FROM engeneer_fio WHERE engeneer_id = " + eng_id + ";"
            sql_update(sql)
            refresh_etab()

        #---------------------------------------------------------------------------------------------------------------
        #Добавление нового менеджера
        #pushButton_add_eng
        def eng_add():
            d_eng  = write_for_strok_add()
            eng_name = d_eng['name']
            eng_otchestvo = d_eng['otchestvo']
            eng_family = d_eng['family']
            eng_shortname = d_eng['shortname']
            eng_login = d_eng['login']
            eng_active = d_eng['active']
            eng_admin = d_eng['admin']
            eng_email = d_eng['email']
            eng_tel = d_eng['tel']

            """
            "INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar')
            sql = "UPDATE engeneer_fio SET engeneer_active = '" + eng_active + "', engeneer_admin_ok = '" + eng_admin + "'," \
                " engeneer_name = '" + eng_name + "', engeneer_family = '" + eng_family + "', engeneer_otchestvo = '" + eng_otchestvo + "'," \
                " engeneer_short_fio = '" + eng_shortname + "', engeneer_login = '" + eng_login + "', engeneer_tel = '" + eng_tel + "', " \
                "engeneer_email = '" + eng_email + "' WHERE engeneer_id = " + eng_id + ";"

            sql = "INSERT INTO engeneer_fio (engeneer_active, engeneer_admin_ok, engeneer_name, engeneer_family," \
                  " engeneer_otchestvo, engeneer_short_fio, engeneer_login, engeneer_tel, engeneer_email)" \
                  " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                  (eng_active, eng_admin, eng_name, eng_family, eng_otchestvo, eng_shortname, eng_login,eng_tel,eng_email)
            """
            sql = "INSERT INTO engeneer_fio (engeneer_active, engeneer_admin_ok, engeneer_name, engeneer_family," \
                  " engeneer_otchestvo, engeneer_short_fio, engeneer_login, engeneer_tel, engeneer_email)" \
                  " VALUES ('" + eng_active + "', '" + eng_admin + "', '" + eng_name + "', '" + eng_family + "', '"\
                  + eng_otchestvo + "', '" + eng_shortname + "', '" + eng_login + "', '" + eng_tel + "', '" + eng_email + "');"


            print("запрос на ДОБАВЛЕНИЕ инженеров sql = ", sql)
            sql_update(sql)
            refresh_etab()
        #---------------------------------------------------------------------------------------------------------------
        self.setupUi(self)
        #---------------------------------------------------------------------------------------------------------------
        # ставим титл главного окна программы
        self.setWindowTitle('Программа модуль для КДМ ДБ для Администратора без разрешения руководства не трогать')
        # Манагеры! ******************************************* Манагеры! **********************************************
        #---------------------------------------------------------------------------------------------------------------
        # Запрещаем редактировать ячейки таблицы манагеров
        self.tableWidget_manager.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #---------------------------------------------------------------------------------------------------------------
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton_exit.setToolTip("Нажав эту кнопку покидаем программу")
        #self.setToolTip("Главное Окно")
        self.lineEdit_name.setToolTip("Введите Имя")
        self.lineEdit_otchestvo.setPlaceholderText("Введите Отчество")
        self.lineEdit_shortname.setPlaceholderText("Введите Короткое Имя")
        #---------------------------------------------------------------------------------------------------------------
        # Устанавливаем количество столбцов таблицы манагеров
        self.tableWidget_manager.setColumnCount(12)
        #---------------------------------------------------------------------------------------------------------------
        # Делаем заголовки над каждым столбцом таблицы манагеров
        self.tableWidget_manager.setHorizontalHeaderLabels(('ID', 'Имя', 'Отчество', 'Фамилия',  'ФИО', 'Логин', 'Админ', '№КП', '№Дог', 'Активен', 'Телефон', 'e-mail'))
        #---------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по ячейки таблицы манагеров, а именно функцию cell_was_clicked_manager
        self.tableWidget_manager.cellClicked.connect(cell_was_clicked_manager)
        #---------------------------------------------------------------------------------------------------------------
        #QtCore.QObject.connect(self.tableWidget_manager, QtCore.SIGNAL(cellClicked(int,int)), this, QtCore.SLOT(myCellClicked(int,int)))

        #QtCore.QObject.connect(self.lineEdit_name, QtCore.SIGNAL("returnPressed()"), lineedit1)
        #QtCore.QObject.connect(self.lineEdit_otchestvo, QtCore.SIGNAL("returnPressed()"), lineedit2)
        #QtCore.QObject.connect(self.pushButton_table_refresh, QtCore.SIGNAL("clicked()"), lineedit2)
        #---------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по кнопке Добавить манагра, а именно функцию dataline_man
        QtCore.QObject.connect(self.pushButton_insert_table1, QtCore.SIGNAL("clicked()"), dataline_man)
        #---------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по кнопке Удалить манагра, а именно функцию manager_del
        QtCore.QObject.connect(self.pushButton_manager_delete, QtCore.SIGNAL("clicked()"), manager_del)
        #---------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по кнопке Обновить таблицу, обновляем таблицу манагеров, вызывая функцию refresh_mtab
        QtCore.QObject.connect(self.pushButton_table1_refresh, QtCore.SIGNAL("clicked()"), refresh_mtab)
        #---------------------------------------------------------------------------------------------------------------
        ################################################################################################################
        #******** Инженеры! ************************ Инженеры! *********************************************************
        ################################################################################################################
        #----------------------update eng-------------------------------------------------------------------------------
        #Назначаем действием на клик мышки по кнопке Обновить данные о инженере, обновляем таблицу манагеров, вызывая функцию refresh_etab
        QtCore.QObject.connect(self.pushButton_edit_eng_table, QtCore.SIGNAL("clicked()"), update_eng)
        #---------------------------------------------------------------------------------------------------------------
        #Назначаем действием на клик мышки по кнопке Добавить данные о инженере pushButton_add_eng , обновляем таблицу манагеров, вызывая функцию refresh_etab
        QtCore.QObject.connect(self.pushButton_add_eng, QtCore.SIGNAL("clicked()"), eng_add)
        #---------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по кнопке Обновить таблицу, обновляем таблицу манагеров, вызывая функцию refresh_etab
        QtCore.QObject.connect(self.pushButton_refresh_eng_table, QtCore.SIGNAL("clicked()"), refresh_etab)
        #---------------------------------------------------------------------------------------------------------------
        #Назначаем действие на клик мыши по кнопке pushButton_eng_del Удалить Инженера из Базы, обновляем таблицу вызывая функцию refresh_etab()
        QtCore.QObject.connect(self.pushButton_eng_del, QtCore.SIGNAL("clicked()"), eng_del)
        #---------------------------------------------------------------------------------------------------------------
        # Устанавливаем количество столбцов таблицы манагеров
        self.tableWidget_eng.setColumnCount(12)
        #---------------------------------------------------------------------------------------------------------------
        # Запрещаем редактировать ячейки таблицы манагеров
        self.tableWidget_eng.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #---------------------------------------------------------------------------------------------------------------
        # Делаем заголовки над каждым столбцом таблицы манагеров
        #self.tableWidget_eng.setHorizontalHeaderLabels(('ID', 'Имя', 'Отчество', 'Фамилия',  'ФИО', 'Логин', 'Админ', '№КП', '№Дог', 'Активен', 'Телефон', 'e-mail'))
        self.tableWidget_eng.setHorizontalHeaderLabels(('ID', 'Имя', 'Отчество', 'Фамилия',  'ФИО', 'Логин', 'Админ', 'Активен', 'Телефон', 'E-Mail'))
        #----------------------------------------------------------------------------------------------------------------------------------
        # Назначаем действием на клик мышки по ячейки таблицы манагеров, а именно функцию cell_was_clicked_manager
        self.tableWidget_eng.cellClicked.connect(cell_was_clicked_eng)
        #----------------------------------------------------------------------------------------------------------------------------------
        #нажимаем на кнопку обновить информацию о пользователе - pushButton_edit_eng_table

if __name__ == "__main__":
    import sys
    #store_ini()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

