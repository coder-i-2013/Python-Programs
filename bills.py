units= int(input("please enter the number of units you consumed: "))
if units < 50:
    amt= units*2.6
    surcharge= 25
elif units <= 100:
    amt= 130+((units-50)*3.25)
    surcharge= 35
elif units <= 200:
    amt= 130+162.5+((units-100)*5.26)
    surcharge= 45
else:
    amt= 130+162.5+526+((units-200)*8.45)
    surcharge= 75
total= amt+surcharge
print("\n the total electricity bill %.2f" %total)
