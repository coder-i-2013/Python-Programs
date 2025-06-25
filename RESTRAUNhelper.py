import tkinter as tk
from tkinter import ttk,messagebox
class ResterauntOrderManagment:
    def __init__(self,root):
        self.root=root
        self.root.title(
            "Restaurant Menu App")
        self.menu_items={
            "Fries":2,
            "Lunch Meal": 6,
            "Burger Meal":5,
            "Pizza Meal": 4,
            "Chicken Sandwhich":3,
            "MAC and Cheese": 5,
            "Chicken Wings":7,
        }
        frame= ttk.Frame(master=root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)


        ttk.Label(frame,text="Resterant Menu App").grid(row=0,columnspan=3)

        self.menu_labels={}
        self.menu_quantities={}
        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(master=frame, text=f"{item}(${price}):")
            label.grid(row=i,column=0)
            self.menu_labels[item]=label

            quantity_entry= ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1)
            self.menu_quantities[item]=quantity_entry
            order_button=ttk.Button(frame,text="Place Order", command=self.place_order)
            order_button.grid(row=len(self.menu_items)+2,columnspan=3)
    def place_order(self):
        total_cost=0
        order_summary="Order Summary:\n"
        
        for item,entry in self.menu_quantities.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.menu_items[item]
                cost=quantity * price
                total_cost+=cost
                if quantity>0:
                    order_summary+=f"{item}: {quantity}x{price}={cost}\n"
            if total_cost > 0:
                order_summary+=f"\nTotal cost: {total_cost}"
                messagebox.showinfo("Order placed",order_summary)
            else:
                messagebox.showerror("Error","Please order at least one item.")

if __name__=="__main__":
    root=tk.Tk()
    app=ResterauntOrderManagment(root)
    root.geometry("800x600")
    root.mainloop()

            