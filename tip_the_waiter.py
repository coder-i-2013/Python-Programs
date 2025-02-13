def total_calc(bill,tip_perc):
    total = bill*(1+0.01*tip_perc)
    total=round(total,2)
    print("Please pay",total)

total_calc(45.00,10)