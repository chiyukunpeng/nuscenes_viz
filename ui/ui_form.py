# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuScenes-Viz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.setEnabled(True)
        form.resize(1923, 1010)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form.sizePolicy().hasHeightForWidth())
        form.setSizePolicy(sizePolicy)
        form.setStyleSheet("background-color: rgb(145, 145, 145);\n"
"")
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1921, 1011))
        self.widget.setObjectName("widget")
        self.all_layout = QtWidgets.QVBoxLayout(self.widget)
        self.all_layout.setContentsMargins(0, 0, 0, 0)
        self.all_layout.setSpacing(0)
        self.all_layout.setObjectName("all_layout")
        self.label_layout_1 = QtWidgets.QHBoxLayout()
        self.label_layout_1.setSpacing(0)
        self.label_layout_1.setObjectName("label_layout_1")
        self.rgb_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_label.sizePolicy().hasHeightForWidth())
        self.rgb_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rgb_label.setFont(font)
        self.rgb_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rgb_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.rgb_label.setLineWidth(1)
        self.rgb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rgb_label.setObjectName("rgb_label")
        self.label_layout_1.addWidget(self.rgb_label)
        self.rgb_lidar_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_lidar_label.sizePolicy().hasHeightForWidth())
        self.rgb_lidar_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rgb_lidar_label.setFont(font)
        self.rgb_lidar_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rgb_lidar_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.rgb_lidar_label.setLineWidth(1)
        self.rgb_lidar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rgb_lidar_label.setObjectName("rgb_lidar_label")
        self.label_layout_1.addWidget(self.rgb_lidar_label)
        self.rgb_radar_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_radar_label.sizePolicy().hasHeightForWidth())
        self.rgb_radar_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rgb_radar_label.setFont(font)
        self.rgb_radar_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rgb_radar_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.rgb_radar_label.setLineWidth(1)
        self.rgb_radar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rgb_radar_label.setObjectName("rgb_radar_label")
        self.label_layout_1.addWidget(self.rgb_radar_label)
        self.label_layout_1.setStretch(0, 1)
        self.label_layout_1.setStretch(1, 1)
        self.label_layout_1.setStretch(2, 1)
        self.all_layout.addLayout(self.label_layout_1)
        self.label_layout_2 = QtWidgets.QHBoxLayout()
        self.label_layout_2.setSpacing(0)
        self.label_layout_2.setObjectName("label_layout_2")
        self.camera_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_label.sizePolicy().hasHeightForWidth())
        self.camera_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.camera_label.setFont(font)
        self.camera_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.camera_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.camera_label.setLineWidth(1)
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_label.setObjectName("camera_label")
        self.label_layout_2.addWidget(self.camera_label)
        self.lidar_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lidar_label.sizePolicy().hasHeightForWidth())
        self.lidar_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lidar_label.setFont(font)
        self.lidar_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lidar_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.lidar_label.setLineWidth(1)
        self.lidar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lidar_label.setObjectName("lidar_label")
        self.label_layout_2.addWidget(self.lidar_label)
        self.radar_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radar_label.sizePolicy().hasHeightForWidth())
        self.radar_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radar_label.setFont(font)
        self.radar_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radar_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.radar_label.setLineWidth(1)
        self.radar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.radar_label.setObjectName("radar_label")
        self.label_layout_2.addWidget(self.radar_label)
        self.label_layout_2.setStretch(0, 1)
        self.label_layout_2.setStretch(1, 1)
        self.label_layout_2.setStretch(2, 1)
        self.all_layout.addLayout(self.label_layout_2)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.button_layout.setContentsMargins(80, 5, 80, 5)
        self.button_layout.setSpacing(80)
        self.button_layout.setObjectName("button_layout")
        self.rgb_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_button.sizePolicy().hasHeightForWidth())
        self.rgb_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rgb_button.setFont(font)
        self.rgb_button.setMouseTracking(False)
        self.rgb_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.rgb_button.setObjectName("rgb_button")
        self.button_layout.addWidget(self.rgb_button)
        self.camera_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_button.sizePolicy().hasHeightForWidth())
        self.camera_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.camera_button.setFont(font)
        self.camera_button.setMouseTracking(False)
        self.camera_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.camera_button.setObjectName("camera_button")
        self.button_layout.addWidget(self.camera_button)
        self.rgb_lidar_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_lidar_button.sizePolicy().hasHeightForWidth())
        self.rgb_lidar_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rgb_lidar_button.setFont(font)
        self.rgb_lidar_button.setMouseTracking(False)
        self.rgb_lidar_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.rgb_lidar_button.setObjectName("rgb_lidar_button")
        self.button_layout.addWidget(self.rgb_lidar_button)
        self.lidar_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lidar_button.sizePolicy().hasHeightForWidth())
        self.lidar_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lidar_button.setFont(font)
        self.lidar_button.setMouseTracking(False)
        self.lidar_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.lidar_button.setObjectName("lidar_button")
        self.button_layout.addWidget(self.lidar_button)
        self.rgb_radar_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_radar_button.sizePolicy().hasHeightForWidth())
        self.rgb_radar_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rgb_radar_button.setFont(font)
        self.rgb_radar_button.setMouseTracking(False)
        self.rgb_radar_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.rgb_radar_button.setObjectName("rgb_radar_button")
        self.button_layout.addWidget(self.rgb_radar_button)
        self.radar_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radar_button.sizePolicy().hasHeightForWidth())
        self.radar_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radar_button.setFont(font)
        self.radar_button.setMouseTracking(False)
        self.radar_button.setStyleSheet("border-style:none;\n"
"border:1px solid #C0DCF2;\n"
"color:#386487;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);")
        self.radar_button.setObjectName("radar_button")
        self.button_layout.addWidget(self.radar_button)
        self.button_layout.setStretch(0, 1)
        self.button_layout.setStretch(1, 1)
        self.button_layout.setStretch(2, 1)
        self.button_layout.setStretch(3, 1)
        self.button_layout.setStretch(4, 1)
        self.button_layout.setStretch(5, 1)
        self.all_layout.addLayout(self.button_layout)
        self.all_layout.setStretch(0, 10)
        self.all_layout.setStretch(1, 10)
        self.all_layout.setStretch(2, 1)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "NuScenes-Viz"))
        self.rgb_label.setText(_translate("form", "RGB"))
        self.rgb_lidar_label.setText(_translate("form", "RGB with lidar PC"))
        self.rgb_radar_label.setText(_translate("form", "RGB with radar PC"))
        self.camera_label.setText(_translate("form", "Camera"))
        self.lidar_label.setText(_translate("form", "Lidar"))
        self.radar_label.setText(_translate("form", "Radar"))
        self.rgb_button.setText(_translate("form", "load dataset"))
        self.camera_button.setText(_translate("form", "Camera"))
        self.rgb_lidar_button.setText(_translate("form", "RGB with lidar PC"))
        self.lidar_button.setText(_translate("form", "Lidar"))
        self.rgb_radar_button.setText(_translate("form", "RGB with radar PC"))
        self.radar_button.setText(_translate("form", "Radar"))

