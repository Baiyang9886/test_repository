from PyQt5 import QtWidgets
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import  QApplication,QVBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["font.sans-serif"] = ["Simhei"]  # 设置默认字体
plt.rcParams["axes.unicode_minus"] = False  # 坐标轴正确显示正负号


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Pyqt5时序打印")
        MainWindow.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # 调用set_matplotlib方法将matplotlib嵌入进来（该方法需要自己写进来，后边会写方法）
        self.set_matplotlib()

        # 速度标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 120, 21))
        self.label.setObjectName("label")
        # 速度输入框
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 200, 21))
        self.lineEdit.setObjectName("lineEdit")

        # 线条颜色标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.label_2.setObjectName("label_2")
        # Max点标签
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 50, 20))
        self.label_3.setObjectName("label_3")
        # Min点标签
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 350, 50, 20))
        self.label_4.setObjectName("label_4")
        # 选择文件标签
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 180, 21))
        self.label_5.setObjectName("label_5")
        # 显示文件地址标签
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 350, 180, 21))
        self.label_6.setObjectName("label_6")

        # 默认线条红色
        self.line_color = 'r'
        # 颜色单选框三个
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 130, 86, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.get_color1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 160, 86, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.get_color2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 190, 86, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.get_color3)

        # 开始绘图按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.pushButton.setObjectName("pushButton")
        # 点击开始绘图执行定时器方法（需要自己编写）
        self.pushButton.clicked.connect(self.start_dingshiqi)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.i = 0
        self.t_list = []
        self.y_list = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyqt5时序打印"))
        self.label.setText(_translate("MainWindow", "绘图速度（秒）："))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入速度，默认为1"))

        self.label_2.setText(_translate("MainWindow", "线条颜色："))
        self.label_3.setText(_translate("MainWindow", "Max点："))
        self.label_4.setText(_translate("MainWindow", "Min点："))

        self.radioButton.setText(_translate("MainWindow", "red"))
        self.radioButton_2.setText(_translate("MainWindow", "blue"))
        self.radioButton_3.setText(_translate("MainWindow", "green"))

        self.pushButton.setText(_translate("MainWindow", "开始绘图"))

        # 嵌入matplotlib方法
    def set_matplotlib(self):
        # 创建画布
        self.fig = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.fig)

        # 把画布放进widget组件,设定位置
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.canvas)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setLayout(self.vlayout)
        self.widget.setGeometry(QtCore.QRect(240, 20, 600, 400))
        self.widget.setObjectName("matplotlib")

        # 初始化matplotlib显示区域
        self.ax = self.fig.subplots()
        self.ax.spines['top'].set_visible(False)  # 顶边界不可见
        self.ax.spines['right'].set_visible(False)  # 右边界不可见
        self.ax.set_title('嵌入的matplotlib')
        self.ax.set_xlabel('序号')
        self.ax.set_ylabel('数值')

    def get_color1(self):
        self.line_color = 'r'

    def get_color2(self):
        self.line_color = 'b'

    def get_color3(self):
        self.line_color = 'g'

    # 找最大值方法
    def search_max(self):
        self.ymax_data = max(self.data.values)
        for i, j in enumerate(self.data.values):
            if j == self.ymax_data:
                self.xmax_data = i
        self.label_5.setText('(%d，%f)' % (self.xmax_data, self.ymax_data))

    # 找最小值方法
    def search_min(self):
        self.ymin_data = min(self.data.values)
        for i, j in enumerate(self.data.values):
            if j == self.ymin_data:
                self.xmin_data = i
        self.label_6.setText('(%d，%f)' % (self.xmin_data, self.ymin_data))

    # 定时器方法
    def start_dingshiqi(self):
        # 获取输入的速度
        self.get_speed()
        self.ax.cla()
        # 设置坐标系范围及刻度
        self.ax.set_xlim(0, len(self.t) + 1)
        self.ax.set_ylim(min(self.y - 1), max(self.y) + 1)
        self.ax.set_yticks(np.arange(min(self.y) - 1, max(self.y) + 1, 5))
        self.ax.set_xticks(np.arange(0, len(self.t) + 1, 500))
        self.ax.set_title('正在绘图')
        self.ax.set_xlabel('序号')
        self.ax.set_ylabel('数值')
        # 定时器
        self.testTimer = QtCore.QTimer()
        self.testTimer.timeout.connect(self.plotfig)  # 调用绘图方法
        self.testTimer.start(self.speed * 10)
        # 输出最大值，最小值
        self.search_max()
        self.search_min()

    # 绘图方法
    def plotfig(self):
        self.ax.autoscale_view()
        # 绘图
        x = np.linspace(0, 10, 10)
        y = [random.randint(0, 10) for i in range(10)]
        xx = np.linspace(0, 10)
        f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
        yy = f(xx)
        self.ax.plot(xx, yy, c=self.line_color, linewidth=1)
        self.fig.canvas.draw()  # 画布重绘，self.figs.canvas
        self.fig.canvas.flush_events()  # 画布刷新 self.figs.canvas
        self.t_list.append(self.t[self.i])  # 更新数据
        self.y_list.append(self.y[self.t[self.i]])  # 每次给原来数据加入新数据
        self.i += 10
        if self.i >= len(self.t):
            self.testTimer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec_()