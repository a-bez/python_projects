from tkinter import *
root = Tk()


# interface

lbl_loanAmount = Label(text='Сумма кредита')
lbl_loanAmount.pack()

entr_loanAmount = Entry()
entr_loanAmount.pack()

lbl_monthlyInterestRate = Label(text='Месячная процентная ставка')
lbl_monthlyInterestRate.pack()

entr_monthlyInterestRate = Entry()
entr_monthlyInterestRate.pack()

lbl_term = Label(text='срок в месяцах')
lbl_term.pack()

entr_term = Entry()
entr_term.pack()






# logic



def credit():
  loanAmount = entr_loanAmount.get()
  monthlyInterestRate = entr_monthlyInterestRate.get()
  term = entr_term.get()

  try:
    loanAmount = int(loanAmount)
    monthlyInterestRate = float(monthlyInterestRate)
    term = int(term)
  except ValueError:
    return None

  mounthlyRate = int(loanAmount / term)          # ежемесячный платеж основной суммы 2к,4к,6к,8к,10к.
  global counter
  counter = 0
  for i in range(0, loanAmount+1, mounthlyRate):
    counter += (i * monthlyInterestRate) / 100
  #print(round(counter, 3))
  estimated_amount = Label(text='вы должны: {}'.format(counter))
  estimated_amount.pack()


btn = Button(text='Подсчитать', command=credit)
btn.pack()



root.mainloop()