string1=input("Enter a word of choice: ")
char= input("Enter a character to check the occourance: ")
count=0
i=0
while i<len(string1):
    
    if string1[i]==char:
        count=count+1
    i=i+1
print("The number of time the",char,"occored in the string is",count)