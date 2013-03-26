#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#strip = "\n"
__author__ = 'petro-ew'
import sys
import time
import os
import subprocess
import string
import shlex
import os.path
some_dir ='/home/petro-ew/work/2013/'
#some_dir ='d:\\py_work\\test1\\solutions\\'
some_dir2='/home/petro-ew/work/2013/text'
cmd = "cp /home/petro-ew/test1/solutions/kachalka_new.py /home/petro-ew/work/2013/text"
os.system(cmd)
#some_dir_all = '/home/petro-ew/work/crx2rnx/txt/all/'
zz_year=2013
year_fn = 13; # последние две цифры нужного вам года. двухзначный год что используется в команде grep .
#sta = "brap"
#fdata = 39
#ldata = 78
sta = sys.argv[1] #название станции
fdata = int(sys.argv[2]) #first data вводится как первый аргумент  (начало расчета)
ldata = int(sys.argv[3]) #last data вводится как второй аргумент (конец расчета)

print(time.gmtime())
#print ("\n year=",year," месяц= ",mon, " день= ", mday, " час= ", hour," минут ", min, " секунд= ", sec,"\n";)
def execscr(cmd):
    """
    :param cmd: команда исполняемая
    """
    args = shlex.split(cmd)
    print(args)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.communicate()[0]
    #print(out)

def fileopen(f_name, curday):
    """
    :param curday: дата на которую весь сыр бор
    :rtype : object
    :param f_name: имя файла
    :param simvol: на каком символе ищем переменную
    :return: переменную
    """
    l2  = []
    s1 = ' .,:;-?!\n'
    strip = string.whitespace + string.punctuation + s1
    simvol1 = "IOD slips <  10.0 deg*"
    simvol2 = "IOD slips >  10.0 deg"
    simvol3 = "IOD or MP slips <  10.0*"
    simvol4 = "IOD or MP slips >  10.0"

    with open(os.path.abspath(f_name), "r", encoding="utf-8") as f:
        for line in f:
            if simvol1 in line:
                q = line.strip(strip)
                l1 = q.split()
                z = q[:24]
                cort = (cday, l1[6])
                l2.insert(1, curday)
                l2.insert(2, l1[6])
            #    print(z, l1[6], cday, cort)
            if simvol2 in line:
                q = line.strip(strip)
                l1 = q.split()
                z = q[:24]
                cort = (cday, l1[6])
                l2.insert(3, l1[6])
           #     print(z, l1[6], cday, cort)
            if simvol3 in line:
                q = line.strip(strip)
                l1 = q.split()
                z = q[:24]
                cort = (cday, l1[6])
                l2.insert(4, l1[6])
          #      print(z, l1[6], cday, cort)
            if simvol4 in line:
                q = line.strip(strip)
                l1 = q.split()
                z = q[:24]
                cort = (cday, l1[7])
                l2.insert(5, l1[7])
         #       print(z, l1[7], cday, cort)
        #print(l2)
    return l2
#-------------------------------------

def filewriter(l):
    ll = ' '.join(l)
    print(ll)
    f_name = "plan.txt"
    with open(os.path.abspath(f_name), "a", encoding="utf-8") as f1:
        f1.write(ll + "\n")
        f1.close
    return

#--------------------------------------
print(os.getcwd())

i = fdata
print (sta, fdata, ldata)
while(i < ldata+1):
    print(i)
    cday = i  #cday новый\следующий current day
    if i < 10:
        #cday = str(i)
        ccday = "00" + str(cday)
#        i = int(i)
        print("i < 10 !!!", ccday, i)

    if i < 100:
        cday = str(i)
        ccday = "0"+cday
        #i = int(i)
    cmd01 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + ccday + "0." + str(year_fn) + "d.Z"
    cmd02 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + ccday + "0." + str(year_fn) + "g.Z"
    cmd03 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + ccday + "0." + str(year_fn) + "n.Z"
#    execscr(cmd01)
#    execscr(cmd02)
#    execscr(cmd03)
    os.chdir(some_dir)
    cmd04 = "/bin/uncompress /home/petro-ew/work/2013/*.Z"
#    os.system(cmd04)
    cmd05 = some_dir + "CRX2RNX " +  sta + ccday + "0." + str(year_fn) + "d"
#    os.system(cmd05)
    cmd06 = some_dir + "teqc +qc " +  sta + ccday + "0." + str(year_fn) + "o"
#    execscr(cmd06)
    cmd_rmz = "rm " + some_dir + "*.Z " + some_dir + "*.azi" + some_dir + "*.n" + some_dir + "*.mp1" + some_dir + "*.mp2" + some_dir + "*.ion" + some_dir + "*.o" + some_dir + "*.g" + some_dir + "*.sn1" + some_dir + "*.sn2" + some_dir + "*.iod" + some_dir + "*.ele"
    execscr(cmd_rmz)
    filename = some_dir + sta + ccday + "0." + str(year_fn) + "S"
    print(filename)
#    filename = some_dir + "text\\"+ sta + str(cday) + "0." + str(year_fn) + "S"
    l = fileopen(filename, ccday)
    print(l)
    filewriter(l)
    i += 1

cmd_rmz = "/bin/rm " + some_dir + "*.Z "
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.azi"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*." + str(year_fn) + "n"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.mp1"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.mp2"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.ion"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*." + str(year_fn) + "o"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*." + str(year_fn) + "g"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*." + str(year_fn) + "d"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.sn1"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.sn2"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.iod"
os.system(cmd_rmz)
cmd_rmz = "/bin/rm " + some_dir + "*.ele"
os.system(cmd_rmz)
cmd_plot = "/usr/bin/gnuplot 1.plt"
os.system(cmd_plot)
#cmd_mv = "/bin/mv " + some_dir + "plot-lines.png" + str(year_fn) + "S " + some_dir2 + "plot-lines" + sta + ".png"
cmd_mv = "/bin/mv " + some_dir + "plot-lines.png " + sta + "*" + str(year_fn) + "S " + some_dir2 + "plot-lines" + sta + ".png"
os.system(cmd_mv)
cmd_mv = "/bin/mv " + some_dir + "plan.txt " + some_dir2 + "plan" + sta + ".txt"
os.system(cmd_mv)
#cmd_rmptext = "/bin/rm " + some_dir + "plan.txt"
#os.system(cmd_rmptext)
#cmd_rmzs ="/bin/rm " + some_dir + "*.S"
#os.system(cmd_rmzs)

"""
#содержимое plt файла для гнуплота
set term png
set output "plot.png"
set xtics 1
plot [] [0:] "./plan.txt" using 1:2 with lines title "aaa", "./plan.txt" using 1:3 with lines title "bbb", "./plan.txt" using 1:4 with lines title "ccc"

"""
