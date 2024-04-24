import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")  # 声明使用QT5


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = None

    # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plot_sin(self):
        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plot_cos(self):
        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plot_3d(self):
        self.axes = self.fig.add_subplot(111, projection='3d')

        x_edges = np.array([[10, 20], [10, 20], [10, 20], [10, 20],
                            [20, 30], [20, 30], [20, 30], [20, 30],
                            [30, 40], [30, 40], [30, 40], [30, 40],
                            [40, 50], [40, 50], [40, 50], [40, 50]])
        # 设置y轴取值
        y_edges = np.array([[10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50]])

        # 设置X,Y对应点的值。即原始数据。
        hist = np.array([[3.0], [0.0], [8.0], [4.0],
                         [2.0], [4.0], [5.0], [7.0],
                         [9.0], [2.0], [6.0], [3.0],
                         [0.0], [3.0], [1.0], [0.0]])
        color_list = ['skyblue', 'lightgreen', 'bisque', 'gold',
                      'lightgreen', 'bisque', 'gold', 'lightpink',
                      'bisque', 'gold', 'lightpink', 'plum',
                      'gold', 'lightpink', 'plum', 'lightgray']

        for i in range(len(x_edges)):
            # 设置作图点的坐标
            xpos, ypos = np.meshgrid(x_edges[i][:-1] - 2.5, y_edges[i][:-1] - 2.5)
            xpos = xpos.flatten('F')
            ypos = ypos.flatten('F')
            zpos = np.zeros_like(xpos)

            # 设置柱形图大小
            dx = 5 * np.ones_like(zpos)
            dy = dx.copy()
            dz = hist[i].flatten()

            # 设置坐标轴标签
            self.axes.set_xlabel('front')
            self.axes.set_ylabel('side')
            self.axes.set_zlabel('height')
            self.axes.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color_list[i], zsort='average')

