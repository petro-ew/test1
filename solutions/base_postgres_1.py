#!/usr/bin/env python3
__author__ = 'petro-ew'
import os
import psycopg2
import math
def sql_data(sql):
    HOST = '192.168.0.33'
    DB_NAME = 'newnav'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'

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

"""Добавляем запись в таблицу БД """
#s = 'AAA'
sql = "SELECT id_st, b_wgs84,  l_wgs84, h_wgs84 FROM stations WHERE id_st = 'RNII';"
#curs.execute('''INSERT INTO log_table (manager_short_fio, text_log,  start_machine) VALUES('%s', 'Машина включена', now())''' % s)
data = sql_data(sql)
print(data)
rows = len(data)
cols = len(data[0])
for i, row in enumerate(data):
                for j, col in enumerate(row):
                    #print(col)
                    print("j=",j)
                    if j < 3 and j != 0:
                        col = float(col)
                        col = (col * 180) / (math.pi)
                        print(col)
                    #print(row)
                    #print(col)

"""Закрываем соединение с БД"""
