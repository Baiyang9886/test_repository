# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ut.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matplot_demo(object):
    def setupUi(self, matplot_demo):
        matplot_demo.setObjectName("matplot_demo")
        matplot_demo.resize(1133, 721)
        self.gridLayout = QtWidgets.QGridLayout(matplot_demo)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_close = QtWidgets.QPushButton(matplot_demo)
        self.bt_close.setObjectName("bt_close")
        self.gridLayout.addWidget(self.bt_close, 1, 1, 1, 1)
        self.bt_open = QtWidgets.QPushButton(matplot_demo)
        self.bt_open.setObjectName("bt_open")
        self.gridLayout.addWidget(self.bt_open, 1, 0, 1, 1)
        self.plt3d_module = QtWidgets.QWidget(matplot_demo)
        self.plt3d_module.setMinimumSize(QtCore.QSize(1111, 611))
        self.plt3d_module.setObjectName("plt3d_module")
        self.gridLayout.addWidget(self.plt3d_module, 0, 0, 1, 2)

        self.retranslateUi(matplot_demo)
        QtCore.QMetaObject.connectSlotsByName(matplot_demo)

    def retranslateUi(self, matplot_demo):
        _translate = QtCore.QCoreApplication.translate
        matplot_demo.setWindowTitle(_translate("matplot_demo", "Form"))
        self.bt_close.setText(_translate("matplot_demo", "按一下就可以关闭图片"))
        self.bt_open.setText(_translate("matplot_demo", "按一下就可以画图"))
