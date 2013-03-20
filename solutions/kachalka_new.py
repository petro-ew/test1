#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#strip = "\n"
__author__ = 'petro-ew'
import sys
import time
import os
import subprocess
import shlex
import os.path
some_dir ='/home/petro-ew/work/2013/'
some_dir2='/home/petro-ew/work/crx2rnx'
some_dir_all = '/home/petro-ew/work/crx2rnx/txt/all/'
zz_year=2013
year_fn = 13; # последние две цифры нужного вам года. двухзначный год что используется в команде grep .
#fday  #first day
#lday #last day
#cday # новый\следующий current day
sta = sys.argv[1] #название станции
fdata = int(sys.argv[2]) #first data вводится как первый аргумент  (начало расчета)
ldata = int(sys.argv[3]) #last data вводится как второй аргумент (конец расчета)
print(time.gmtime())
#print ("\n year=",year," месяц= ",mon, " день= ", mday, " час= ", hour," минут ", min, " секунд= ", sec,"\n";)
def execscr(cmd):
    args = shlex.split(cmd)
    print(args)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.communicate()[0]
    print(out)


def fileopen(f_name, simvol):
    with open(a, "r", encoding="utf-8") as f:
        for line in f:
            if simvol in line:
                line = line.strip("\n")
                print(line)
    return
#--------------------------------------
print(os.getcwd())

i  = fdata
print (sta, fdata, ldata)
while(i < ldata):
    print(i)
    cday = i #current day
    if cday < 100:
        cday = "0"+str(cday)
    cmd01 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + str(cday) + "0." + str(year_fn) + "d.Z"
    cmd02 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + str(cday) + "0." + str(year_fn) + "g.Z"
    cmd03 = "wget -t 1  --ftp-user=petro-ew --ftp-password=fvbjksdx ftp://192.168.0.21/rinex/" + str(zz_year) + "/" + str(cday) + "/" +  sta + str(cday) + "0." + str(year_fn) + "n.Z"

    execscr(cmd01)
    execscr(cmd02)
    execscr(cmd03)
    os.chdir(some_dir)
    cmd04 = "/bin/uncompress /home/petro-ew/work/2013/*.Z"
    os.system(cmd04)
    #execscr(cmd04)
    cmd05 = some_dir + "CRX2RNX " +  sta + str(cday) + "0." + str(year_fn) + "d"
    os.system(cmd05)
    #execscr(cmd05)
    cmd06 = some_dir + "teqc +qc " +  sta + str(cday) + "0." + str(year_fn) + "o"
    execscr(cmd06)
    cmd_rmz = "rm " + some_dir + "*.Z " + some_dir + "*.azi" + some_dir + "*.n" + some_dir + "*.mp1" + some_dir + "*.mp2" + some_dir + "*.ion" + some_dir + "*.o" + some_dir + "*.g" + some_dir + "*.sn1" + some_dir + "*.sn2" + some_dir + "*.iod" + some_dir + "*.ele"
    execscr(cmd_rmz)
    filename =
    fileopen(, )

    i+=1
"""
j = fdata

while (j < ldata):
	os.chdir(some_dir)
	cmd04 = "/bin/uncompress /home/petro-ew/work/2013/*.Z"
	os.system(cmd04)
	#execscr(cmd04)
	cmd05 = some_dir + "CRX2RNX " +  sta + str(cday) + "0." + str(year_fn) + "d"
	os.system(cmd05)
	#execscr(cmd05)
	cmd06 = some_dir + "teqc +qc " +  sta + str(cday) + "0." + str(year_fn) + "o"
	execscr(cmd06)
	cmd_rmz = "rm " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*d.Z " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*n " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*g " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*o " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*ion " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*iod " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*azi " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*ele " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*sn1 " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*sn2 " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*mp1 " + some_dir +  sta + str(cday) + "0." + str(year_fn) + "*mp2 "
	execscr(cmd_rmz)

	j+=1
	"""
os.system("/bin/chmod 777 *")
cmd_rmz = "/bin/rm " + some_dir + "*.Z "
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.azi"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir +  "*." + str(year_fn) + "n"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.mp1"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.mp2"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.ion"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir +   "*." +   str(year_fn) + "o"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir +  "*." +   str(year_fn) + "g"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir +   "*." +   str(year_fn) + "d"
os.system(cmd_rmz)

cmd_rmz ="/bin/rm " + some_dir + "*.sn1"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.sn2"
os.system(cmd_rmz)
cmd_rmz ="/bin/rm " + some_dir + "*.iod"
os.system(cmd_rmz)
cmd_rmz = "/bin/rm " + some_dir + "*.ele"
os.system(cmd_rmz)
#com  "some_dir2/day_kachalka.pl mend ".ARGV[0]." ".ARGV[1] 