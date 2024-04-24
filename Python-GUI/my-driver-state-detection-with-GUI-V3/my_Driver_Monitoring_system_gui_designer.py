#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os
import time
import PySide2
import numpy as np
from driver_state_detection1 import Face_mesh
from UI.my_ui_driver import Ui_Form


dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Driver_state_detection():
    def __init__(self):
        # self.face_recong = face.Recognition()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.fm = Face_mesh()
        self.CAM_NUM = 1
        # self.CAM_NUM = 'E:/Ducuments/A-star program/Drier-state-detection/Driver-state-detection-video-on-road.mp4'
        self.set_ui()        # 创建界面
        self.slot_init()     # 关联控件和事件
        self.__flag_work = 0
        self.count = 0
        self.fps = []
        self.aver_fps = 0

    def set_ui(self):
        self.MainWindow = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle("    Driver monitoring system                 "
                                       "                                                        AutoMan @ NTU")
        self.MainWindow.setWindowIcon(QtGui.QIcon('AutoMan.ico'))

        button_color = [self.ui.button_open_camera, self.ui.button_close]
        for i in range(2):
            button_color[i].setStyleSheet("QPushButton{color:black}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:rgb(188,230,111)}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:6px}"
                                          "QPushButton{padding:2px 2px}")

        self.ui.button_open_camera.setMinimumHeight(20)
        self.ui.button_close.setMinimumHeight(20)

        self.xdata = list(range(len(self.fm.yawn_interval)))
        self.ydata = [1/(interval + 0.00000001) for interval in self.fm.yawn_interval]
        self.x = list(range(len(self.fm.blink_interval)))
        self.y = [1/(interval + 0.00000001) for interval in self.fm.blink_interval]
        # self.update_plot()

        # # 设置背景图片
        # palette1 = QPalette()
        # palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        # self.setPalette(palette1)

    def update_plot(self):
        self.xdata = list(range(len(self.fm.yawn_interval)))
        self.ydata = [1 / (interval + 0.00000001) for interval in self.fm.yawn_interval]
        self.ui.canvas1.axes.cla()
        self.ui.canvas1.axes.plot(self.xdata, self.ydata, 'orange', alpha=1)
        self.ui.canvas1.axes.set_ylim(bottom=0, top=20)
        self.ui.canvas1.axes.fill_between(self.xdata, self.ydata, y2=0, color='orange', alpha=1, label='area')
        self.ui.canvas1.draw()

        self.x = list(range(len(self.fm.blink_interval)))
        self.y = [1 / (interval + 0.00000001) for interval in self.fm.blink_interval]
        self.ui.canvas2.axes.cla()
        self.ui.canvas2.axes.plot(self.x, self.y, 'b', alpha=1)
        self.ui.canvas2.axes.set_ylim(bottom=0, top=120000000)
        self.ui.canvas2.axes.fill_between(self.x, self.y, y2=0, color='b', alpha=1, label='area')
        self.ui.canvas2.draw()


    def slot_init(self):
        self.ui.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.ui.button_close.clicked.connect(QCoreApplication.instance().quit)


    def draw_figure(self):
        print('drawing')

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"Please check the connection of camera!",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_camera.start(30)
                self.ui.button_open_camera.setText(u'Close Camera')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.ui.camera_show.clear()
            # self.ui.face_mesh.clear()
            # self.ui.left_eye.clear()
            # self.ui.right_eye.clear()
            # self.ui.mouth.clear()
            # self.ui.head_pitch.clear()
            # self.ui.head_yaw.clear()
            # self.ui.gaze_pitch.clear()
            # self.ui.gaze_yaw.clear()
            self.ui.button_open_camera.setText(u'Open Camera')

    def show_camera(self):
        print('showing')
        start_time = time.time()
        flag, self.image = self.cap.read()
        # self.image = cv2.flip(self.image, 1)
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass
        output = self.fm.get_3D_face_mesh(self.image)

        show = cv2.resize(self.image, (1280, 960))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        cv2.rectangle(show, (0, 0), (1280, 80), color=(180, 180, 180), thickness=-1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(show, str("FPS: %.2f" % (self.aver_fps)), (20, 60), font, 1.2, (0, 0, 255), 2)

        annotated_image = cv2.cvtColor(output[1], cv2.COLOR_BGR2RGB)
        annotated_image = cv2.resize(annotated_image, (520, 400))
        left_eye = cv2.cvtColor(output[2], cv2.COLOR_BGR2RGB)
        left_eye = cv2.resize(left_eye, (160, 200))
        right_eye = cv2.cvtColor(output[3], cv2.COLOR_BGR2RGB)
        right_eye = cv2.resize(right_eye, (160, 200))
        mouth = cv2.cvtColor(output[4], cv2.COLOR_BGR2RGB)
        mouth = cv2.resize(mouth, (184, 160))

        # print(annotated_image.shape[1], annotated_image.shape[0])
        # show.shape[1] = 640, show.shape[0] = 480
        showImage1 = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        showImage2 = QtGui.QImage(annotated_image.data, annotated_image.shape[1], annotated_image.shape[0], QtGui.QImage.Format_RGB888)
        showImage3 = QtGui.QImage(left_eye.data, left_eye.shape[1], left_eye.shape[0], QtGui.QImage.Format_RGB888)
        showImage4 = QtGui.QImage(right_eye.data, right_eye.shape[1], right_eye.shape[0], QtGui.QImage.Format_RGB888)
        showImage5 = QtGui.QImage(mouth.data, mouth.shape[1], mouth.shape[0], QtGui.QImage.Format_RGB888)

        head_roll = np.sum(self.fm.angle_roll) / len(self.fm.angle_roll)
        head_yaw = np.sum(self.fm.angle_yaw) / len(self.fm.angle_yaw)
        head_pitch = np.sum(self.fm.angle_pitch) / len(self.fm.angle_pitch)
        gaze_pitch = np.sum(self.fm.gaze_pitch) / len(self.fm.gaze_pitch)
        gaze_yawn = np.sum(self.fm.gaze_yaw) / len(self.fm.gaze_yaw)
        self.ui.head_roll.setText("%.1f" % (head_roll))
        self.ui.head_pitch.setText("%.1f" % (head_pitch))
        self.ui.head_yaw.setText("%.1f" % (head_yaw))
        self.ui.gaze_pitch.setText("%.1f" % (gaze_pitch))
        self.ui.gaze_yaw.setText("%.1f" % (gaze_yawn))

        head_yaw_score, head_pitch_score = 0, 0
        gaze_yawn_score, gaze_pitch_score = 0, 0
        if head_yaw > 0:
            head_yaw_score = 60 / 40 * head_yaw
        else:
            head_yaw_score = -head_yaw
        if head_pitch > 0:
            head_pitch_score = 2 * head_pitch
        else:
            head_pitch_score = - head_pitch * 2
        if gaze_yawn > 0:
            gaze_yawn_score = 60 / 50 * gaze_yawn
        else:
            gaze_yawn_score = - gaze_yawn
        if gaze_pitch > 0:
            gaze_pitch_score = 60/40 * gaze_pitch
        else:
            gaze_pitch_score = - gaze_pitch * 2
        if self.fm.eye_close or self.fm.yawning:
            distraction_score = 0
        else:
            distraction_score = np.max([head_yaw_score, head_pitch_score, gaze_yawn_score, gaze_pitch_score])

        drowsiness_score1 = self.fm.blink_duration / 100 * 50 + 8 * (len(self.fm.blink_frequency) - 2)
        drowsiness_score2 = self.fm.yawn_duration / 100 * 20 + 20 * (len(self.fm.yawn_frequency) - 1)
        drowsiness_score = np.max([drowsiness_score1, drowsiness_score2, 0])
        print('drowsiness score: ' + str(drowsiness_score))

        if drowsiness_score > 60:
            cv2.putText(show, "Drowsiness detected!!!", (460, 52), font, 1.2, (255, 0, 0), 2)
        elif distraction_score > 60:
            cv2.putText(show, "Distraction detected!!!", (460, 52), font, 1.2, (255, 0, 0), 2)
        else:
            cv2.putText(show, "Normal driving~~~", (460, 52), font, 1.2, (0, 255, 0), 2)

        self.ui.camera_show.setPixmap(QtGui.QPixmap.fromImage(showImage1))
        self.ui.face_mesh.setPixmap(QtGui.QPixmap.fromImage(showImage2))
        self.ui.left_eye.setPixmap(QtGui.QPixmap.fromImage(showImage3))
        self.ui.right_eye.setPixmap(QtGui.QPixmap.fromImage(showImage4))
        self.ui.mouth.setPixmap(QtGui.QPixmap.fromImage(showImage5))

        if self.fm.blink_duration < 60:
            self.ui.blink_duration.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:green;"
                                                 "text-align:center;"
                                                 "}")
        else:
            self.ui.blink_duration.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:red;"
                                                 "}")
        if distraction_score < 60:
            self.ui.distraction_detection.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:green;"
                                                 "text-align:center;"
                                                 "}")
        else:
            self.ui.distraction_detection.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:red;"
                                                 "}")
        if drowsiness_score < 60:
            self.ui.drowsiness_detection.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:green;"
                                                 "text-align:center;"
                                                 "}")
        else:
            self.ui.drowsiness_detection.setStyleSheet("QProgressBar::chunk"
                                                 "{"
                                                 "background-color:red;"
                                                 "}")
        self.ui.blink_duration.setValue(float(self.fm.blink_duration))
        self.ui.drowsiness_detection.setValue(float(drowsiness_score))
        self.ui.distraction_detection.setValue(float(distraction_score))
        self.update_plot()

        end_time = time.time()
        process_time = end_time - start_time
        self.fps.append(1/process_time)
        if len(self.fps) > 100:
            self.fps.pop(0)
        self.aver_fps = np.sum(self.fps) / len(self.fps)


    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"Close", u"Do you want to close?")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'OK')
        cacel.setText(u'Cancel')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    driver = Driver_state_detection()
    driver.MainWindow.show()
    sys.exit(App.exec_())