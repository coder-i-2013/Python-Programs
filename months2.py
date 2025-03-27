import calendar

def display_months_and_days():
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        days = calendar.monthrange(2025, month)[1]  # Get the number of days in the selected month
        days_list = [str(day) for day in range(1, days + 1)]
        print(f"{month_name}: {', '.join(days_list)}")

# Call the function to display the months and days
display_months_and_days()
