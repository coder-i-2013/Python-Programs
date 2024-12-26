sale_price=float(input("Enter the sales price: "))
actual_price=float(input("Enter the actual price: "))
if actual_price<sale_price:
    profit= sale_price - actual_price
    print("The profit of the business was", profit)
else:
    print("No profit")

