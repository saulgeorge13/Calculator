from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth= 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    current = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(current)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, first_num + int(second_num))
    if math == "subtraction":
        e.insert(0, first_num - int(second_num))
    if math == "multiplication":
        e.insert(0, first_num * int(second_num))
    if math == "division":
        e.insert(0, first_num / int(second_num))

def button_sub():
    current = e.get()
    global first_num
    global math
    math = "subtraction"
    first_num = int(current)
    e.delete(0, END)

def button_mul():
    current = e.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(current)
    e.delete(0, END)

def button_div():
    current = e.get()
    global first_num
    global math
    math = "division"
    first_num = int(current)
    e.delete(0, END)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonEqual = Button(root, text="=", padx=85, pady=20, command=button_equal)
buttonClr = Button(root, text="CLR", padx=80, pady=20, command=button_clear)
buttonSub = Button(root, text="-", padx=41, pady=20, command=button_sub)
buttonMul = Button(root, text="*", padx=40, pady=20, command=button_mul)
buttonDiv = Button(root, text="/", padx=40, pady=20, command=button_div)

button1.grid(row= 3, column= 0)
button2.grid(row= 3, column= 1)
button3.grid(row= 3, column= 2)
button4.grid(row= 2, column= 0)
button5.grid(row= 2, column= 1)
button6.grid(row= 2, column= 2)
button7.grid(row= 1, column= 0)
button8.grid(row= 1, column= 1)
button9.grid(row= 1, column= 2)
button0.grid(row= 4, column= 0)
buttonAdd.grid(row= 5, column= 0)
buttonEqual.grid(row= 5, column= 1, columnspan=2)
buttonClr.grid(row= 4, column= 1, columnspan=2)
buttonSub.grid(row= 6, column= 0)
buttonMul.grid(row= 6, column= 1)
buttonDiv.grid(row= 6, column= 2)

root.mainloop()

