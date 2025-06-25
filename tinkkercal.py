from tkinter import *
from datetime import date
window=Tk()
window.title("Demo Window")
window.geometry("400x300")
lbl=Label(text="Calculator",fg="white",bg="#072F5F",height =3,width=300)

number_1=Entry()

number_2=Entry()

name_lbl=Label(text="",bg="light blue",height=3,width=300)



def display():
    num1=number_1.get()
    num2=number_2.get()
    answer=num1*num2    
    global Message




bttn=Button(text="calculate",command=display, height=1,bg="blue",fg="white")
text_box=Text(text=answer, height=3)
lbl.pack()
name_lbl.pack()
number_1.pack()
number_2.pack()
bttn.pack()
text_box.pack()

 