n=int(input("Enter a value ans we will use it for n: "))
def sum(n):
    return n*(n+1)/2
print(sum(n))

c=int(input("Enter a value and we will use it for c: "))
def summ(c):
    if (c<=0):
        return 0
    else:
        return c+ summ(c-1)
print(summ(c))



def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
a=[12,3,4,15]
print("The total of a is equal to:",arraysum(a))

    