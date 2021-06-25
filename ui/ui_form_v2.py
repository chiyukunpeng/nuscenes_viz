# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/chiyukunpeng/CHENPENG01/project/nuscenes_viz20210618/ui/ui_form_v2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 781, 631))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.windows_layout_1 = QtWidgets.QHBoxLayout()
        self.windows_layout_1.setSpacing(0)
        self.windows_layout_1.setObjectName("windows_layout_1")

        self.rgb_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(16)
        self.rgb_label.setFont(font)
        self.rgb_label.setFixedSize(388, 286)
        self.rgb_label.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.rgb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rgb_label.setObjectName("rgb_label")
        self.windows_layout_1.addWidget(self.rgb_label)

        self.camera_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(16)
        self.camera_label.setFont(font)
        self.camera_label.setFixedSize(388, 286)
        self.camera_label.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_label.setObjectName("camera_label")
        self.windows_layout_1.addWidget(self.camera_label)

        self.windows_layout_1.setStretch(0, 1)
        self.windows_layout_1.setStretch(1, 1)
        self.verticalLayout.addLayout(self.windows_layout_1)

        self.window_layout_2 = QtWidgets.QHBoxLayout()
        self.window_layout_2.setSpacing(0)
        self.window_layout_2.setObjectName("window_layout_2")

        self.lidar_figure = plt.figure(figsize=(9, 9))
        self.lidar_figure.suptitle('Lidar', x=0.5, y=0.5, ha='center', va='center', size='xx-large')
        self.lidar_canvas = FigureCanvas(self.lidar_figure)
        self.lidar_canvas.setFixedSize(388, 286)
        self.lidar_canvas.setObjectName('lidar_canvas')
        self.window_layout_2.addWidget(self.lidar_canvas)

        self.radar_figure = plt.figure(figsize=(9, 9))
        self.radar_figure.suptitle('Radar', x=0.5, y=0.5, ha='center', va='center', size='xx-large')
        self.radar_canvas = FigureCanvas(self.radar_figure)
        self.radar_canvas.setFixedSize(388, 286)
        self.radar_canvas.setObjectName('radar_canvas')
        self.window_layout_2.addWidget(self.radar_canvas)

        self.window_layout_2.setStretch(0, 1)
        self.window_layout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.window_layout_2)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setContentsMargins(80, 5, 100, 5)
        self.buttons_layout.setSpacing(100)
        self.buttons_layout.setObjectName("buttons_layout")

        self.load_dataset_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_dataset_button.sizePolicy().hasHeightForWidth())
        self.load_dataset_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.load_dataset_button.setFont(font)
        self.load_dataset_button.setStyleSheet("QPushButton#pushButton {\n"
                                                                                "background-color: rgb(0, 0, 255);\n"
                                                                                "border-style: outset;\n"
                                                                                "border-width: 2px;\n"
                                                                                "}\n"
                                                                                "\n"
                                                                                "QPushButton#pushButton:pressed {\n"
                                                                                "background-color: rgb(255, 0, 0);\n"
                                                                                "border-style: inset;\n"
                                                                                "}\n"
                                                                                "\n"
                                                                                "QPushButton#pushButton:hover {\n"
                                                                                "background-color: rgb(0, 255, 0);\n"
                                                                                "border-style: inset;\n"
                                                                                "}")
        self.load_dataset_button.setObjectName("load_dataset_button")
        self.buttons_layout.addWidget(self.load_dataset_button)

        self.nusc_viz_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nusc_viz_button.sizePolicy().hasHeightForWidth())
        self.nusc_viz_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nusc_viz_button.setFont(font)
        self.nusc_viz_button.setStyleSheet("QPushButton#pushButton {\n"
                                                                                "background-color: rgb(0, 0, 255);\n"
                                                                                "border-style: outset;\n"
                                                                                "border-width: 2px;\n"
                                                                                "}\n"
                                                                                "\n"
                                                                                "QPushButton#pushButton:pressed {\n"
                                                                                "background-color: rgb(255, 0, 0);\n"
                                                                                "border-style: inset;\n"
                                                                                "}\n"
                                                                                "\n"
                                                                                "QPushButton#pushButton:hover {\n"
                                                                                "background-color: rgb(0, 255, 0);\n"
                                                                                "border-style: inset;\n"
                                                                                "}")
        self.nusc_viz_button.setObjectName("nusc_viz_button")
        self.buttons_layout.addWidget(self.nusc_viz_button)

        self.buttons_layout.setStretch(0, 1)
        self.buttons_layout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.buttons_layout)

        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setSpacing(1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "nuscenes_viz_v2"))
        self.rgb_label.setText(_translate("MainWindow", "Raw"))
        self.camera_label.setText(_translate("MainWindow", "Camera"))
        self.load_dataset_button.setText(_translate("MainWindow", "load dataset"))
        self.nusc_viz_button.setText(_translate("MainWindow", "viz dataset"))

