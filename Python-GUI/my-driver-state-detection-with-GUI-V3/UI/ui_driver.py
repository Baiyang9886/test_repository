# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 548)
        self.label_show_camera2 = QtWidgets.QLabel(Form)
        self.label_show_camera2.setGeometry(QtCore.QRect(10, 10, 120, 160))
        self.label_show_camera2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_show_camera2.setObjectName("label_show_camera2")
        self.label_show_camera3 = QtWidgets.QLabel(Form)
        self.label_show_camera3.setGeometry(QtCore.QRect(10, 180, 120, 160))
        self.label_show_camera3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_show_camera3.setObjectName("label_show_camera3")
        self.label_show_camera4 = QtWidgets.QLabel(Form)
        self.label_show_camera4.setGeometry(QtCore.QRect(10, 350, 120, 160))
        self.label_show_camera4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_show_camera4.setObjectName("label_show_camera4")
        self.label_show_camera1 = QtWidgets.QLabel(Form)
        self.label_show_camera1.setGeometry(QtCore.QRect(140, 10, 640, 501))
        self.label_show_camera1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_show_camera1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_show_camera1.setObjectName("label_show_camera1")
        self.button_open_camera = QtWidgets.QPushButton(Form)
        self.button_open_camera.setGeometry(QtCore.QRect(260, 520, 75, 23))
        self.button_open_camera.setObjectName("button_open_camera")
        self.button_close = QtWidgets.QPushButton(Form)
        self.button_close.setGeometry(QtCore.QRect(440, 520, 75, 23))
        self.button_close.setObjectName("button_close")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_show_camera2.setText(_translate("Form", ""))
        self.label_show_camera3.setText(_translate("Form", ""))
        self.label_show_camera4.setText(_translate("Form", ""))
        self.label_show_camera1.setText(_translate("Form", ""))
        self.button_open_camera.setText(_translate("Form", "打开相机"))
        self.button_close.setText(_translate("Form", "退出"))

