#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab:
__author__ = 'petro-ew'
"""
import matplotlib
matplotlib.matplotlib_fname()
'/home/petro-ew/test1/solutions/'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab as P
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
import os
import os.path
some_dir = "/home/petro-ew/test1/solutions/"
os.chdir(some_dir)
fname2 = cbook.get_sample_data('akko.slmp', asfileobj=False)
#fname2 = akko.slmp
#mu, sigma = 100, 15
#x = mu + sigma*np.random.randn(10000)

# the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1)
#plotfile(fname2, cols=(1,2,3,4,5), delimiter=' ',
#         names=['sl < 10', 'sl > 10', 'mp < 10', 'mp > 10'])
plotfile(fname2, cols=(1,2,3,4))

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ AKKO:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
"""
"""
import matplotlib.pyplot as plt

# Значения по оси X

X = [20.0, 40.0, 60.0, 80.0, 100.0]

# Набор значений по оси Y

Y_10 = [0.97252, 0.94238, 0.89927, 0.85197, 0.79784]
Y_20 = [0.96864, 0.93518, 0.89113, 0.84344, 0.78934]
Y_30 = [0.96395, 0.92770, 0.88278, 0.83473, 0.78075]

# Строим диаграмму

# Задаем исходные данные для каждой линии диаграммы, внешний вид линий и маркеров.
# Функция plot() возвращает кортеж ссылок на объекты класса matplotlib.lines.Line2D

line_10, line_20, line_30 = plt.plot(X, Y_10, 'bD:', X, Y_20, 'r^:', X, Y_30, 'go:')

# Задаем интервалы значений по осям X и Y

plt.axis([15.0, 105.0, 0.75, 1.0])

# Задаем заголовок диаграммы

plt.title('Зависимость плотности водных растворов этилового спирта от температуры')

# Задаем подписи к осям X и Y

plt.xlabel('Массовая доля этилового спирта, %')
plt.ylabel('Плотность, г/мл')

# Задаем исходные данные для легенды и ее размещение

plt.legend( (line_10, line_20, line_30), ('Температура 10 \00b0C', 'Температура 20 \00b0C', 'Температура 30 \00b0C'), loc = 'best')

# Включаем сетку

plt.grid()

# Сохраняем построенную диаграмму в файл

# Задаем имя файла и его тип

plt.savefig('spirit.png', format = 'png')
"""

"""
import numpy as np
import os
from matplotlib import rc
import matplotlib.pyplot as plt
fn = u'./test/solutions/akko.slmp'
channels = 4
rows = os.path.getsize(f)/2/channels
print rows
X = np.memmap(f, dtype=np.int16, mode='r', shape=(rows,ch), offset=0)
# Iarm=X[:,0]
# Kf=X[:,1]
# Sync=X[:,2]
# Omega=X[:,3]
plt.plot(X)
plt.show()
#plt.savefig(fn+'.png')
"""
import matplotlib.pyplot as plt
import numpy as np
import numpy
import pylab
from pylab import plotfile, show, gca
from pylab import *
from matplotlib import *
from numpy import *
from pylab import load           # warning, the load() function of numpy will be shadowed
from pylab import save
import matplotlib.pyplot as plt
from matplotlib import pyplot

#data1=10*np.random.rand(5)
#data2=10*np.random.rand(5)
#data3=10*np.random.rand(5)
data1 = numpy.genfromtxt('akko.txt', usecols = [1,]) 
data2 = numpy.genfromtxt('akko.txt', usecols = [2,])
data3 = numpy.genfromtxt('akko.txt', usecols = [3,])
locs = np.arange(1, len(data1)+1)
width = 0.27
# Задаем заголовок диаграммы
plt.title('AKKO',{'fontname':'Arial','fontsize':16})
#plt.title(u'AKKO')
# Задаем подписи к осям X и Y
#plt.xlabel(u'Дни с начала года')
#plt.ylabel(u'Значения')
plt.xlabel('Дни с начала года',{'fontname':'Arial','fontsize':16})
plt.ylabel('Значения',{'fontname':'Arial','fontsize':16})
# Включаем сетку
plt.grid()
plt.xticks(locs + width * 1.5, locs)
#ax = plt.subplot(1, 1, 1)
#p1, = plt.bar(locs, data1, width = width, label = 'ls < 10')
#p2, = plt.bar(locs + width, data2, width = width, color = 'red', label = 'sl > 10')
#p3, = plt.bar(locs + 2 * width, data3, width = width, color = 'green', label = 'mp < 10')
pylab.bar(locs, data1, width = width, label = 'ls < 10')
pylab.bar(locs + width, data2, width = width, color = 'red', label = 'ls > 10')
pylab.bar(locs + 2 * width, data3, width = width, color = 'green', label = 'mp > 10')
pylab.legend()
#handles, labels = ax.get_legend_handles_labels()
#handles, labels = plt.ax.get_legend_handles_labels()
#plt.ax.legend(handles[::-1], labels[::-1])
# Задаем исходные данные для легенды и ее размещение
#plt.legend( (p1, p2, p3), ('sl < 10', 'sl > 10', 'mp < 10 '), loc = 'best')

#plt.show()
#read_data = load("myfile.txt")
#data = numpy.genfromtxt('akko.txt', usecols = [0, 2,]) 
#plt.plot(data,data)
#plt.savefig('spirit.png', format = 'png')
plt.show()
plt.savefig('spirit.pdf', format = 'pdf')
"""
plt.rcParams['savefig.facecolor'] = "0.8"
def example_plot(ax, fontsize=12):
ax.plot([1, 2])
ax.locator_params(nbins=3)
ax.set_xlabel('x-label', fontsize=fontsize)
ax.set_ylabel('y-label', fontsize=fontsize)
ax.set_title('Title', fontsize=fontsize)
plt.close('all')
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)
"""
