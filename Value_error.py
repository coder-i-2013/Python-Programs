try:
    num=int(input("Enter a number: "))
    print(" the value entered is", num)
except ValueError as ex:
    print("EXCEPTION!",ex)
