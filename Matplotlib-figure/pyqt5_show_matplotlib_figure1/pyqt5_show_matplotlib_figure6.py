import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pyqtgraph.Qt import QtCore, QtGui
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)

        self.setWindowTitle('Psrxx: Subpulse Drifting analyse')
        self.resize(1200, 800)

        self.verticalLayoutWidget = QtWidgets.QWidget(self._main)
        # 设置第一个画布的尺寸
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 280, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # 创建画布1
        self.figure = plt.figure(figsize=(5, 3), facecolor='w')
        # 创建子图
        self.ax1 = self.figure.add_subplot(211)
        self.ax2 = self.figure.add_subplot(212)
        # 将画布绑定到canvas上
        self.canvas = FigureCanvas(self.figure)
        ## 添加图控件到布局
        self.verticalLayout.addWidget(self.canvas)
        ## 添加画图的工具栏
        self.verticalLayout.addWidget(NavigationToolbar(self.canvas, self))

        self.ax1.plot(np.sin(np.linspace(0, 10, 100)))
        self.ax2.plot(np.cos(np.linspace(0, 10, 100)))
        # plt.margins(0, 0)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self._main)
        # 设置第二个画布的尺寸
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 40, 900, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # 创建画布2
        self.figure1 = plt.figure(figsize=(5, 3), facecolor='w')
        # 创建子图
        self.ax3 = self.figure1.add_subplot(121)
        self.ax4 = self.figure1.add_subplot(122)
        # 将画布绑定到canvas上
        self.canvas1 = FigureCanvas(self.figure1)
        ## 添加图控件到布局
        self.horizontalLayout.addWidget(self.canvas1)

        self.ax3.plot(np.sin(np.linspace(0, 10, 100)), color="k")
        self.ax4.plot(np.cos(np.linspace(0, 10, 100)))

        self.setCentralWidget(self._main)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()



