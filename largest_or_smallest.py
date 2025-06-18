number_largest=int(input("Enter your larger number: "))
number_smallest=int(input("Enter your smaller number: "))

while number_smallest:
    number_store=number_smallest
    number_smallest=number_largest % number_smallest
    number_largest= number_store

print("The GCF of these 2 numbers are:",number_largest)