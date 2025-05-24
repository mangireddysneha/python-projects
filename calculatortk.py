from tkinter import *
a=Tk()

def b_click(number):
    global operator
    operator=operator+str(number)
    input.set(operator)

def b_clear():
    global operator
    operator=""
    input.set("")

def b_equal():
    global operator
    result=str(eval(operator))
    input.set(result)
    operator=""

    
a.title("calculator")
operator=""
input=StringVar()
display = Entry(a, font=("arial", 30, "bold"), textvariable=input, bg="#AFEEEE", bd=30, insertwidth=4, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)

'''ROW 1'''
b7=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="7",command=lambda:b_click(7))
b7.grid(row=1,column=0)
b8=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="8",command=lambda:b_click(8))
b8.grid(row=1,column=1)
b9=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="9",command=lambda:b_click(9))
b9.grid(row=1,column=2)
b_mul=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="*",command=lambda:b_click("*"))
b_mul.grid(row=1,column=3)

'''ROW 2'''
b4=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="4",command=lambda:b_click(4))
b4.grid(row=2,column=0)
b5=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="5",command=lambda:b_click(5))
b5.grid(row=2,column=1)
b6=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="6",command=lambda:b_click(6))
b6.grid(row=2,column=2)
b_sub=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="-",command=lambda:b_click("-"))
b_sub.grid(row=2,column=3)

'''ROW 3'''
b1=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="1",command=lambda:b_click(1))
b1.grid(row=3,column=0)
b2=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="2",command=lambda:b_click(2))
b2.grid(row=3,column=1)
b3=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="3",command=lambda:b_click(3))
b3.grid(row=3,column=2)
b_add=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="+",command=lambda:b_click("+"))
b_add.grid(row=3,column=3)

'''ROW 4'''
b0=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="0",command=lambda:b_click(0))
b0.grid(row=4,column=0)
bc=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="c",command=b_clear)
bc.grid(row=4,column=1)
b_equal=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="=",command=b_equal)
b_equal.grid(row=4,column=2)
b_div=Button(a,padx=10,bd=10,fg="black",font=("arial",20),text="/",command=lambda:b_click("/"))
b_div.grid(row=4,column=3)

a.mainloop()
