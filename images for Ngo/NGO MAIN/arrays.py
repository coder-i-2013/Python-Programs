import array as arr
array_first=arr.array("i",[1,3,5,7,11,13,17,19])
print("The Orignal Array:"+(str(array_first)))

print("the occourances in the:"+str(array_first.count(5)))

array_first.reverse()
print("The reversed array of the greatest to the least is")
print(str(array_first))
