import copy
import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

window = Tk()
window.title("Кредитный калькулятор")
window.geometry('500x400')
pereplats = []

frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)
sum = Label(frame,text="Cумма кредита:  ")
sum.grid(row=1, column=1)

period = Label(frame,text="Период кредитования:  ",)
period.grid(row=2, column=1)

proc = Label(frame,text="Процентная ставка:  ")
proc.grid(row=3, column=1)

okno_sum = Entry(frame,)
okno_sum.grid(row=1, column=2)

okno_period = Entry(frame,)
okno_period.grid(row=2, column=2)

okno_proc = Entry(frame,)
okno_proc.grid(row=3,column=2)

#okno_vid = Entry(frame,)
#okno_vid.pack()


def tabl(arr):

    tabl = Tk()
    tabl.title("Платежи")
    tree = ttk.Treeview(tabl, show='headings')

    heads = ['Номер платежа', 'Сумма платежа', 'Остаток по кредиту']
    tree['columns'] = heads

    for header in heads:
        tree.heading(header, text=header, anchor='center')
        tree.column(header,anchor='center')

    for row in arr:
        tree.insert("",tk.END, values=row)

    tree.pack(expand=tk.YES, fill=tk.BOTH)


def anuit():
    kred = []
    summ = int(okno_sum.get())
    period = int(okno_period.get())
    stavka = int(okno_proc.get())

    procent = int(stavka) / 100
    i = procent / 12
    po = math.pow((1 + i), int(period))
    k = (i * po)/(po - 1)
    a = k * int(summ)
    prockred = a * int(period)
    perepl = prockred - int(summ)
    pereplats.append(round(perepl))

    for x in range(int(period)):
        prockred = prockred - a
        dop = []
        dop.append(x+1)
        dop.append(round(a))
        dop.append(round(prockred))
        kred.append(dop)

    tabl(kred)


def dif():
    kred = []
    summ = int(okno_sum.get())
    period = int(okno_period.get())
    stavka = int(okno_proc.get())

    perepl = 0
    sum = int(summ)
    i = int(stavka)/100
    sp = sum / int(period)  # сумма платежа по основному долгу

    for x in range(int(period)):
        ip = sum * i / 12       #сумма платежа по начисленным процентам
        p = sp + ip
        perepl = perepl + ip
        sum = sum - sp
        dop = []
        dop.append(x+1)
        dop.append(round(p))
        dop.append(round(sum))
        kred.append(dop)

    pereplats.append(round(perepl))
    tabl(kred)


def raz_pereplat():
    dif()
    anuit()
    per = pereplats[1] - pereplats[0]
    messagebox.showinfo('Разница переплат ', f'Разница между кредитами = {per}')


calcraz_button = Button(frame, text='Посчитать разницу кредитов', command=raz_pereplat)
calcraz_button.grid(row=5, column=1)

calcdif_button = Button(frame,text='Рассчитать дифф. кредит', command=dif)
calcdif_button.grid(row=4, column=1)

calcanut_button = Button(frame, text='Рассчитать ануит. кредит',command=anuit)
calcanut_button.grid(row=4, column=2)

window.mainloop()
