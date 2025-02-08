decimal_num = float(input("Enter a decimal number: "))
binary_num = ""

while decimal_num > 0:
    binary_num = str(decimal_num % 2) + binary_num
    decimal_num = decimal_num // 2

print("Binary representation is:", binary_num)
