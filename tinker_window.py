from tkinter import *
from datetime import date
window=Tk()
window.title("Demo Window")
window.geometry("400x300")
lbl=Label(text="Hey",fg="white",bg="#072F5F",height =3,width=300)
name_lbl=Label(text="Enter Your Full Name",bg="light blue",height=3,width=300)
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcome to the Application \nToday's date is: "
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
bttn=Button(text="Begin",command=display, height=1,bg="blue",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
bttn.pack()
text_box.pack()
window.mainloop()

 