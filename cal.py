import tkinter as tk

def click_button(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "x²":
        result= e**2
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  

entry = tk.Entry(root, width=16, font=("Arial", 30), borderwidth=10, relief=tk.GROOVE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipady=20)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("x²", 5, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 25), padx=30, pady=30, bg="#f0f0f0", activebackground="#d3d3d3", borderwidth=5)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", click_button)


for i in range(5):  
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)

root.mainloop()