def mach_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
            
    print("list of words with first and last character same \n",lst)
    return ctr
count= mach_words(['abc','cfc','xyz','12221'])
print("the number of words with the same first and last letters are",count)
    