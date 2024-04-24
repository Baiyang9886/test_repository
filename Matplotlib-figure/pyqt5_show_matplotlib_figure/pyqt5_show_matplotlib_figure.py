# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
@contact: 微信 1257309054
@file: dym_plot_mpl_main.py
@time: 2022/5/25 17:14
@author: LDC
"""

import json

import numpy as np
import logging
import os

import time
import sys

from PyQt5.Qt import *
from dym_plot_matplotlib import Ui_MainWindow
from mpl_plot import Mplplot
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from scipy.interpolate import make_interp_spline


class Window(QMainWindow, Ui_MainWindow):
    '''
    pyqt5界面流程
    '''

    def __init__(self, app):
        super(QMainWindow, self).__init__()
        self.app = app
        self.setup_ui()  # 渲染画布
        self.update_data_thread = UpdateDataThread()  # 创建更新波形数据线程
        self.connect_signals()  # 绑定触发事件

    def setup_ui(self):
        self.setupUi(self)
        # 加载相位振动波形
        self.phase_fig = Mplplot(width=5, height=3, dpi=72)
        self.fig_ntb = NavigationToolbar(self.phase_fig, self)
        self.gridlayout = QGridLayout(self.plot_view)
        self.gridlayout.addWidget(self.phase_fig)
        self.gridlayout.addWidget(self.fig_ntb)
        # 准备数据，绘制曲线
        self.x_data = np.arange(-10, 10, 0.1)
        y_data = np.sin(self.x_data)
        self.phase_fig.add_line(self.x_data, y_data)

    def connect_signals(self):
        # 绑定触发事件
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.update_data_thread._signal_update.connect(self.update_data_thread_slot)  # 绑定回调事件

    def btn_start_clicked(self):
        # 开启按钮
        self.update_data_thread.start()
        self.update_data_thread.x_data = self.x_data

    def update_data_thread_slot(self, data):
        # 线程回调函数
        data = json.loads(data)
        print(data['sin_data'])
        self.phase_fig.line.set_ydata(data['sin_data'])  # 更新数据
        self.phase_fig.draw()  # 重新画图


# 使用线程不断更新波形数据
class UpdateDataThread(QThread):
    _signal_update = pyqtSignal(str)  # 信号

    def __init__(self, parent=None):
        super(UpdateDataThread, self).__init__(parent)
        self.qmut = QMutex()
        self.is_exit = False
        self.ts = time.time()
        self.x_data = None

    def run(self):
        while True:
            self.qmut.lock()
            if self.is_exit:
                break
            self.qmut.unlock()
            dt = time.time() - self.ts
            z_data = np.sin(self.x_data + dt)  # 准备动态数据

            self._signal_update.emit(json.dumps({'sin_data': z_data.tolist()}))  # 发送信号给槽函数
            time.sleep(1)
        self.qmut.unlock()


def main():
    app = QApplication(sys.argv)
    mywindow = Window(app)
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
