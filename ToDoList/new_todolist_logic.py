from PySide import QtCore, QtGui
import sys
from new_todolist import Ui_Form

import pickle

# инициализация приложения
app = QtGui.QApplication(sys.argv)

Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

lineEditText = ''   # вспомагательная переменная для переноса значения из ui.lineEdit в ui.listWidget

# добавить элемент в список из lineEdit
def pb_addNote():
  global lineEditText
  lineEditText = lineEditText + ui.lineEdit.text()
  if lineEditText != '':                                        #исключить добавления путсых строк!
    ui.listWidget.addItem(lineEditText)
    ui.lineEdit.clear()
  else:
    pass
  lineEditText = lineEditText[0:0]

ui.pb_addNote.clicked.connect(pb_addNote)

# удалить выделеный элемент
def pb_delNote():
  delRow = ui.listWidget.selectedItems()
  for SelectedItem in delRow:
    ui.listWidget.takeItem(ui.listWidget.row(SelectedItem))

ui.pb_delNote.clicked.connect(pb_delNote)

# удаление всех элементов из списка
def pb_delAll():
  ui.listWidget.clear()

ui.pb_delAll.clicked.connect(pb_delAll)

# сохранение списка в файл
def pb_save():
  pass

ui.pb_save.clicked.connect(pb_save)

# загрузка списка из файла
def pb_load():
  pass

ui.pb_load.clicked.connect(pb_load)

sys.exit(app.exec_())