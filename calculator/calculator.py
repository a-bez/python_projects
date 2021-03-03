import sys
from PySide import QtCore, QtGui
from calc import Ui_Form
import math


app = QtGui.QApplication(sys.argv)

Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

symbol = ''
view_numbers = ''                     # переменная для вывода набераемого числа
num_1 = ''
num_2 = ''

# logic for buttons
# функции цифровых копок
def pb_0():
  global view_numbers                 # ввод переменной в функцию
  global num_1                        # ввод переменной в функцию
  view_numbers = view_numbers + '0'   # добавление значений в переменную
  ui.lineEdit.setText(view_numbers)   # обращение к интерфейсу, поле вывода и вывод содержимого переменной с помощью метода setText()
  num_1 = num_1 + '0'                 # сохранение первого введеного числа в отдельную переменную

ui.pb_0.clicked.connect(pb_0)         # вызов функции pb_0() по нажатию на кнопку pb_0

def pb_1():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '1'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '1'

ui.pb_1.clicked.connect(pb_1)

def pb_2():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '2'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '2'

ui.pb_2.clicked.connect(pb_2)

def pb_3():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '3'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '3'

ui.pb_3.clicked.connect(pb_3)

def pb_4():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '4'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '4'

ui.pb_4.clicked.connect(pb_4)

def pb_5():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '5'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '5'

ui.pb_5.clicked.connect(pb_5)

def pb_6():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '6'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '6'

ui.pb_6.clicked.connect(pb_6)

def pb_7():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '7'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '7'

ui.pb_7.clicked.connect(pb_7)

def pb_8():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '8'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '8'

ui.pb_8.clicked.connect(pb_8)

def pb_9():
  global view_numbers
  global num_1
  view_numbers = view_numbers + '9'
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1 + '9'

ui.pb_9.clicked.connect(pb_9)

# функции операционных кнопок
#def pb_devide():
#  global view_numbers
#  global num_1
#  view_numbers = view_numbers + '/'
#  ui.lineEdit.setText(view_numbers)
#  num_1 = num_1 + '/'

#ui.pb_devide.clicked.connect(pb_devide)

#def pb_multiply():
#  global view_numbers
#  global num_1
#  view_numbers = view_numbers + '*'
#  ui.lineEdit.setText(view_numbers)
#  num_1 = num_1 + '*'

#ui.pb_multiply.clicked.connect(pb_multiply)

#def pb_plus():
#  global view_numbers
#  global num_1
#  view_numbers = view_numbers + '+'
#  ui.lineEdit.setText(view_numbers)
#  num_1 = num_1 + '+'

#ui.pb_plus.clicked.connect(pb_plus)

#def pb_minus():
#  global view_numbers
#  global num_1
#  view_numbers = view_numbers + '-'
#  ui.lineEdit.setText(view_numbers)
#  num_1 = num_1 + '-'

#ui.pb_minus.clicked.connect(pb_minus)

def pb_dot():
  global view_numbers
  global num_1
  if '.' in num_1:
    pass
  else:
    num_1 = num_1 + '.'
    view_numbers = view_numbers + '.'
    ui.lineEdit.setText(view_numbers)

ui.pb_dot.clicked.connect(pb_dot)

def pb_percent():
  global view_numbers
  global num_1
  if '-' in view_numbers or '+' in view_numbers or '/' in view_numbers or '×' in view_numbers or '%' in view_numbers:
    pass
  else:
    num_1 = float(num_1)
    num_1 = num_1 * 0.01
    num_1 = str(num_1)
    view_numbers = num_1
    ui.lineEdit.setText(view_numbers)

ui.pb_percent.clicked.connect(pb_percent)

#factorial
#def pb_plus_minus():
# global view_numbers
#  global num_1
#  fact = 1
#  num_1 = int(num_1)
#  for i in range(1, num_1 + 1):
#    fact = fact * i
#  num_1 = fact
#  num_1 = str(num_1)
#  view_numbers = num_1
#  ui.lineEdit.setText(view_numbers)

