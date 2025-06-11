n=int(input("enter a value for N "))
def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)

prints(n)
