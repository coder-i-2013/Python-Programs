def print_factors(num):
    print("the factors of",num,"are: ")
    for i in range(1,num + 1):
        if num % i == 0:
            print(i)

num=int(input("Enter a number to find its factor/s: "))
print_factors(num)