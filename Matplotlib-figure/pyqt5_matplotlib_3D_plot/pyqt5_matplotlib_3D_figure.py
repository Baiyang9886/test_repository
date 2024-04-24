import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_ut import Ui_matplot_demo
from leetcode218_figure import MyFigure


class myWindow(QWidget, Ui_matplot_demo):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0, 0)

        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=10, height=6, dpi=100)
        self.F.plot_cos()

        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        # 在容器中添加一个groupbox对象，在groupbox对象中创建布局
        self.groupBox = QGroupBox(self.plt3d_module)
        self.groupBox.setMinimumSize(QSize(1100, 610))
        self.groupBox.setTitle("画图demo")

        def connect_bind():
            self.bt_open.clicked.connect(self.open_pic)
            self.bt_close.clicked.connect(self.close_pic)
        connect_bind()

        self.glo_plt_figure = QGridLayout(self.groupBox)

    def open_pic(self):
        self.F = MyFigure(width=10, height=6, dpi=100)
        self.F.plot_3d()
        self.glo_plt_figure.addWidget(self.F, 0, 0)
        print("here")
        self.show()
        self.glo_plt_figure.addWidget(self.F, 0, 0)

    def close_pic(self):
        self.glo_plt_figure.removeWidget(self.F)
        self.show()


def main():
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
