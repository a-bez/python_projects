from PyQt5 import QtCore, QtGui, QtWidgets
from pass_gen_ui import Ui_Form
from dialog import Ui_Dialog
import sys
import random

    
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#password generator


chars = ''



def add_simbols(self):
    global chars
    if ui.checkBox.isChecked():
        chars += '!@#$%^&*_=+><'
    else:
        chars = chars[0:13]

def add_nums(self):
    global chars
    if ui.checkBox_2.isChecked():
        chars += '0123456789'
    else:
        chars = chars[0:10]

def add_capLat(self):
    global chars
    if ui.checkBox_3.isChecked():
        chars += 'ABCDEFGHIJKLOPQRSTUVWXYZ'
    else:
        chars = chars[0:24]

def add_smlLat(self):
    global chars
    if ui.checkBox_4.isChecked():
        chars += 'abcdefghijklnopqrstuvwxyz'
    else:
        chars = chars[0:24]


global pass_len
global password

def pass_gen(self):
    try:
        password = ''
        pass_len = int(ui.spinBox.value())
        for i in range(pass_len):
            password += random.choice(chars)
        ui.passwod_output.setText(password)
        password = password[0:0]
    except Exception:
        ui.passwod_output.setText('Настройте параметры генерации ☟')
        ui.passwod_output.setStyleSheet('color : #FF0000;')


    

ui.checkBox.stateChanged.connect(add_simbols)
ui.checkBox_2.stateChanged.connect(add_nums)
ui.checkBox_3.stateChanged.connect(add_capLat)
ui.checkBox_4.stateChanged.connect(add_smlLat)

ui.pushButton.clicked.connect(pass_gen)




sys.exit(app.exec_())