#ui.pb_plus_minus.clicked.connect(pb_plus_minus)

# очистка поля
def pb_del_one():
  global view_numbers
  global num_1
  view_numbers = view_numbers [0:-1]
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1[0:-1]

ui.pb_del_one.clicked.connect(pb_del_one)

def pb_del_all():
  global view_numbers
  global num_1
  view_numbers = view_numbers[0:0]
  ui.lineEdit.setText(view_numbers)
  num_1 = num_1[0:0]

ui.pb_del_all.clicked.connect(pb_del_all)

# вичислительная логика

def pb_devide():
  global view_numbers
  global num_1
  global num_2
  global symbol
  if '+' in view_numbers or '-' in view_numbers or '×' in view_numbers or '/' in view_numbers or '%' in view_numbers:
    pass
  else:
    view_numbers = view_numbers + '/'
    ui.lineEdit.setText(view_numbers)
    symbol = '/'
    num_2 = num_1
    num_1 = ''

ui.pb_devide.clicked.connect(pb_devide)

def pb_multiply():
  global view_numbers
  global num_1
  global num_2
  global symbol
  if '+' in view_numbers or '-' in view_numbers or '×' in view_numbers or '/' in view_numbers or '%' in view_numbers:
    pass
  else:
    view_numbers = view_numbers + '×'
    ui.lineEdit.setText(view_numbers)
    symbol = '×'
    num_2 = num_1
    num_1 = ''

ui.pb_multiply.clicked.connect(pb_multiply)

def pb_minus():
  global view_numbers
  global num_1
  global num_2
  global symbol
  if '+' in view_numbers or '-' in view_numbers or '×' in view_numbers or '/' in view_numbers or '%' in view_numbers:
    pass
  else:
    view_numbers = view_numbers + '-'
    ui.lineEdit.setText(view_numbers)
    symbol = '-'
    num_2 = num_1
    num_1 = ''

ui.pb_minus.clicked.connect(pb_minus)

def pb_plus():
  global view_numbers
  global num_1
  global num_2
  global symbol
  if '+' in view_numbers or '-' in view_numbers or '×' in view_numbers or '/' in view_numbers or '%' in view_numbers:
    pass
  else:
    view_numbers = view_numbers + '+'
    ui.lineEdit.setText(view_numbers)
    symbol = '+'
    num_2 = num_1
    num_1 = ''

ui.pb_plus.clicked.connect(pb_plus)

def pb_equally():
  global view_numbers
  global symbol
  global num_1
  global num_2
  if symbol == '+':
    num_1 = float(num_1)
    num_2 = float(num_2)
    answer = num_1 + num_2
    num_1 = answer
    answer = str(answer)
    ui.lineEdit.setText(answer)
    num_1 = str(num_1)
    num_2 = str(num_2)
    view_numbers = num_1
    answer = ''
  elif symbol == '-':
    num_1 = float(num_1)
    num_2 = float(num_2)
    answer = num_2 - num_1
    num_1 = answer
    answer = str(answer)
    ui.lineEdit.setText(answer)
    num_1 = str(num_1)
    num_2 = str(num_2)
    view_numbers = num_1
    answer = ''
  elif symbol == '×':
    num_1 = float(num_1)
    num_2 = float(num_2)
    answer = num_1 * num_2
    num_1 = answer
    answer = str(answer)
    ui.lineEdit.setText(answer)
    num_1 = str(num_1)
    num_2 = str(num_2)
    view_numbers = num_1
    answer = ''
  elif symbol == '/':
    num_1 = float(num_1)
    num_2 = float(num_2)
    answer = num_2 / num_1
    num_1 = answer
    answer = str(answer)
    ui.lineEdit.setText(answer)
    num_1 = str(num_1)
    num_2 = str(num_2)
    view_numbers = num_1
    answer = ''
  else:
    ui.lineEdit.setText('error')

ui.pb_equally.clicked.connect(pb_equally)

sys.exit(app.exec_())