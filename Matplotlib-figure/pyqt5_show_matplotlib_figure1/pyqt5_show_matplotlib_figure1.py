from PyQt5.Qt import *
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


class Figure_Canvas(FigureCanvas):
    def __init__(self, width=3.2, height=2.7):
        self.fig = Figure(figsize=(width, height), dpi=70)
        super().__init__(self.fig)

        self.ax = self.fig.add_subplot(111)

    def add_line(self, x_data, y_data, y2_data=None):
        self.line = Line2D(x_data, y_data)
        self.line.set_ls('--')
        self.line.set_marker("*")
        self.line.set_color('red')

        self.ax.grid(True)
        self.ax.set_title('外汇动态曲线')
        self.ax.set_xlim(np.min(x_data), np.max(x_data))
        self.ax.set_ylim(np.min(y_data), np.max(y_data) + 2)

        self.ax.set_xlabel('X坐标')
        self.ax.set_ylabel('Y坐标')

        self.ax.fill_between(x_data, y_data, color='g', alpha=0.1)
        self.ax.add_line(self.line)

        # 绘制第二条曲线
        self.line2 = Line2D(x_data, y2_data)

        self.ax.add_line(self.line2)

        self.line2.set_color('blue')
        self.ax.legend([self.line, self.line2], ['sinx', 'cosx'])

        self.ax2 = self.ax.twinx()
        self.ax2.set_ylabel("y2坐标")


class LineWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('动态曲线')
        self.resize(1000, 800)

        self.groupBox = QGroupBox(self)
        self.groupBox.setGeometry(QRect(100, 200, 800, 300))
        self.load_line()

        self.timer = QTimer()
        self.timer.start(10)
        self.ts = time.time()
        self.timer.timeout.connect(self.UpdateData)

    def load_line(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox)
        self.LineFigureLayout.addWidget(self.LineFigure)

        x_data = np.arange(-4, 4, 0.02)
        y_data = np.sin(x_data)

        y2_data = np.cos(x_data)

        self.LineFigure.add_line(x_data, y_data, y2_data)

    def UpdateData(self):
        dt = time.time() - self.ts
        x_data = np.arange(-4, 4, 0.02)
        z_data = np.sin(x_data + dt)
        h_data = np.cos(x_data + dt)

        self.LineFigure.line2.set_ydata(h_data)
        self.LineFigure.draw()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    win = LineWidget()
    win.show()
    sys.exit(app.exec_())
