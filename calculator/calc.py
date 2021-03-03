# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python_projects\calc.ui'
#
# Created: Tue Dec 22 08:46:01 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 345)
        Form.setMinimumSize(QtCore.QSize(270, 345))
        Form.setMaximumSize(QtCore.QSize(270, 345))
        Form.setCursor(QtCore.Qt.ArrowCursor)
        Form.setStyleSheet("QWidget{\n"
"    background-color:#373640;\n"
"}\n"
"QPushButton{\n"
"    width: 50px;\n"
"    height:50px;    \n"
"    border: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    background-color:#373331;\n"
"}\n"
"")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"    font-size:17px;\n"
"    color:white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 251, 281))
        self.gridLayoutWidget.setStyleSheet("QPushButton{\n"
"    background-color:#605a56;\n"
"}")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_equally = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_equally.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_equally.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_equally.setObjectName("pb_equally")
        self.gridLayout.addWidget(self.pb_equally, 4, 4, 1, 1)
        self.pb_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_3.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_3.setObjectName("pb_3")
        self.gridLayout.addWidget(self.pb_3, 3, 3, 1, 1)
        self.pb_plus = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_plus.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_plus.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_plus.setObjectName("pb_plus")
        self.gridLayout.addWidget(self.pb_plus, 2, 4, 1, 1)
        self.pb_dot = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_dot.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_dot.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_dot.setObjectName("pb_dot")
        self.gridLayout.addWidget(self.pb_dot, 4, 3, 1, 1)
        self.pb_multiply = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_multiply.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_multiply.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_multiply.setObjectName("pb_multiply")
        self.gridLayout.addWidget(self.pb_multiply, 1, 4, 1, 1)
        self.pb_6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_6.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_6.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_6.setObjectName("pb_6")
        self.gridLayout.addWidget(self.pb_6, 2, 3, 1, 1)
        self.pb_minus = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_minus.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_minus.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_minus.setObjectName("pb_minus")
        self.gridLayout.addWidget(self.pb_minus, 3, 4, 1, 1)
        self.pb_del_one = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_del_one.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_del_one.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_del_one.setObjectName("pb_del_one")
        self.gridLayout.addWidget(self.pb_del_one, 0, 1, 1, 1)
        self.pb_9 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_9.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_9.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_9.setObjectName("pb_9")
        self.gridLayout.addWidget(self.pb_9, 1, 3, 1, 1)
        self.pb_8 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_8.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_8.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_8.setObjectName("pb_8")
        self.gridLayout.addWidget(self.pb_8, 1, 1, 1, 1)
        self.pb_del_all = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_del_all.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_del_all.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_del_all.setObjectName("pb_del_all")
        self.gridLayout.addWidget(self.pb_del_all, 0, 0, 1, 1)
        self.pb_7 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_7.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_7.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_7.setObjectName("pb_7")
        self.gridLayout.addWidget(self.pb_7, 1, 0, 1, 1)
        self.pb_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_4.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_4.setObjectName("pb_4")
        self.gridLayout.addWidget(self.pb_4, 2, 0, 1, 1)
        self.pb_1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_1.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_1.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_1.setObjectName("pb_1")
        self.gridLayout.addWidget(self.pb_1, 3, 0, 1, 1)
        self.pb_percent = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_percent.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_percent.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_percent.setObjectName("pb_percent")
        self.gridLayout.addWidget(self.pb_percent, 4, 0, 1, 1)
        self.pb_0 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_0.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_0.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_0.setObjectName("pb_0")
        self.gridLayout.addWidget(self.pb_0, 4, 1, 1, 1)
        self.pb_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_2.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_2.setObjectName("pb_2")
        self.gridLayout.addWidget(self.pb_2, 3, 1, 1, 1)
        self.pb_devide = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_devide.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_devide.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_devide.setObjectName("pb_devide")
        self.gridLayout.addWidget(self.pb_devide, 0, 4, 1, 1)
        self.pb_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_5.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_5.setObjectName("pb_5")
        self.gridLayout.addWidget(self.pb_5, 2, 1, 1, 1)
        self.pb_plus_minus = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_plus_minus.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_plus_minus.setStyleSheet("QPushButton{\n"
"    background-color:#red;\n"
"    color:white;\n"
"}")
        self.pb_plus_minus.setObjectName("pb_plus_minus")
        self.gridLayout.addWidget(self.pb_plus_minus, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_equally.setText(QtGui.QApplication.translate("Form", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_3.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_plus.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dot.setText(QtGui.QApplication.translate("Form", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_multiply.setText(QtGui.QApplication.translate("Form", "×", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_6.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_minus.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_del_one.setText(QtGui.QApplication.translate("Form", "<==", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_9.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_8.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_del_all.setText(QtGui.QApplication.translate("Form", "CE", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_7.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_4.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_1.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_percent.setText(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_0.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_2.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_devide.setText(QtGui.QApplication.translate("Form", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_5.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_plus_minus.setText(QtGui.QApplication.translate("Form", "\00B1", None, QtGui.QApplication.UnicodeUTF8))