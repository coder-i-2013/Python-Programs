from tkinter import *
window=Tk()
window.geometry("100x100")
window.title("Event Handler")

def handle_keypress(event):
    
    print(event.char)
window.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

button =Button(text="click me!")
button.pack()
button.bind("<Button-1>",handle_click)

window.mainloop()