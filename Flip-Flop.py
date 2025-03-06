def palid(r):
    e=len(r)-1
    s=0
    while s<e:
            if(r[s]!=r[e]):
                return False
            s+=1
            e-=1
    return True


r=(1,2,4,3,2,1)

if(palid(r))==True:
       print("Yes,the tuple is a flip-flop")
else:
       print("No the tuple does not flip flop")
       