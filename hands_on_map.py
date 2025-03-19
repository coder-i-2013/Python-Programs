numbers1=[1,2,3]
numbers2=[4,5,6]
result= map(lambda x,y:x+y,numbers1,numbers2)
print("the Addition of both lists are:")
print(list(result))

#map
nums=[88,12,11]
def sq(n):
    return n**2
square=list(map(sq,nums))
print(square)