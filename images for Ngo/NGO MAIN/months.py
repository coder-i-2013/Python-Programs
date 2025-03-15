import calendar

def show_days(month):
    days = calendar.monthrange(2025, month)[1]  # Get the number of days in the selected month
    days_list = [str(day) for day in range(1, days + 1)]
    messagebox.showinfo(f"Days in {calendar.month_name[month]}", ", ".join(days_list))


def create_month_buttons():
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        button = tk.Button(root, text=month_name, command=lambda m=month: show_days(m))
        button.pack(pady=5)


# Create the main GUI window
root = tk.Tk()
root.title("Months and Days")

# Add a label
label = tk.Label(root, text="Click on a month to see its days", font=("Helvetica", 14))
label.pack(pady=10)

# Create buttons for each month
create_month_buttons()

# Start the GUI event loop
root.mainloop()
