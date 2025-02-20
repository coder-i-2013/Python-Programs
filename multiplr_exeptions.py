try:
    num1, num2=eval(input ("enter 2 numbers seprated by a comma."))
    result = num1/num2
    print("result is", result)
except ZeroDivisionError:
    print("The divison by zeros are errors")
except SyntaxError:
    print("the comma is missing. Enter 2 numbers seprated by a comma like this: 24,6")
except:
    print("WRONG INPUT")
else:
    print("No exceptions")
finally:
    print("This will be executed error or not")