from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk, )

from matplotlib.figure import Figure


def solve_eq():
    display1.delete(0, 'end')

    x1 = int(entry1.get())
    y1 = int(entry3.get())
    a = int(entry5.get())
    x2 = int(entry2.get())
    y2 = int(entry4.get())
    b = int(entry6.get())

    str1 = "The two equations do not intersect each other.They are parallel lines."
    str2 = "The two equations are same and every point on the line is the solution."

    if (x1 == x2) & (y1 == y2) & (a != b):
        display1.insert(0, str1)

    elif (x1 == x2) & (y1 == y2) & (a == b):
        display1.insert(0, str2)

    elif x1 != x2 | y1 != y2:
        A = np.matrix([[x1, y1], [x2, y2]])
        B = np.matrix([[a], [b]])
        display1.insert(0, "The solution is : ")
        display1.insert('end', np.linalg.solve(A, B))


def show_graph():
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(-5, 5, 100)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    x1 = int(entry1.get())
    y1 = int(entry3.get())
    a = int(entry5.get())
    x2 = int(entry2.get())
    y2 = int(entry4.get())
    b = int(entry6.get())

    ya = -((x1/y1)*x) + (a/y1)
    fig.add_subplot(1, 1, 1).plot(x, ya, label=entry1.get() + "x + " + entry3.get() + "y = " + entry5.get())
    yb = -((x2 / y2)*x) + (b/y2)
    fig.add_subplot(1, 1, 1).plot(x, yb, label=entry2.get() + "x + " + entry4.get() + "y = " + entry6.get())
    fig.legend(loc='upper left')
    canvas = FigureCanvasTkAgg(fig, master=label10)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, label10)
    toolbar.update()
    canvas.get_tk_widget().pack()


def show_entry():
    display.delete(0, 'end')
    t1 = "The equations are : " + entry1.get() + "x + " + entry3.get() + "y" + " = " + entry5.get() + " and " + entry2.get() + "x + " + entry4.get() + "y = " + entry6.get() + "."
    display.insert(0, t1)


root = Tk()

display = Entry(root)
display1 = Entry(root)
display.grid(row=11, columnspan=6, sticky=W + E)
display1.grid(row=29, columnspan=6, sticky=W + E)


label0 = Label(root, text="Enter the value of the equation in the format 'x1'x + 'y1'y = a and 'x2'x + 'y2'y = b.")
label1 = Label(root, text="x1 Value : ")
label2 = Label(root, text="y1 Value : ")
label3 = Label(root, text="x2 Value : ")
label4 = Label(root, text="y2 Value : ")
label5 = Label(root, text="a Value : ")
label6 = Label(root, text="b Value : ")
label7 = Label(root)
label8 = Label(root)
label9 = Label(root)
label10 = Label(root)
label11 = Label(root)

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)

label0.grid(row=0, columnspan=6)
label1.grid(row=1, column=0)
label2.grid(row=1, column=2)
label3.grid(row=2, column=0)
label4.grid(row=2, column=2)
label5.grid(row=1, column=4)
label6.grid(row=2, column=4)
label7.grid(row=10, column=0)
label9.grid(row=10, column=1)
label10.grid(row=12, columnspan=6)
label11.grid(row=10, column=2)

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=1, column=3)
entry4.grid(row=2, column=3)
entry5.grid(row=1, column=5)
entry6.grid(row=2, column=5)

button1 = Button(label7, text="Show Entries", command=show_entry)
button2 = Button(label9, text="Show Graph", command=show_graph)
button3 = Button(label11, text="Show Solution", command=solve_eq)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
