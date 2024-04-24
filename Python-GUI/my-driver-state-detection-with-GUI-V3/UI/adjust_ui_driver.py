# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adjust_driver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.face_mesh = QtWidgets.QLabel(self.widget)
        self.face_mesh.setFrameShape(QtWidgets.QFrame.Box)
        self.face_mesh.setText("")
        self.face_mesh.setObjectName("face_mesh")
        self.verticalLayout.addWidget(self.face_mesh)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setMaximumSize(QtCore.QSize(22, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.head_yaw = QtWidgets.QLineEdit(self.widget_3)
        self.head_yaw.setMaximumSize(QtCore.QSize(44, 19))
        self.head_yaw.setObjectName("head_yaw")
        self.horizontalLayout_4.addWidget(self.head_yaw)
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.head_pitch = QtWidgets.QLineEdit(self.widget_3)
        self.head_pitch.setMaximumSize(QtCore.QSize(44, 19))
        self.head_pitch.setObjectName("head_pitch")
        self.horizontalLayout_4.addWidget(self.head_pitch)
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.head_roll = QtWidgets.QLineEdit(self.widget_3)
        self.head_roll.setMaximumSize(QtCore.QSize(44, 19))
        self.head_roll.setObjectName("head_roll")
        self.horizontalLayout_4.addWidget(self.head_roll)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_eye = QtWidgets.QLabel(self.widget_5)
        self.left_eye.setFrameShape(QtWidgets.QFrame.Box)
        self.left_eye.setText("")
        self.left_eye.setObjectName("left_eye")
        self.horizontalLayout_2.addWidget(self.left_eye)
        self.right_eye = QtWidgets.QLabel(self.widget_5)
        self.right_eye.setFrameShape(QtWidgets.QFrame.Box)
        self.right_eye.setText("")
        self.right_eye.setObjectName("right_eye")
        self.horizontalLayout_2.addWidget(self.right_eye)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        self.label_15.setMaximumSize(QtCore.QSize(22, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.gaze_yaw = QtWidgets.QLineEdit(self.widget_6)
        self.gaze_yaw.setMaximumSize(QtCore.QSize(44, 19))
        self.gaze_yaw.setObjectName("gaze_yaw")
        self.horizontalLayout_5.addWidget(self.gaze_yaw)
        self.label_16 = QtWidgets.QLabel(self.widget_6)
        self.label_16.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.gaze_pitch = QtWidgets.QLineEdit(self.widget_6)
        self.gaze_pitch.setMaximumSize(QtCore.QSize(44, 19))
        self.gaze_pitch.setObjectName("gaze_pitch")
        self.horizontalLayout_5.addWidget(self.gaze_pitch)
        self.label_17 = QtWidgets.QLabel(self.widget_6)
        self.label_17.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.gaze_roll = QtWidgets.QLineEdit(self.widget_6)
        self.gaze_roll.setMaximumSize(QtCore.QSize(44, 19))
        self.gaze_roll.setObjectName("gaze_roll")
        self.horizontalLayout_5.addWidget(self.gaze_roll)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 1)
        self.horizontalLayout_5.setStretch(5, 1)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mouth_state = QtWidgets.QLabel(self.widget_4)
        self.mouth_state.setFrameShape(QtWidgets.QFrame.Box)
        self.mouth_state.setText("")
        self.mouth_state.setObjectName("mouth_state")
        self.horizontalLayout_3.addWidget(self.mouth_state)
        self.drowsiness_state = QtWidgets.QLabel(self.widget_4)
        self.drowsiness_state.setFrameShape(QtWidgets.QFrame.Box)
        self.drowsiness_state.setText("")
        self.drowsiness_state.setObjectName("drowsiness_state")
        self.horizontalLayout_3.addWidget(self.drowsiness_state)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 4)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 4)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_7 = QtWidgets.QWidget(Form)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 6, 2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.detect_icon = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.detect_icon.setFont(font)
        self.detect_icon.setFrameShape(QtWidgets.QFrame.Box)
        self.detect_icon.setText("")
        self.detect_icon.setObjectName("detect_icon")
        self.horizontalLayout_7.addWidget(self.detect_icon)
        self.detect_result = QtWidgets.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.detect_result.setFont(font)
        self.detect_result.setObjectName("detect_result")
        self.horizontalLayout_7.addWidget(self.detect_result)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 10)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.camera_show = QtWidgets.QLabel(self.widget_7)
        self.camera_show.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_show.setText("")
        self.camera_show.setObjectName("camera_show")
        self.verticalLayout_3.addWidget(self.camera_show)
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout_6.setSpacing(200)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_open_camera = QtWidgets.QPushButton(self.widget_9)
        self.button_open_camera.setMaximumSize(QtCore.QSize(92, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.button_open_camera.setFont(font)
        self.button_open_camera.setObjectName("button_open_camera")
        self.horizontalLayout_6.addWidget(self.button_open_camera)
        self.button_close = QtWidgets.QPushButton(self.widget_9)
        self.button_close.setMaximumSize(QtCore.QSize(92, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.button_close.setFont(font)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout_6.addWidget(self.button_close)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 18)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.widget_7)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Head pose"))
        self.label_14.setText(_translate("Form", "Yaw"))
        self.label_12.setText(_translate("Form", "Pitch"))
        self.label_13.setText(_translate("Form", "Roll"))
        self.label_4.setText(_translate("Form", "Eyes state"))
        self.label_6.setText(_translate("Form", "left eye                                       right eye"))
        self.label_7.setText(_translate("Form", "Gaze direction"))
        self.label_15.setText(_translate("Form", "Yaw"))
        self.label_16.setText(_translate("Form", "Pitch"))
        self.label_17.setText(_translate("Form", "Roll"))
        self.label_3.setText(_translate("Form", "   Mouth state               Drowsiness state"))
        self.button_open_camera.setText(_translate("Form", "Open Camera"))
        self.button_close.setText(_translate("Form", "Exit"))

