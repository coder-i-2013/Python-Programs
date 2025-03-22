fruits = ["apple", "banana", "cherry", "date", "strawbwrry"]
number = int(input("Enter a number: "))
odd_numbers = [x for x in range(1, number + 1) if x % 2 != 0]
print("List of odd numbers:", odd_numbers)
updated_fruits = [fruit.upper() for fruit in fruits]
print("Updated list of fruits:", updated_fruits)
