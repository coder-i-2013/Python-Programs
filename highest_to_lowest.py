L =[4,5,1,2,7,9,8]
print("The original list is: ",L)

count=0
for i in L:
    count += i
avg =count/len(L)
print("the sum is ",count)
print("the average is", avg)
L.sort()

print("The smallest element is",L[0])
print("the highest element is ",L[-1])


