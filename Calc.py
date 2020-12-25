from tkinter import *

window = Tk()
window.title('calculator')
window.geometry('355x475')
window.configure(bg='#bfbfbf')
window.iconbitmap('calc_icon.ico')
window.resizable(False, False)

expression =''

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('bruh')
        expression =''

def clear():
    global expression
    expression = ''
    equation.set(0)

button_frame = Frame(window,bg='#bfbfbf')

button_frame.pack()

equation = StringVar()
equation.set('0')

expression_field = Entry(button_frame,textvariable=equation,
                         justify='right',font=('arial',20,'bold'))

button1 = Button(button_frame,text='1',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(1))
button2 = Button(button_frame,text='2',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(2))
button3 = Button(button_frame,text='3',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(3))
addition = Button(button_frame,text='+',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press('+'))

button4 = Button(button_frame,text='4',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(4))
button5 = Button(button_frame,text='5',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(5))
button6 = Button(button_frame,text='6',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(6))
subtract = Button(button_frame,text='-',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press('-'))

button7 = Button(button_frame,text='7',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(7))
button8 = Button(button_frame,text='8',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(8))
button9 = Button(button_frame,text='9',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(9))
multyply = Button(button_frame,text='*',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press('*'))

button0 = Button(button_frame,text='0',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press(0))
decimal = Button(button_frame,text='.',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press('.'))
clear = Button(button_frame,text='C',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=clear)
division = Button(button_frame,text='/',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=8,height=3,command=lambda:press('/'))

equal = Button(button_frame,text='=',font=('times new roman',12),
                 relief='groove',bd=1,bg='#d9d9d9',width=35,height=3,command=equalpress)

expression_field.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=10)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
addition.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subtract.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
multyply.grid(row=3,column=3)

decimal.grid(row=4,column=0)
button0.grid(row=4,column=1)
clear.grid(row=4,column=2)
division.grid(row=4,column=3)

equal.grid(row=5,column=0,columnspan=4,pady=10)

window.mainloop()
