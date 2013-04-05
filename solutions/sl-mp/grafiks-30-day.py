#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab:
__author__ = 'petro-ew'
import matplotlib.pyplot as plt
import numpy as np
import numpy
import pylab
import matplotlib.axes
import matplotlib.axis
import sys
import string
import matplotlib as mpl
import matplotlib.figure

#bdiff -n -s
#http://matplotlib.org/users/customizing.html#dynamic-rc-settings
#font.family         : sans-serif
#font.style          : normal
#font.variant        : normal
#font.weight         : medium
#font.stretch        : normal
# note that font.size controls default text sizes.  To configure
# special text sizes tick labels, axes, labels, title, etc, see the rc
# settings for axes and ticks. Special text sizes can be defined
# relative to font.size, using the following values: xx-small, x-small,
# small, medium, large, x-large, xx-large, larger, or smaller
#font.size           : 12.0
#font.serif          : Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif     : Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
#font.cursive        : Apple Chancery, Textile, Zapf Chancery, Sand, cursive
#font.fantasy        : Comic Sans MS, Chicago, Charcoal, Impact, Western, fantasy
#font.monospace      : Bitstream Vera Sans Mono, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace

params = {'font.size' : 12,
          'axes.labelsize' : 12,
          'font.style' : 'normal',
          'font.family' : 'sans-serif',
          'font.sans-serif' : 'Arial'
}
pylab.rcParams.update(params)
TITLE = sys.argv[1]
#TITLE = 'akko'
# Create the figure (A4 format)
plt.figure(num=None, figsize=(11.69, 8.27), dpi=600)
fig = plt.figure()

fn = TITLE + ".slmp"
print(fn)
data1 = numpy.genfromtxt(TITLE + '.slmp', usecols = [1,])
data2 = numpy.genfromtxt(TITLE + '.slmp', usecols = [2,])
data3 = numpy.genfromtxt(TITLE + '.slmp', usecols = [3,])

locs = np.arange(1, len(data1)+1)
width = 0.27
# Задаем заголовок диаграммы

plt.title('Станция  ' + TITLE,{'fontname':'Arial','fontsize':16})
#plt.title(u'AKKO')

# Задаем подписи к осям X и Y

#plt.xlabel(u'Дни с начала года')
#plt.ylabel(u'Значения')
plt.xlabel('Дни с начала года',{'fontname':'Arial','fontsize':14})
plt.ylabel('Значения',{'fontname':'Arial','fontsize':14})

# Включаем сетку

plt.grid()

plt.xticks(locs + width * 1.5, locs)
pylab.bar(locs, data1, width = width, color = 'yellow', label = 'ls < 10')
pylab.bar(locs + width, data2, width = width, color = 'red', label = 'ls > 10')
pylab.bar(locs + 2 * width, data3, width = width, color = 'green', label = 'mp > 10')

pylab.legend()
ax = fig.add_subplot(111)
for label in ax.get_xticklabels():
    label.set_color('black')
    label.set_rotation(90)
    label.set_fontsize(8)
#fig.autofmt_xdate()

#plt.tight_layout()

#plt.savefig('spirit.png', format = 'png')
#plt.show()
#plt.savefig('spirit.pdf', format = 'pdf')
# Save to PDF
plt.savefig("%s_day30.pdf" % TITLE)
