import random
num= random.randint(1,10)
guessus=0
while guessus < 5:
    guess =int(input("Enter a number between 1 and 10: "))
    guessus= guessus+1
    if guess ==num:
        print("you got the correct number in",guessus,"guessus ")
        break
    elif num > guess :
        print("Your guess is lower than the number")
        break
    elif num < guess :
        print("Your guess is higher than the number")
else:
    print("you couldn't guess the number the number is",num)
    