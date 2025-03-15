from datetime import date,time,datetime
today= date.today()
now= datetime.now()
print("Today's date is ",today)
print("Current date and time is",now)
print("Today's date components are ", today.day, today.month, today.year)