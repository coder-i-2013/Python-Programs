squishy_world=2*2
print("Welcome to the squishy store")
color = input("Pick a color for your squishy. Each color has a different price\n 1. blue: 4.50 \n 2. pink: 3.50 \n 3. teal: 4.75 \n 4. yellow: 2.50\n Pick a color: ")

if color == "blue":
    total = 4.50
    print("Your color total is", total)
elif color == "pink":
    total = 3.50
    print("Your color total is", total)
elif color == "teal":
    total = 4.75
    print("Your color total is", total)
elif color == "yellow":
    total = 2.50
    print("Your color total is", total)
else:
    print("Invalid color selected. Please run the program again.")
    exit()

animal = input("\nPick an animal for your squishy. Each animal has a different price\n 1. panda: 8.50 \n 2. elephant: 7.50 \n 3. bunny: 8.75 \n 4. narwhal: 6.50\n Pick an animal: ")

if animal == "panda":
    total += 8.50
    print("Your complete total is", total)
elif animal == "elephant":
    total += 7.50
    print("Your complete total is", total)
elif animal == "bunny":
    total += 8.75
    print("Your complete total is", total)
elif animal == "narwhal":
    total += 6.50
    print("Your complete total is", total)
else:
    print("Invalid animal selected. Please run the program again.")
    exit()

number = int(input("Enter the amount of these squishies you want: "))
c_total = number * total
print("Your final total is ", c_total)

paid_total = float(input("How much would you like to pay right now: "))
amount_due = c_total - paid_total
percent_back = 0.15 * c_total
name = input("Pick the name of your squishy: ")

if round(amount_due, 2) == 0.00:
    print("You get", percent_back, "back.")
    pay_now = c_total - percent_back
    print("Pay", pay_now)
elif amount_due > 0.00:
    print("Pay", paid_total)
    print("Your due amount is", amount_due)
print("Hope you enjoy",name,":)")
