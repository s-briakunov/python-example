# *- coding: utf-8 -*-
from Tkinter import *
from math import *

def solve():
    a = float(a_entry.get())
    S=0
    v = var.get()
    if v==1:        
        h = float(c_entry.get())
        S=a*h*1/2
    if v==2:
        b = float(b_entry.get())
        h = float(c_entry.get())
        S=(a+b)*h*1/2
    if v==3:
        b = float(b_entry.get())
        S=pi*a*b
    try:
        f_x = "%10.2f" % (S)            
    except:
        f_x = "?"
    k_label.configure(text=f_x)

root=Tk()
root.title("Задание 3")
frame = Frame(root, width=480,height=300)
frame.pack()
var=IntVar()
var.set(1)

t1_label = Label(text="Расчет площади фигуры", font='arial 14')
t1_label.place(x=120, y=10)

x=Radiobutton(variable=var,value=1).place(x=20, y=40)
xl=Label(text="треугольник").place(x=40,y=40)
y=Radiobutton(variable=var,value=2).place(x=20, y=60)
yl=Label(text="трапеция").place(x=40,y=60)
z=Radiobutton(variable=var,value=3).place(x=20, y=80)
zl=Label(text="эллипс").place(x=40,y=80)

a_label = Label(text="Введите сторону треугольника (основание трапеции, ось эллипса)")
a_label.place(x=20, y=120)
a_entry = Entry(width=10)
a_entry.place(x=400, y=120)

b_label = Label(text="Введите второе основание трапеции (вторую ось эллипса)")
b_label.place(x=20, y=140)
b_entry = Entry(width=10)
b_entry.place(x=400, y=140)

c_label = Label(text="Введите высоту треугольника (трапеции)")
c_label.place(x=20, y=160)
c_entry = Entry(width=10)
c_entry.place(x=400, y=160)

k1_label = Label(text="Площадь фигуры = ")
k1_label.place(x=120, y=200)
k_label = Label(width=10,bg='white', text="?")
k_label.place(x=250, y=200)

button = Button(text="Вычислить", width=10, bg='#5C3317', fg='#C0C0C0', font='arial 14', command=solve)
button.place(x=100, y=240)
exit_button = Button(text="Выход", width=10, bg='#5C3317', fg='#C0C0C0', font='arial 14', command=root.destroy)
exit_button.place(x=250, y=240)

root.mainloop()



