from tkinter import * 
from tkinter import messagebox
root=Tk()
root.geometry("300x300")
def msg():
        messagebox.showwarning("Alert","STOP! A Virus Has Been Found")
button=Button(root, text="Scan for a virus",command=msg)
button.place(x=40,y=80)

root.mainloop()


