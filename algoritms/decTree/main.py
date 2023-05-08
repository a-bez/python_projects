# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 10:00:16 2018

@author: aoanng
"""

from pylab import *
import treePlotter
from ID3Tree import *
mpl.rcParams['font.sans-serif'] = ['SimHei']  # Укажите шрифт по умолчанию
mpl.rcParams['axes.unicode_minus'] = False  # Решить проблему, заключающуюся в том, что знак минуса «-» отображается как квадрат при сохранении изображения
##################################

# Тестирование построения дерева решений
myDat, labels = createDataSet()
myTree = createTree(myDat, labels)
# Нарисовать дерево решений

treePlotter.createPlot(myTree)