# *- coding: utf-8 -*-
from Tkinter import *
from math import *
# описание функции
def func(x,y):
    return (1-x**2)/(x*y)

def fx(x_i,y_i,x_k,n_1):
# шаг интегрирования
    h=(x_k-x_i)/n_1
#Модифицированный метод эйлера (В-1)
    for i in range (0,n_1):
        y1=y_i+h*func(x_i+(h/2),y_i+h*func(x_i,y_i)/2)
        x1=x_i+h
        x_i=x1
        y_i=y1
    return y1

def rk(x_i,y_i,x_k,n_1):
    h=(x_k-x_i)/n_1
# метод рунге-кутта
    for i in range (0,n_1):
        k1=h*func(x_i,y_i)
        k2=h*func(x_i+h/2,y_i+k1/2)
        k3=h*func(x_i+h,y_i+2*k2-k1)
        y1=y_i+(k1+4*k2+k3)/6
        x_i=x_i+h
        y_i=y1
    return y1

def calculate_y1():
# начальные условия
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
# конечная точка
    xk = float(xk_entry.get())
# число разбиений
    n = int(n_entry.get())
# использование обработки исключений. Сначала выполняется ветвь try
    try:
        y1 = "%11.3f" % fx(x0,y0,xk,n)
        y2 = "%11.3f" % rk(x0,y0,xk,n)
# если во время выполнения try возникает исключение,
# то дальнейшее выполнение try прекращается и выполняется ветвь except
    except:
        y1 = "?"
        y2 = "?"
    y1_label.configure(text=y1)
    y2_label.configure(text=y2)
    
root=Tk()

root.title("задача 5")
frame = Frame(root)
frame.pack()

t1_label = Label(frame, bg='lightyellow', text="Численное решение дифференциальных уравнений первого порядка", font='arial 10')
t1_label.grid(row=0, column=1, columnspan=4, padx=25,pady=15)

x0_entry = Entry(frame, bg="lightblue", width=10)
x0_entry.grid(row=2, column=0)
x0_lebel = Label(frame, text="Начальное значение X")
x0_lebel.grid(row=1, column=0)

y0_entry = Entry(frame, bg="lightblue", width=10)
y0_entry.grid(row=2, column=1)
y0_lebel = Label(frame, text="Начальное значение Y")
y0_lebel.grid(row=1, column=1)

xk_entry = Entry(frame, bg="lightblue", width=10)
xk_entry.grid(row=2, column=2)
xk_lebel = Label(frame, text="Конечное значение Х")
xk_lebel.grid(row=1, column=2)

n_entry = Entry(frame, bg="lightblue", width=10)
n_entry.grid(row=2, column=3)
n_lebel = Label(frame, text="Число разбиений")
n_lebel.grid(row=1, column=3)

y1_label = Label(frame, text="?")
y1_label.grid(row=5, column=1)
y1_lebel = Label(frame, text="Модифицированный метод Эйлера (вариант 2)")
y1_lebel.grid(row=4, column=1)
# 
y2_label = Label(frame, text="?")
y2_label.grid(row=5, column=2)
y2_lebel = Label(frame, text="Метод Рунге-Кутта третьего порядка")
y2_lebel.grid(row=4, column=2)
# 
eval_button = Button(frame, text="Вычислить", width=10,
                     command=calculate_y1)
eval_button.grid(row=8, column=0)
#
exit_button = Button(frame, text="Выход", width=10,
                     command=root.destroy)
exit_button.grid(row=8, column=3)
#
canvas1 = Canvas(frame, width =200, height=80)
img = PhotoImage(file='./1.gif')
canvas1.create_image(150, 50, image=img, anchor=CENTER)
canvas1.grid(row=3, columnspan=4)
#
root.mainloop()
