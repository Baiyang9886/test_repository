# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
@contact: 微信 1257309054
@file: mpl_plot.py
@time: 2022/5/23 15:05
@author: LDC
"""

import matplotlib
import numpy as np
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from matplotlib.lines import Line2D
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Mplplot(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(Mplplot, self).__init__(self.fig)
        self.setParent(parent)
        self.axes = self.fig.add_subplot(111) # 111 表示 1 行 1 列，第一张曲线图


        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def add_line(self, x_data, y_data):
        self.line = Line2D(x_data, y_data)  # 绘制 2D 折线图
        # ------------------ 调整折线图基本样式 ---------------------#
        # self.line.set_ls('--')  # 设置连线
        # self.line.set_marker('*') # 设置每个点
        # self.line.set_color('red')  # 设置线条颜色
        self.axes.grid(True)  # 添加网格
        self.axes.set_title('动态曲线 ')  # 设置标题
        # 设置 xy 轴最大最小值 , 找到 x_data, y_data 最大最小值
        self.axes.set_xlim(np.min(x_data), np.max(x_data))
        self.axes.set_ylim(np.min(y_data), np.max(y_data) + 5)  # y 轴稍微多一点，会好看一点
        self.axes.set_xlabel('x 坐标 ')  # 设置坐标名称
        self.axes.set_ylabel('y 坐标 ')
        # 在曲线下方填充颜色
        # self.ax.fill_between(x_data, y_data, color='g', alpha=0.1)
        # self.ax.legend([self.line], ['sinx'])  # 添加图例
        # ------------------------------------------------------#
        self.axes.add_line(self.line)
