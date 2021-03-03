# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python_projects\ToDoList\new_todolisti.ui'
#
# Created: Wed Dec 23 11:51:26 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(402, 545)
        Form.setStyleSheet("background-color: #968c83;\n"
"")
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 381, 241))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.listWidget.setFont(font)
        self.listWidget.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.listWidget.setMouseTracking(True)
        self.listWidget.setStyleSheet("background-color: #8db596;\n"
"border: 1px solid #f0ece3;\n"
"color: #f0ece3;\n"
"padding: 7px;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(30, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.dateEdit.setFont(font)
        self.dateEdit.setCursor(QtCore.Qt.PointingHandCursor)
        self.dateEdit.setMouseTracking(False)
        self.dateEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit.setAcceptDrops(True)
        self.dateEdit.setToolTip("")
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setStyleSheet("border: none;\n"
"color: #f0ece3;")
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setKeyboardTracking(False)
        self.dateEdit.setDate(QtCore.QDate(2020, 12, 23))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(240, 40, 131, 31))
        self.progressBar.setCursor(QtCore.Qt.WaitCursor)
        self.progressBar.setMouseTracking(True)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTip("")
        self.progressBar.setStatusTip("")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("border-left:1px solid black;\n"
"border-right:1px solid black;\n"
"color: #f0ece3;")
        self.progressBar.setProperty("value", 59)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 381, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_addNote = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pb_addNote.setFont(font)
        self.pb_addNote.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_addNote.setStyleSheet("background-color: #cbaf87;\n"
"color: #f0ece3;\n"
"border: none;\n"
"padding:5px;")
        self.pb_addNote.setObjectName("pb_addNote")
        self.verticalLayout.addWidget(self.pb_addNote)
        self.pb_delNote = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.pb_delNote.setFont(font)
        self.pb_delNote.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_delNote.setStyleSheet("background-color: #cbaf87;\n"
"color: #f0ece3;\n"
"border: none;\n"
"padding:5px;")
        self.pb_delNote.setObjectName("pb_delNote")
        self.verticalLayout.addWidget(self.pb_delNote)
        self.pb_save = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.pb_save.setFont(font)
        self.pb_save.setCursor(QtCore.Qt.PointingHandCursor)
        self.pb_save.setStyleSheet("background-color: #cbaf87;\n"
"color: #f0ece3;\n"
"border: none;\n"
"padding:5px;")
        self.pb_save.setObjectName("pb_save")
        self.verticalLayout.addWidget(self.pb_save)
        self.pb_delAll = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.pb_delAll.setFont(font)
        self.pb_delAll.setStyleSheet("background-color: #cbaf87;\n"
"color: #f0ece3;\n"
"border: none;\n"
"padding:5px;")
        self.pb_delAll.setObjectName("pb_delAll")
        self.verticalLayout.addWidget(self.pb_delAll)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 340, 381, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #8db596;\n"
"color: #f0ece3;\n"
"border: 1px solid #f0ece3;")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 320, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #f0ece3;")
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 520, 191, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_addNote.setText(QtGui.QApplication.translate("Form", "Add Note", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_delNote.setText(QtGui.QApplication.translate("Form", "Delete Note", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_save.setText(QtGui.QApplication.translate("Form", "Save Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_delAll.setText(QtGui.QApplication.translate("Form", "Delete All Noties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Your Notice", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "© Copyright 2020. All Rights Reserved.", None, QtGui.QApplication.UnicodeUTF8))