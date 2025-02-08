def DecToBia(num):
    if num>=1:
        DecToBia(num//2)
    print(num % 2,end="")
dtb=float(input("Enter a number to convert: "))
DecToBia(dtb)