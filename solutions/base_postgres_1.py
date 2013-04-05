#!/usr/bin/env python3
__author__ = 'petro-ew'
import os
import psycopg2
HOST = '127.0.0.1'
DB_NAME = 'firma1'
DB_USER = 'postgres'
DB_PASS = 'texnolog'

conn = psycopg2.connect(host=HOST,database=DB_NAME,user=DB_USER,password=DB_PASS)
curs = conn.cursor()

"""Добавляем запись в таблицу БД """
s = 'AAA'
curs.execute('''INSERT INTO log_table (manager_short_fio, text_log,  start_machine) VALUES('%s', 'Машина включена', now())''' % s)
conn.commit()

"""Закрываем соединение с БД"""
curs.close()
conn.close()
